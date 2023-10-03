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
    # pups - push status register to stack
    # order: CVZN ((!) Carry-bit (!) oVerflow, Zero, Negative)
    # check add and sub with / without overflowing

    # ========================= Add tests =======================
    # Ordinary test case
    ldi r1, 15
    ldi r2, 16
    add r2, r1
    pups
    push r1

    # Zero test case
    ldi r1, 15
    ldi r2, -15
    add r2, r1
    pups
    push r1

    # Overflow (negative overflow) test case
    ldi r1, 32760
    ldi r2, 65
    add r2, r1
    pups
    push r1

    # Carry (unsigned overflow) test case
    ldi r1, 65530
    ldi r2, 65
    add r2, r1
    pups
    push r1

    # Just zero test case
    ldi r1, 0
    ldi r2, 0
    add r2, r1
    pups
    push r1

    # Just negative case
    ldi r1, 0
    ldi r2, -5
    add r2, r1
    pups
    push r1

    # Negative plus negative case
    ldi r1, -1
    ldi r2, -1
    add r2, r1
    pups
    push r1

    # Negative overflow case
    ldi r1, -32760
    ldi r2, -65
    add r2, r1
    pups
    push r1

    # ========================= Sub tests =======================

    # stps r0
    # and r2, r1
    # check for zeros

    halt

end.
