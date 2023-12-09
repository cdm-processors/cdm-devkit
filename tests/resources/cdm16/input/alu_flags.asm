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
    ldi r0, 31

    add r2, r1
    ldps r3
    add r3, 16
    push r3
    if
        cmp r1, r0
    is eq
        push 1
    else
        push 2
    fi

    # Zero test case
    ldi r1, 15
    ldi r2, -15
    ldi r0, 0

    add r2, r1
    ldps r3
    add r3, 16
    push r3
    if
        cmp r1, r0
    is eq
        push 1
    else
        push 2
    fi

    # Overflow (negative overflow) test case
    ldi r1, 32760
    ldi r2, 65
    ldi r0, 32825

    add r2, r1
    ldps r3
    add r3, 16
    push r3
    if
        cmp r1, r0
    is eq
        push 1
    else
        push 0
    fi

    # Carry (unsigned overflow) test case
    ldi r1, 65530
    ldi r2, 65
    ldi r0, 59

    add r2, r1
    ldps r3
    add r3, 16
    push r3
    if
        cmp r1, r0
    is eq
        push 1
    else
        push 2
    fi

    # Just zero test case
    ldi r1, 0
    ldi r2, 0
    ldi r0, 0

    add r2, r1
    ldps r3
    add r3, 16
    push r3
    if
        cmp r1, r0
    is eq
        push 1
    else
        push 2
    fi

    # Just negative case
    ldi r1, 0
    ldi r2, -5
    ldi r0, -5

    add r2, r1
    ldps r3
    add r3, 16
    push r3
    if
        cmp r1, r0
    is eq
        push 1
    else
        push 2
    fi

    # Negative plus negative case
    ldi r1, -1
    ldi r2, -1
    ldi r0, -2

    add r2, r1
    ldps r3
    add r3, 16
    push r3
    if
        cmp r1, r0
    is eq
        push 1
    else
        push 2
    fi

    # Negative overflow case
    ldi r1, -32760
    ldi r2, -65
    ldi r0, 32711

    add r2, r1
    ldps r3
    add r3, 16
    push r3
    if
        cmp r1, r0
    is eq
        push 1
    else
        push 2
    fi

    # ========================= Sub tests =======================
    # Ordinary test case
    ldi r1, 32
    ldi r2, 13
    ldi r0, 19

    sub r1, r2
    ldps r3
    add r3, 16
    push r3
    if
        cmp r2, r0
    is eq
        push 1
    else
        push 2
    fi

    # Zero test case
    ldi r1, 15
    ldi r2, 15
    ldi r0, 0

    sub r1, r2
    ldps r3
    add r3, 16
    push r3
    if
        cmp r2, r0
    is eq
        push 1
    else
        push 2
    fi

    # Overflow (negative overflow) test case
    ldi r1, 32760
    ldi r2, -65
    ldi r0, 32825

    sub r1, r2
    ldps r3
    add r3, 16
    push r3
    if
        cmp r2, r0
    is eq
        push 1
    else
        push 2
    fi

    # Carry (unsigned overflow) test case
    ldi r1, 65530
    ldi r2, -65
    ldi r0, 59

    sub r1, r2
    ldps r3
    add r3, 16
    push r3
    if
        cmp r2, r0
    is eq
        push 1
    else
        push 2
    fi

    # Just zero test case
    ldi r1, 0
    ldi r2, 0
    ldi r0, 0

    sub r1, r2
    ldps r3
    add r3, 16
    push r3
    if
        cmp r2, r0
    is eq
        push 1
    else
        push 2
    fi

    # Just negative case
    ldi r1, 0
    ldi r2, 5
    ldi r0, -5

    sub r1, r2
    ldps r3
    add r3, 16
    push r3
    if
        cmp r2, r0
    is eq
        push 1
    else
        push 2
    fi

    # Negative minus positive case
    ldi r1, -1
    ldi r2, 1
    ldi r0, -2

    sub r1, r2
    ldps r3
    add r3, 16
    push r3
    if
        cmp r2, r0
    is eq
        push 1
    else
        push 2
    fi

    # Negative overflow case
    ldi r1, -32760
    ldi r2, 65
    ldi r0, 32711

    sub r1, r2
    ldps r3
    add r3, 16
    push r3
    if
        cmp r2, r0
    is eq
        push 1
    else
        push 2
    fi

    halt

end.
