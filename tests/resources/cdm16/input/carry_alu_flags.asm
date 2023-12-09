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

    # ========================= Addc (basic) tests =======================
    # Ordinary test case
    ldi r3, 0
    ldi r4, 0
    ldi r1, 15
    ldi r2, 16
    ldi r0, 31

    add r3, r4
    addc r2, r1
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
    ldi r3, 0
    ldi r4, 0
    ldi r1, 15
    ldi r2, -15
    ldi r0, 0

    add r3, r4
    addc r2, r1
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
    ldi r3, 0
    ldi r4, 0
    ldi r1, 32760
    ldi r2, 65
    ldi r0, 32825

    add r3, r4
    addc r2, r1
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
    ldi r3, 0
    ldi r4, 0
    ldi r1, 65530
    ldi r2, 65
    ldi r0, 59

    add r3, r4
    addc r2, r1
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
    ldi r3, 0
    ldi r4, 0
    ldi r1, 0
    ldi r2, 0
    ldi r0, 0

    add r3, r4
    addc r2, r1
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
    ldi r3, 0
    ldi r4, 0
    ldi r1, 0
    ldi r2, -5
    ldi r0, -5

    add r3, r4
    addc r2, r1
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
    ldi r3, 0
    ldi r4, 0
    ldi r1, -1
    ldi r2, -1
    ldi r0, -2

    add r3, r4
    addc r2, r1
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
    ldi r3, 0
    ldi r4, 0
    ldi r1, -32760
    ldi r2, -65
    ldi r0, 32711

    add r3, r4
    addc r2, r1
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

    # ========================= Addc (specific) tests =======================
    # Ordinary test case
    ldi r3, 65535
    ldi r4, 65535
    ldi r1, 15
    ldi r2, 16
    ldi r0, 32

    add r3, r4
    addc r2, r1
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
    ldi r3, 65535
    ldi r4, 65535
    ldi r1, 15
    ldi r2, -16
    ldi r0, 0

    add r3, r4
    addc r2, r1
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
    ldi r3, 65535
    ldi r4, 65535
    ldi r1, 32760
    ldi r2, 7
    ldi r0, 32768

    add r3, r4
    addc r2, r1
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
    ldi r3, 65535
    ldi r4, 65535
    ldi r1, 65530
    ldi r2, 5
    ldi r0, 0

    add r3, r4
    addc r2, r1
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

    # Just zero (?) test case
    ldi r3, 65535
    ldi r4, 65535
    ldi r1, -1
    ldi r2, 0
    ldi r0, 0

    add r3, r4
    addc r2, r1
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
    ldi r3, 65535
    ldi r4, 65535
    ldi r1, 0
    ldi r2, -5
    ldi r0, -4

    add r3, r4
    addc r2, r1
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
    ldi r3, 65535
    ldi r4, 65535
    ldi r1, -1
    ldi r2, -1
    ldi r0, -1

    add r3, r4
    addc r2, r1
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

    # Negative overflow (?) case
    ldi r3, 65535
    ldi r4, 65535
    ldi r1, -32760
    ldi r2, -7
    ldi r0, -32766

    add r3, r4
    addc r2, r1
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

    # ========================= Subc (basic) tests =======================
    # Ordinary test case
    ldi r3, 5
    ldi r4, 3
    ldi r1, 32
    ldi r2, 13
    ldi r0, 19

    sub r3, r4
    subc r1, r2
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
    ldi r3, 5
    ldi r4, 3
    ldi r1, 15
    ldi r2, 15
    ldi r0, 0

    sub r3, r4
    subc r1, r2
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
    ldi r3, 5
    ldi r4, 3
    ldi r1, 32760
    ldi r2, -65
    ldi r0, 32825

    sub r3, r4
    subc r1, r2
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
    ldi r3, 5
    ldi r4, 3
    ldi r1, 65530
    ldi r2, -65
    ldi r0, 59

    sub r3, r4
    subc r1, r2
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
    ldi r3, 5
    ldi r4, 3
    ldi r1, 0
    ldi r2, 0
    ldi r0, 0

    sub r3, r4
    subc r1, r2
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
    ldi r3, 5
    ldi r4, 3
    ldi r1, 0
    ldi r2, 5
    ldi r0, -5

    sub r3, r4
    subc r1, r2
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
    ldi r3, 5
    ldi r4, 3
    ldi r1, -1
    ldi r2, 1
    ldi r0, -2

    sub r3, r4
    subc r1, r2
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
    ldi r3, 5
    ldi r4, 3
    ldi r1, -32760
    ldi r2, 65
    ldi r0, 32711

    sub r3, r4
    subc r1, r2
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

    # ========================= Subc (specific) tests =======================
    # Ordinary test case
    ldi r3, 1
    ldi r4, 7
    ldi r1, 32
    ldi r2, 13
    ldi r0, 18

    sub r3, r4
    subc r1, r2
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
    ldi r3, 1
    ldi r4, 7
    ldi r1, 15
    ldi r2, 14
    ldi r0, 0

    sub r3, r4
    subc r1, r2
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

    # Overflow (?) (negative overflow) test case
    ldi r3, 1
    ldi r4, 7
    ldi r1, 32760
    ldi r2, -8
    ldi r0, 32767

    sub r3, r4
    subc r1, r2
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
    ldi r3, 1
    ldi r4, 7
    ldi r1, 65530
    ldi r2, -6
    ldi r0, 65535

    sub r3, r4
    subc r1, r2
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
    ldi r3, 1
    ldi r4, 7
    ldi r1, 0
    ldi r2, -1
    ldi r0, 0

    sub r3, r4
    subc r1, r2
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
    ldi r3, 1
    ldi r4, 7
    ldi r1, 0
    ldi r2, 5
    ldi r0, -6

    sub r3, r4
    subc r1, r2
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
    ldi r3, 1
    ldi r4, 7
    ldi r1, -1
    ldi r2, 1
    ldi r0, -3

    sub r3, r4
    subc r1, r2
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
    ldi r3, 1
    ldi r4, 7
    ldi r1, -32760
    ldi r2, 8
    ldi r0, 32767

    sub r3, r4
    subc r1, r2
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
