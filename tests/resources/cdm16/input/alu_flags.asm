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
    if
        ldi r1, 15
        ldi r2, 16
        ldi r0, 31

        add r2, r1
        pups
        cmp r0, r1
    is eq
        push 1
    else
        push 0
    fi
    # Zero test case
    if
        ldi r1, 15
        ldi r2, -15
        ldi r0, 0

        add r2, r1
        pups
        cmp r0, r1
    is eq
        push 1
    else
        push 0
    fi
    # Negative (Overflow) test case
    if
        ldi r1, 117
        ldi r2, 65
        ldi r0, 182

        add r2, r1
        pups
        cmp r0, r1
    is eq
        push 1
    else
        push 0
    fi

    # ========================= Sub tests =======================

    stps r0
    and r2, r1
    # check for zeros

    halt

end.
