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
    # ========================= And tests =======================
    # Zero test case
    ldi r0, 0b1101
    ldi r1, 0
    ldi r2, 65535
    ldi r3, 0

    stps r0
    and r1, r2
    ldps r0
    add r0, 16
    push r0
    if
        cmp r2, r3
    is eq
        push 1
    else
        push 2
    fi

    # Negative test case
    ldi r0, 0b1110
    ldi r1, 32771
    ldi r2, 32773
    ldi r3, 32769

    stps r0
    and r1, r2
    ldps r0
    add r0, 16
    push r0
    if
        cmp r2, r3
    is eq
        push 1
    else
        push 2
    fi

    # Common test case
    ldi r0, 0b1111
    ldi r1, 0b0101
    ldi r2, 0b0011
    ldi r3, 0b0001

    stps r0
    and r1, r2
    ldps r0
    add r0, 16
    push r0
    if
        cmp r2, r3
    is eq
        push 1
    else
        push 2
    fi

    # ========================= Or tests =======================
    # Zero test case
    ldi r0, 0b1101
    ldi r1, 0
    ldi r2, 0
    ldi r3, 0

    stps r0
    or r1, r2
    ldps r0
    add r0, 16
    push r0
    if
        cmp r2, r3
    is eq
        push 1
    else
        push 2
    fi

    # Negative test case
    ldi r0, 0b1110
    ldi r1, 32771
    ldi r2, 32773
    ldi r3, 32775

    stps r0
    or r1, r2
    ldps r0
    add r0, 16
    push r0
    if
        cmp r2, r3
    is eq
        push 1
    else
        push 2
    fi

    # Common test case
    ldi r0, 0b1111
    ldi r1, 0b0101
    ldi r2, 0b0011
    ldi r3, 0b0111

    stps r0
    or r1, r2
    ldps r0
    add r0, 16
    push r0
    if
        cmp r2, r3
    is eq
        push 1
    else
        push 2
    fi

    # ========================= Xor tests =======================
    # Zero test case
    ldi r0, 0b1101
    ldi r1, 65535
    ldi r2, 65535
    ldi r3, 0

    stps r0
    xor r1, r2
    ldps r0
    add r0, 16
    push r0
    if
        cmp r2, r3
    is eq
        push 1
    else
        push 2
    fi

    # Negative test case
    ldi r0, 0b1110
    ldi r1, 32771
    ldi r2, 1
    ldi r3, 32770

    stps r0
    xor r1, r2
    ldps r0
    add r0, 16
    push r0
    if
        cmp r2, r3
    is eq
        push 1
    else
        push 2
    fi

    # Common test case
    ldi r0, 0b1111
    ldi r1, 0b0101
    ldi r2, 0b0011
    ldi r3, 0b0110

    stps r0
    xor r1, r2
    ldps r0
    add r0, 16
    push r0
    if
        cmp r2, r3
    is eq
        push 1
    else
        push 2
    fi

    # ========================= Not tests =======================
    # Zero test case
    ldi r0, 0b1101
    ldi r1, 65535
    ldi r3, 0

    stps r0
    not r1
    ldps r0
    add r0, 16
    push r0
    if
        cmp r1, r3
    is eq
        push 1
    else
        push 2
    fi

    # Negative test case
    ldi r0, 0b1110
    ldi r1, 0b1111
    ldi r3, 0xfff0

    stps r0
    not r1
    ldps r0
    add r0, 16
    push r0
    if
        cmp r1, r3
    is eq
        push 1
    else
        push 2
    fi

    # Common test case
    ldi r0, 0b1111
    ldi r1, 65530
    ldi r3, 0b0101

    stps r0
    not r1
    ldps r0
    add r0, 16
    push r0
    if
        cmp r1, r3
    is eq
        push 1
    else
        push 2
    fi

    # ========================= Bic tests =======================
    # Zero test case
    ldi r0, 0b1101
    ldi r1, 29715
    ldi r2, 65535
    ldi r3, 0

    stps r0
    bic r1, r2
    ldps r0
    add r0, 16
    push r0
    if
        cmp r2, r3
    is eq
        push 1
    else
        push 2
    fi

    # Negative test case
    ldi r0, 0b1110
    ldi r1, 32771
    ldi r2, 3
    ldi r3, 32768

    stps r0
    bic r1, r2
    ldps r0
    add r0, 16
    push r0
    if
        cmp r2, r3
    is eq
        push 1
    else
        push 2
    fi

    # Common test case
    ldi r0, 0b1111
    ldi r1, 0b0101
    ldi r2, 0b0011
    ldi r3, 0b0100

    stps r0
    bic r1, r2
    ldps r0
    add r0, 16
    push r0
    if
        cmp r2, r3
    is eq
        push 1
    else
        push 2
    fi

    halt

end.
