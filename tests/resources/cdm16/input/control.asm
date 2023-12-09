asect 0
main: ext               # Declare labels
default_handler: ext    # as external
right_handler: ext

# Interrupt vector table (IVT)
# Place a vector to program start and
# map all internal exceptions to default_handler
dc main, 0              # Startup/Reset vector
dc right_handler, 0     # Unaligned SP
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

right_handler>
    ldi fp, 0xaabb

    halt

# Main program section
rsect main
main>
    ei

    ldps r0

    di

    ldps r1

    tst r2

    bnz stop

    inc r2

    reset

stop:

    reset 1

end.
