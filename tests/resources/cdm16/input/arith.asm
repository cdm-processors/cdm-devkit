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

    ldi r0, 2
    ldi r1, 3

    add r0, r1, r2
    push r2

    add r2, 50
    push r2

    sub r2, 10
    push r2

    inc r2
    push r2

    dec r2
    push r2

    sub r0, r1, r2
    push r2

    neg r2
    push r2

    ldi r2, 0x7f
    sxt r2
    push r2
    scl r2
    push r2

    ldi r2, 0x80
    sxt r2
    push r2
    scl r2
    push r2

    clr r2
    inc r2
    push r2

    ldi r0, 0b111
    ldi r1, 0b010

    and r0, r1, r2
    push r2

    or r0, r1, r2
    push r2

    ldi r1, 0b1010

    xor r0, r1, r2
    push r2

    ldi r2, 0xffff

    not r2
    inc r2
    push r2

    ldi r1, 0b010

    bic r0, r1, r2
    push r2

    ldi r0, 10

    shl r0, r2, 1
    push r2

    shr r0, r2, 1
    push r2

    ldi r0, 0xff00

    shra r0, r2, 1
    push r2

    ldi r0, 0x0f00

    shra r0, r2, 1
    push r2

    ldi r0, 0xaabb

    rol r0, r2, 2
    push r2

    ror r0, r2, 2
    push r2

    tst r5

    rcr r0, r2, 2
    push r2

    rcl r0, r2, 2
    push r2


    ldi r0, 5
    ldi r1, 6

    add r0, r1, r2
    push r2

    add r0, r1
    push r1

    clr r0

    not r0, r1
    push r1

    not r0
    push r0

    ldi r0, 0x0f00

    shr r0, r1, 1
    push r1

    shr r0, r2
    push r2

    move r0, r3
    shr r3, 1
    push r3

    shr r0
    push r0

    halt

end.
