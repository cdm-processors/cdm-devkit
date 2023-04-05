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
    ldi fp, 0x8000

    ldi r0, 0x8879
    ldi r1, 0x55

    ssw r0, 0

    ldi r0, 0xaabb

    ssw r0, 2
    ssb r1, 4
    ssb r0, 5

    ssw r0, -2
    ssb r1, -4
    ssb r0, -3

    lsw r2, 2
    lsb r3, 4
    lssb r4, 5

    lsw r5, -2
    lsb r0, -4
    lssb r1, -3

    lssb fp, 0

    halt

end.
