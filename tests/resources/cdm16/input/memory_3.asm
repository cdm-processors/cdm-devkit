asect 0
main: ext               # Declare labels
default_handler: ext    # as external

# Interrupt vector table (IVT)
# Place a vector to program start and
# map all internal exceptions to default_handler
dc main, 0x0000         # Startup/Reset vector
dc default_handler, 0   # Unaligned SP
dc default_handler, 0   # Unaligned PC
dc default_handler, 0   # Invalid instruction
dc default_handler, 0   # Division by zero
dc 0, 0                 # Reserved
dc default_handler, 0   # Interrupt fault
align 0x80              # Reserve space for the rest
                        # of IVT

# Exception handlers section
rsect exc_handlers

# This handler halts processor
default_handler>
    halt

# Main program section
rsect main
data: ext
main>
    ldi r0, 0x8000
    ldi r1, 0xaabb

    ldi r2, -2
    ldi r3, -3

    stw r0, r2, r1
    stb r0, r3, r1

    ldw r0, r2, r4
    ldb r0, r2, r5
    ldsb r0, r2, r6

    ldi r0, data
    ldi r1, 2

    lcb r0, r1, r2
    lcsb r0, r1, r3
    lcw r0, r1, r7

    ldi r1, 1

    lcw r0, r1, r1

    lcw r0, r0

    halt

rsect data
data>
    dw 0xbbaa, 0xfa86

end.
