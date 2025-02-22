# Assembly templates

In order to run properly processors need some boilerplate code.

## CdM-8/8e

CdM-8/8e start execution from `0x00` address, so you can place instructions directly at the beginning of memory with `asect 0` directive.

```python
asect 0
# Your program starts from 0x00 address

start:
    # your code here

end.
```

However, good practice is to put your executable code in some `rsect` and add a label at the beginning of this section. Then, put branch to that label at address `0x00`.

## CdM-16

When using CdM-16, you are required to initialize [IVT](./cdm16/cdm16-overview.md#startup-and-ivt). You should put address of entry point of your program at address `0x00`. Moreover you should put addresses of several exception handles in next vectors.

The code below will initialize IVT. That way, program entry point is `main` label and all exceptions are handled with `default_handler` which halts the processor.
```python
asect 0
main: ext               # Declare labels
default_handler: ext    # as external

# Interrupt vector table (IVT)
# Place a vector to program start and
# map all internal exceptions to default_handler
dc main, 0              # Startup/Reset vector
dc default_handler, 0   # Unaligned SP
dc default_handler, 0   # Unaligned PC
dc default_handler, 0   # Invalid instruction
dc default_handler, 0   # Double fault
align 0x80              # Reserve space for the rest 
                        # of IVT

# Exception handlers section
rsect exc_handlers

# This handler halts processor
default_handler>
    halt

# Main program section
rsect main

main>
    # your code here

end.
```
