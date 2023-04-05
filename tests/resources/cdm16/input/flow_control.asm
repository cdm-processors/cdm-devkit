asect 0
main: ext               # Declare labels
default_handler: ext    # as external
custom_handler: ext

# Interrupt vector table (IVT)
# Place a vector to program start and
# map all internal exceptions to default_handler
dc main, 0x0400         # Startup/Reset vector
dc default_handler, 0   # Unaligned SP
dc default_handler, 0   # Unaligned PC
dc default_handler, 0   # Invalid instruction
dc default_handler, 0   # Division by zero
dc 0, 0                 # Reserved
dc default_handler, 0   # Interrupt fault
dc custom_handler, 0x20 # Test interrupt
align 0x80              # Reserve space for the rest
                        # of IVT

# Exception handlers section
rsect exc_handlers

# This handler halts processor
default_handler>
    halt

custom_handler>
    ldi r2, 0xeeff

    ldps fp

    rti

# Main program section
rsect main
main>

    ldi r0, 15

loop:

    dec r0

    bnz loop

    ldi r0, 0xdd

    jsr sub

    ldi r5, comp
    jsrr r5

    ldpc fp
    add fp, 6
    br far_br

    ldi r5, far_comp
    jsrr r5

    jsr far_jsr

    int 0x7

    halt

sub:
    ldi r1, 0xcc

    rts

comp:
    ldi r3, 0xbb

    rts

asect 0xaa00
far_br:
    ldi r4, 0xaa

    stpc fp

far_comp:
    ldi r5, 0x99

    rts

far_jsr:
    ldi r6, 0x88

    rts

end.
