# CdM-16 Overview

**CdM-16** is 16-bit RISC processor.

**Basic information:**
+ 64k address space
+ 16-bit arithmetics
+ 16-bit registers

## Registers
+ **8 general purpose** registers *(r0..r7)*
+ **r7** is called **fp** aka **frame pointer**, can be used with a special addressing mode
+ **SP** - **stack pointer**, points to the top of the stack, stack grows downwards, should be aligned by 2, otherwise an exception is raised
+ **PC** - **program coutner**, points to the next instruction that will be fetched, should be aligned by 2, otherwise an exception is raised
+ **PSR** - **processor status register** *(or just **PS**)*, contains arithemic flag bit fields and interrupt enable bit field <br>
  *(sometimes called **PSW** - **processor status word**)*

**Structure of *PS*:**
<table>
  <thead><tr>
    <th>15</th><th>14</th><th>13</th><th>12</th><th>11</th><th>10</th><th>9</th><th>8</th><th>7</th><th>6</th><th>5</th><th>4</th><th>3</th><th>2</th><th>1</th><th>0</th>
  </tr></thead>
  <tbody align=center><tr>
    <td>I</td>
    <td colspan=11>R</td>
    <td>C</td>
    <td>V</td>
    <td>Z</td>
    <td>N</td>
  </tr></tbody>
</table>

+ **I** - interrupt enable bit field, interrupts are enabled if this bit is set
+ **C, V, Z, N** - arithmetic flags, have the same meaning as in CdM-8/8e
+ **R** - reserved, these bit fields are not used

## Instruction operands

**Operands used in the instructions can have following types:**
+ **rs, rs0, rs1, rd** - registers *(r0, r1, r2, r3, r4, r5, r6, r7, fp)*

