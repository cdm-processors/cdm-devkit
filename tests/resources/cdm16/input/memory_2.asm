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
main>
    ldi r0, 0x8000
    ldi r1, 0x8002

    ldi r2, 0xaabb

    stw r0, r2
    stb r1, r2

    ldw r0, r3
    ldb r1, r4
    ldsb r1, r5

    ldi r0, 0x9000
    ldi r1, 0

    stw r0, r1, r2

    ldi r1, 2

    stb r0, r1, r2

    ldi r1, 0

    ldw r0, r1, r6
    
    ldi r1, 2

    ldb r0, r1, r7

    ldsb r0, r1, r2

    halt

end.
