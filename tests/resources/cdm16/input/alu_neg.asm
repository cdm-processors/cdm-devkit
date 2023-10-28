asect 0
main: ext               # Declare labels
default_handler: ext    # as external

# Interrupt vector table (IVT)
# Place a vector to program start and
# map all internal exceptions to default_handler
dc main, 0x8000         # Startup/Reset vector
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
    # 15
    ldi r0, 15
	neg r0

    ldps r1
    add r1, 16

	push r0
    push r1

    # -10
    ldi r0, -10
	neg r0

    ldps r1
    add r1, 16

	push r0
    push r1

    # 0
    ldi r0, 0
	neg r0

    ldps r1
    add r1, 16
    add r0, 15

	push r0
    push r1

    # 0x8000
    ldi r0, 0x8000
	neg r0

    ldps r1
    add r1, 16

	push r0
    push r1

    halt

end.