+ **imm6, imm9** - short immediate value, can be interpreted as positive or negative (2's compement) integer
  + **imm6** - can take values from -64 to 63
  + **imm9** - can take values from -512 to 511

+ **imm16** - long immediate value, 16-bit integer or label

Some commands have variants with both **imm6/imm9** and **imm16** operands, but programmer don't have to worry about it as assembler will put appropriate command automatically.
However, programmer should not exceed size of maximum available operand type.

> This is done that way as, in fact, it gives some ability to optimize code as **imm6/imm9** variants take less space (2 bytes) than **imm16** variants (4 bytes).
> 
> *Example: `ldi r0, 15` with long immediate is encoded as `10 20 0f 00`, but assembler will optimize it and encode it as `78 74` instead.*

## Instuction set

### Memory access instructions

**Store and load by address:**
|              Instruction               |                     Description                       | Flags <br> affected | Time <br> (cycles) | Size <br> (bytes) |
| :------------------------------------: | :---------------------------------------------------: | :-----------------: | :----------------: | :---------------: |
| **ldw** ***rs***, ***rd*** | **Load word**. Loads 2 bytes from data memory pointed by ***rs*** to ***rd***. | - | 1-2 | 2 |
| **ldb** ***rs***, ***rd*** | **Load byte**. Loads a byte from data memory pointed by ***rs*** to ***rd***. | - | 1-2 | 2 |
| **ldsb** ***rs***, ***rd*** | **Load signed byte**. Loads a byte from data memory pointed <br> by ***rs*** to ***rd*** with sign-extend. | - | 1-2 | 2 |
| **lcw** ***rs***, ***rd*** | **Load constant word**. Loads 2 bytes from instruction memory pointed <br> by ***rs*** to ***rd***. | - | 1-2 | 2 |
| **lcb** ***rs***, ***rd*** | **Load constant byte**. Loads a byte from instruction memory pointed <br> by ***rs*** to ***rd***. | - | 1-2 | 2 |
| **lcsb** ***rs***, ***rd*** | **Load constant signed byte**. Loads a byte from  instruction memory pointed <br> by ***rs*** to ***rd*** with sign-extend. | - | 1-2 | 2 |
| **stw** ***rs***, ***rd*** | **Store word**. Stores 2 bytes from ***rd*** to data memory pointed by ***rs***. | - | 1-2 | 2 |
| **stb** ***rs***, ***rd*** | **Store byte**. Stores a lower byte from ***rd*** to data memory pointed by ***rs***. | - | 1-2 | 2 |

**These instructions have 3 operand analogues:**
|              Instruction               |                     Description                       | Flags <br> affected | Time <br> (cycles) | Size <br> (bytes) |
| :------------------------------------: | :---------------------------------------------------: | :-----------------: | :----------------: | :---------------: |
| **ldw** ***rs0***, ***rs1***, ***rd*** | **Load word**. Loads 2 bytes from data memory pointed by ***rs0* + *rs1*** to ***rd***. | - | 1-2 | 2 |
| **ldb** ***rs0***, ***rs1***, ***rd*** | **Load byte**. Loads a byte from data memory pointed by ***rs0* + *rs1*** to ***rd***. | - | 1-2 | 2 |
| **ldsb** ***rs0***, ***rs1***, ***rd*** | **Load signed byte**. Loads a byte from data memory pointed <br> by ***rs0* + *rs1*** to ***rd*** with sign-extend. | - | 1-2 | 2 |
| **lcw** ***rs0***, ***rs1***, ***rd*** | **Load constant word**. Loads 2 bytes from instruction memory pointed <br> by ***rs0* + *rs1*** to ***rd***. | - | 1-2 | 2 |
| **lcb** ***rs0***, ***rs1***, ***rd*** | **Load constant byte**. Loads a byte from instruction memory pointed <br> by ***rs0* + *rs1*** to ***rd***. | - | 1-2 | 2 |
| **lcsb** ***rs0***, ***rs1***, ***rd*** | **Load constant signed byte**. Loads a byte from  instruction memory pointed <br> by ***rs0* + *rs1*** to ***rd*** with sign-extend. | - | 1-2 | 2 |
| **stw** ***rs0***, ***rs1***, ***rd*** | **Store word**. Stores 2 bytes from ***rd*** to data memory pointed by ***rs0* + *rs1***. | - | 1-2 | 2 |
| **stb** ***rs0***, ***rs1***, ***rd*** | **Store byte**. Stores a lower byte from ***rd*** to data memory pointed by ***rs0* + *rs1***. | - | 1-2 | 2 |

**Macros:**
|                  Macro                 |                     Description                       |      Expansion      |
| :------------------------------------: | :---------------------------------------------------: | :-----------------: |
| **ld** ***rs***, ***rd*** | **Load from memory**. Simulates **CdM-8/8e** **ld** instruction. Operates with words. | **ldw** ***rs***, ***rd*** | 
| **ldc** ***rs***, ***rd*** | **Load constatnt from memory**. Simulates **CdM-8/8e** **ldc** instruction. Operates with words. | **lcw** ***rs***, ***rd*** | 
| **st** ***rs***, ***rd*** | **Store to memory**. Simulates **CdM-8/8e** **st** instruction. Operates with words. | **stw** ***rs***, ***rd*** | 

**Operations with stack:**

+ When a **push** is performed, processor decrements **SP** by 2 bytes and stores data to memory pointed by new **SP** <br> *(resulting address is **SP-2**)*.
+ When a **pop** is performed, processor loads data from memory pointed by **SP** and then increments **SP** by 2 bytes.

|              Instruction               |                     Description                       | Flags <br> affected | Time <br> (cycles) | Size <br> (bytes) |
| :------------------------------------: | :---------------------------------------------------: | :-----------------: | :----------------: | :---------------: |
| **push** ***rd*** | **Push register**. Stores contents of ***rd*** to the top of the stack. | - | 1 | 2 |
| **push** ***imm9*** | **Push immediate**. Stores immediate value ***imm9*** to the top of the stack. | - | 1 | 2 |
| **pop** ***rd*** | **Pop register**. Loads a value from the top of the stack to ***rd***. | - | 1 | 2 |
| **pupc** | **Push PC**. Pushes ***PC*** to the stack. | - | 1 | 2 |
| **popc** | **Pop PC**. Pops ***PC*** from the stack. | - | 1 | 2 |
| **pusp** | **Push SP**. Pushes ***SP*** to the stack. | - | 1 | 2 |
| **posp** | **Pop SP**. Pops ***SP*** from the stack. This operation doesn't increment ***SP***. | - | 1 | 2 |
| **pups** | **Push PS**. Pushes ***PS*** to the stack. | - | 1 | 2 |
| **pops** | **Pop PS**. Pops ***PS*** from the stack. | - | 1 | 2 |

**Operations with frame pointer:**

Processor can access data by adding a constant to **fp**. There, ***off*** is an immediate value, offset to **fp** in bytes.

There are some limitations:
+ For **byte** variants: $-64 \leq off < 64$
+ For **word** variants: $-128 \leq off < 128$ and ***off*** must be **even**

> **Note:** ***off*** will be expanded by assembler as ***off*** = ***imm6* \* *size***. This gives limitations above. 

|              Instruction               |                     Description                       | Flags <br> affected | Time <br> (cycles) | Size <br> (bytes) |
| :------------------------------------: | :---------------------------------------------------: | :-----------------: | :----------------: | :---------------: |
| **lsw** ***rd***, ***off*** | **Load word relative to *fp***. Loads a word from memory locaton ***fp* + *off*** to ***rd***. | - | 1 | 2 |
| **lsb** ***rd***, ***off*** | **Load byte relative to *fp***. Loads a byte from memory locaton ***fp* + *off*** to ***rd***. | - | 1 | 2 |
| **lssb** ***rd***, ***off*** | **Load signed byte relative to *fp***. Loads a byte from memory<br>locaton ***fp* + *off*** to ***rd*** with sign-extend. | - | 1 | 2 |
| **ssw** ***rd***, ***off*** | **Store word relative to *fp***. Stores a word from ***rd*** to memory locaton ***fp* + *off***. | - | 1 | 2 |
| **ssb** ***rd***, ***off*** | **Store byte relative to *fp***. Stores a lower byte of ***rd*** to memory locaton ***fp* + *off***. | - | 1 | 2 |

### Flow control instructions:
Asterisk *(\*)* in branch instuctions is a condition. It must be replaced with one of condition codes:

| Condition code | Description | 
| :------------: | :---------: |
| **eq/z** | equal, equal to zero, **Z** is set |
| **ne/nz** | not equal, not zero, **Z** is clear |
| **hs/cs** | unsigned higher or same, **C** is set |
| **lo/cc** | unsigned lower, **C** is clear |
| **mi** | negative (minus) |
| **pl** | positive or zero (plus) |
| **vs** | **V** is set |
| **vc** | **V** is clear |
| **hi** | unsigned higher |
| **ls** | unsigned lower or same |
| **ge** | greater than or equal |
| **lt** | less than, less than zero |
| **gt** | greater than |
| **le** | less than or equal |
| **r** | unconditional branch |

Instruction changes **PC** only if this condition is met, processor determines it by testing condition against **C, V, Z, N** flags in **PS** register.

*Examples:*
```python
br foo # unconditional branch
  
cmp r0, r1 
beq bar # branch if r0 == r1
  
tst r0
bz # branch if r0 == 0
```

|              Instruction               |                     Description                       | Flags <br> affected | Time <br> (cycles) | Size <br> (bytes) |
| :------------------------------------: | :---------------------------------------------------: | :-----------------: | :----------------: | :---------------: |
| **b\*** ***imm16*** | **Absolute branch**. Loads ***imm16*** to **PC**, thus passing control to the instruction located at the address ***imm16***. | - | 1 | 4 |
| **b\*** ***imm9*** | **Relative branch**. Adds value ***imm9* \* *2*** to **PC**, thus passing control to the instruction located at the address **PC + (*imm9* \* *2*) + *2***. | - | 1 | 2 |
| **jsr** ***imm16*** | **Jump to subroutine (Absolute)**. Pushes **PC** to stack and then does unconditional <br> absolute branch to address ***imm16***. | - | 2 | 4 |
| **jsr** ***imm9*** | **Jump to subroutine (Relative)**. Pushes **PC** to stack and then does unconditional <br> relative branch with offset ***imm9***. | - | 2 | 2 |
| **jsrr** ***rd*** | **Jump to subroutine by pointer**. Pushes **PC** to stack and then does unconditional <br> absolute branch to address contained in ***rd***. | - | 2 | 2 |
| **int** ***imm9*** | **Sofware interrupt**. Triggers an interrupt with vector with number ***imm9***. | - | 4 | 2 |
| **rti** | **Return from iterrupt**. Pops **PC** and **PS** from stack and thus returns <br> control to the caller code and restores **PS**. | - | 2 | 2 |

**Macros**
|                  Macro                 |                     Description                       |      Expansion      |
| :------------------------------------: | :---------------------------------------------------: | :-----------------: |
| **rts** | **Return from subroutine**. Pops **PC** from stack and thus returns control to the caller code. <br> *(Assuming return address was previosly pushed to stack, for exmaple, with **jsr**)* | **popc** |


### Register transfer instructions:
|              Instruction               |                     Description                       | Flags <br> affected | Time <br> (cycles) | Size <br> (bytes) |
| :------------------------------------: | :---------------------------------------------------: | :-----------------: | :----------------: | :---------------: |
| **ldi** ***rd***, ***imm16*** | **Load immediate to register**. Loads immedaite value ***imm16*** to ***rd***. | - | 1 | 4 |
| **ldi** ***rd***, ***imm6*** | **Load short immediate to register**. Loads immedaite value ***imm6*** to ***rd***. | - | 1 | 2 |
| **move** ***rs***, ***rd*** | **Copy register**. Copies value from ***rs*** to ***rd***. | C, V, Z, N | 1 | 2 |
| **addsp** ***imm9*** | **Add immediate to SP**. Adds ***imm9* * *2*** to **SP**. <br> (***imm9** is number of **words***) | - | 1 | 2 |
| **ldsp** ***rd*** | **Load SP**. Copies value from **SP** to ***rd***. | - | 1 | 2 |
| **stsp** ***rd*** | **Store SP**. Copies value from ***rd*** to **SP**. | - | 1 | 2 |
| **ldps** ***rd*** | **Load PS**. Copies value from **PS** to ***rd***. | - | 1 | 2 |
| **stps** ***rd*** | **Store PS**. Copies value from ***rd*** to **PS**. | - | 1 | 2 |
| **ldpc** ***rd*** | **Load PC**. Copies value from **PC** to ***rd***. | - | 1 | 2 |
| **stpc** ***rd*** | **Store PC**. Copies value from ***rd*** to **PC**. | - | 1 | 2 |

### Processor control instructions:
|              Instruction               |                     Description                       | Flags <br> affected | Time <br> (cycles) | Size <br> (bytes) |
| :------------------------------------: | :---------------------------------------------------: | :-----------------: | :----------------: | :---------------: |
| **halt** | **Halt processor**. Stops processor clock, changes processor status to **HALTED**. | - | 1 | 2 |
| **wait** | **Wait for an interrupt**. Stops processor clock until an interrupt or an exception <br> occurs, changes processor status to **WAITING**. | - | 1 | 2 |
| **reset** | **Reset processor**. Fetches reset vector thus performing soft reset. | - | 2 | 2 |
| **reset** ***imm9*** | **Reset processor**. Fetches vector ***imm9*** thus performing soft reset. | - | 2 | 2 |
| **ei** | **Enable interrupts**. Sets **I** bit *(bit 15)* in **PS** thus enabling interrupts. | - | 1 | 2 |
| **di** | **Disable interrupts**. Clears **I** bit *(bit 15)* in **PS** thus disabling interrupts. | - | 1 | 2 |

**Macros:**
|                  Macro                 |                     Description                       |      Expansion      |
| :------------------------------------: | :---------------------------------------------------: | :-----------------: |
| **nop** | **No operation**. Performs no operation. Processor executes this instruction with no side <br> effects except for updated **PC**. Can be used for creating delay or filling up space.  | **bfalse** ***_nop*** |

### Arithmetic instructions:
|              Instruction               |                     Description                       | Flags <br> affected | Time <br> (cycles) | Size <br> (bytes) |
| :------------------------------------: | :---------------------------------------------------: | :-----------------: | :----------------: | :---------------: |
| **add** ***rs0***, ***rs1***, ***rd*** | **Add**. Computes ***rs0* + *rs1*** and puts result in ***rd***. | C, V, Z, N | 1 | 2 |
| **add** ***rd***, ***imm6*** | **Add immediate**. Computes ***rs0* + *imm6*** and puts result in ***rd***. | C, V, Z, N | 1 | 2 |
| **addc** ***rs0***, ***rs1***, ***rd*** | **Add with carry**. Computes ***rs0* + *rs1* + *C*** and puts result in ***rd***. | C, V, Z, N | 1 | 2 |
| **sub** ***rs0***, ***rs1***, ***rd*** | **Substract**. Computes ***rs0* - *rs1*** and puts result in ***rd***. | C, V, Z, N | 1 | 2 |
| **sub** ***rd***, ***imm6*** | **Substract immediate**. Computes ***rs0* - *imm6*** and puts result in ***rd***. | C, V, Z, N | 1 | 2 |
| **subc** ***rs0***, ***rs1***, ***rd*** | **Substract with carry**. Computes ***rs0* - *rs1* + *C* - *1*** and puts result in ***rd***. | C, V, Z, N | 1 | 2 |
| **neg** ***rs***, ***rd*** | **Negation**. Computes **-*rs*** (2's complement) and puts result in ***rd***. | Z, N | 1 | 2 |
| **sxt** ***rs***, ***rd*** | **Sign extend**. Fills higher 8 bits with 7-th bit of ***rs*** and puts result in ***rd***. | Z, N | 1 | 2 |
| **scl** ***rs***, ***rd*** | **Sign clear**. Clears higher 8 bits of ***rs*** and puts result in ***rd***. | Z, N | 1 | 2 |

**Macros:**
|                  Macro                 |                     Description                       |      Expansion      |
| :------------------------------------: | :---------------------------------------------------: | :-----------------: |
| **inc** ***rd*** | **Increment register**. Increments register by 1 and sets all flags according to the result. | **add** ***rd***, ***1*** | 
| **dec** ***rd*** | **Decrement register**. Decrements register by 1 and sets all flags according to the result. | **sub** ***rd***, ***1*** |
| **clr** ***rd*** | **Clear register**. Sets register to 0 and sets flags according to its value before operation. | **sub** ***rd***, ***rd*** | 

### Logic instructions:
|              Instruction               |                     Description                       | Flags <br> affected | Time <br> (cycles) | Size <br> (bytes) |
| :------------------------------------: | :---------------------------------------------------: | :-----------------: | :----------------: | :---------------: |
| **and** ***rs0***, ***rs1***, ***rd*** | Bitwise **and**. Computes ***rs0* & *rs1*** and puts result in ***rd***. | Z, N | 1 | 2 |
| **or** ***rs0***, ***rs1***, ***rd*** | Bitwise **or**. Computes ***rs0* \| *rs1*** and puts result in ***rd***. | Z, N | 1 | 2 |
| **xor** ***rs0***, ***rs1***, ***rd*** | Bitwise **xor**. Computes ***rs0* ^ *rs1*** and puts result in ***rd***. | Z, N | 1 | 2 |
| **not** ***rs***, ***rd*** | Bitwise **not**. Computes **~*rs*** (1's complement) and puts result in ***rd***. | Z, N | 1 | 2 |
| **bic** ***rs0***, ***rs1***, ***rd*** | **Bit clear**. Clears bits in ***rs0*** that are set in ***rs1***. <br> Computes ***rs0* & (~*rs1***) and puts result in ***rd***. | Z, N | 1 | 2 |

**Macros:**
|                  Macro                 |                     Description                       |      Expansion      |
| :------------------------------------: | :---------------------------------------------------: | :-----------------: |
| **bis** ***rs0***, ***rs1***, ***rd*** | **Bit set**. Sets bits in ***rs0*** that are set in ***rs1***. Computes ***rs0* \| *rs1*** and puts result in ***rd***. | **or** ***rs0***, ***rs1***, ***rd*** | 

### Shift instructions:
**CdM-16** has a barrel shifter that can performs shifts from **1** to **8** postitions, ***val*** determines distance of shift.

+ **Z, N** flags is set accoding to resulting number
+ **C** is set according to last shifted bit

|              Instruction               |                     Description                       | Flags <br> affected | Time <br> (cycles) | Size <br> (bytes) |
| :------------------------------------: | :---------------------------------------------------: | :-----------------: | :----------------: | :---------------: |
| **shl** ***rs***, ***rd***, ***val*** | **Logic left shift**. Shifts left and fills with zeros. | C, Z, N | 1 | 2 |
| **shr** ***rs***, ***rd***, ***val*** | **Logic right shift**. Shifts right and fills with zeros. | C, Z, N | 1 | 2 |
| **shra** ***rs***, ***rd***, ***val*** | **Arithmetic right shift**. Shifts right and fills with sign bit <br> *(most significant bit of inital number)*. | C, Z, N | 1 | 2 |
| **rol** ***rs***, ***rd***, ***val*** | **Cyclic left shift**. Shifts left, bit 15 shifts to bit 0. | C, Z, N | 1 | 2 |
| **ror** ***rs***, ***rd***, ***val*** | **Cyclic right shift**. Shifts right, bit 0 shifts to bit 15. | C, Z, N | 1 | 2 |
| **rcl** ***rs***, ***rd***, ***val*** | **Cyclic left shift with carry**. Shifts left, bit 15 shifts to **C**, old **C** shifts to bit 0. | C, Z, N | 1 | 2 |
| **rcr** ***rs***, ***rd***, ***val*** | **Cyclic right shift with carry**. Shifts right, bit 0 shifts to **C**, old **C** shifts to bit 15. | C, Z, N | 1 | 2 |

### Compare instructions:
|              Instruction               |                     Description                       | Flags <br> affected | Time <br> (cycles) | Size <br> (bytes) |
| :------------------------------------: | :---------------------------------------------------: | :-----------------: | :----------------: | :---------------: |
| **cmp** ***rs***, ***rd*** | **Compare**. Performs indestructive subrtaction, sets flags <br> and thus compares numbers in registers ***rs*** and ***rd***. | C, V, Z, N | 1 | 2 |
| **cmp** ***rs***, ***imm6*** | **Compare with immediate**. Performs indestructive subrtaction, sets flags <br> and thus compares numbers ***rs*** and ***imm6***. | C, V, Z, N | 1 | 2 |
| **bit** ***rs***, ***rd*** | **Bit test**. Performs indestructive **AND** and sets flags. If any of bits that <br> are set in bitmask ***rd*** are also set in ***rs***, then **Z** is **0**, otherwise **Z** is **1**. | Z, N | 1 | 2 |

**Macros:**
|                  Macro                 |                     Description                       |      Expansion      |
| :------------------------------------: | :---------------------------------------------------: | :-----------------: |
| **tst** ***rd*** | **Test register**. Compares register with iteself and sets **Z, N** flags according to the result. | **move** ***rd***, ***rd*** | 







