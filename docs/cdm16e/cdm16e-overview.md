# CdM-16e Processor
CdM-16e is a modified version of CdM-16 that serves as a playground for testing various ideas.

It is highly extensible as it features additional microcode bank, so it has free space for both new instructions and new microcode commands.

## Modifications

For now, the `OS Extension` is implemented, it includes:
+ System and user mode
+ Shadow `SP`
+ Bit fields in `PS` that store information about current context
+ Atomic exchange instruction

There are some ideas that haven't been implemented yet:
+ Group `push` and `pop` instructions
+ Arithmetic extension that includes:
  + Additional 32-bit registers for advanced arithmetic operations
  + Multiplier and divider
  + Floating point arithmetic

## Modifications description

### PS
PS register is extended with new flags that indicate current processor mode *(MD)* and store information relevant to MMU *(IO, Context number)*

<table>
  <thead><tr>
    <th>15</th><th>14</th><th>13</th><th>12</th><th>11</th><th>10</th><th>9</th><th>8</th><th>7</th><th>6</th><th>5</th><th>4</th><th>3</th><th>2</th><th>1</th><th>0</th>
  </tr></thead>
  <tbody align=center><tr>
    <td>IE</td>
    <td>MD</td>
    <td>IO</td>
    <td>R</td>
    <td colspan=8>Context number</td>
    <td>C</td>
    <td>V</td>
    <td>Z</td>
    <td>N</td>
  </tr></tbody>
</table>

- **IE** - interrupt enable
- **MD** - mode (0 - system, 1 - user)
- **IO** - IO header presence
- **R** - Reserved
- **Context number** - number of current context for MMU
- **C, V, Z, N** - arithmetic flags

**IO** and **Context number** have correspondent processor pins to interface with MMU


### System and User modes
Processor has two operating modes: **system** and **user**. Instructions are then divided into two categories: **privileged** and **non-privileged**.

+ **Non-privileged** instructions can be executed in both modes.
+ **Privileged** instructions can be executed only in system mode. Trying to execute privileged instruction in user mode will trigger an execption.


### SP
There are two SP registers. One for system mode and one for user mode. **Active** SP is selected according to MD flag. Other one is called **shadow** SP.

Instructions that interact with SP use active one. Special system-mode instructions are used to interact with shadow SP.

+ `ldssp rd`, `stssp rd` - move from/to shadow SP from GP register `rd`


### Interrupt handling
As processor support system and user modes, interrupt handling routine is different. 

Interrupts and exceptions are handled with `int` instruction that is fetched virtually or physically. This instruction saves PC and PS on stack and then loads new PC and PS from interrupt vector.

Since we have different stacks for user and system mode, and we need to save registers to system stack, we firstly need to switch to system mode.

Then, behaviour of `int` instruction is following:
+ Save PC and PS to temporary registers inside processor
+ Load new PC and PS from interrupt vector, thus switch to system mode
+ Push PC and PS from temporary registers to system stack


### Syscalls
Processor supports syscalls through `int` instruction. This instruction is privileged i.e. works only in system mode. However, executing this instruction with a special reserved vector number is considered a system call and won't trigger privilege violation execption when executed in user mode.

Vector 7 is reserved for syscall, so to invoke a syscall one can use `int 0x7` or `syscall` macro.

### IVT
IVT have two new entries: one for privilege violation exception and another for system call.

| Vector no. | Offset |                   Name                   |
|:----------:|:------:|:----------------------------------------:|
|     0      |  0x00  |              Startup/Reset               |
|     1      |  0x04  |               Unaligned SP               | 
|     2      |  0x08  |               Unaligned PC               |
|     3      |  0x0C  |           Invalid instruction            |
|     4      |  0x10  |               Double fault               |
|     5      |  0x14  |           Privilege violation            |
|     6      |  0x18  |                 Reserved                 |
|     7      |  0x1С  |                  Syscall                 |
|    ... <br> 63    |  ... <br> 0xFC  | External interrupts <br> and exceptions |


### Atomic exchange
This instrucion atomically exchanges contents of memory pointed by `rs` with `rd`. It can be used to implement synchronization primitives.

+ `swpw rs, rd` - word variant
+ `swpb rs, rd` - byte variant
