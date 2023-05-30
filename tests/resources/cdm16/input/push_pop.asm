asect 0
default_handler: ext    # Declare label
                        # as external

# Interrupt vector table (IVT)
# Place a vector to program start and
# map all internal exceptions to default_handler
dc main, 0x1234         # Startup/Reset vector
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
asect 0x100
main:
    ldi r0, 0xaabb	# 100, 101, 102, 103
	
    
    push r0         # 104, 105
    push 1          # 106, 107
    push -1         # 108, 109

    push 15         # 10a, 10b
    pop r1          # 10c, 10d

    pupc            # 10e, 10f
    pusp
    pups

    ldi r7, 0x8000
    push fp

    rts

asect 0x8000
    push 10
    pops

    push 0x0e
    posp

    halt

end.
