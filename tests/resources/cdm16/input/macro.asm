asect 0
main: ext               # Declare labels
default_handler: ext    # as external

# Interrupt vector table (IVT)
# Place a vector to program start and
# map all internal exceptions to default_handler
dc main, 0x0000         # Startup/Reset vector
dc default_handler, 0   # Unaligned SP
dc default_handler, 0   # Unaligned PC
dc default_handler, 0   # Invalid instruction
dc default_handler, 0   # Division by zero
dc 0, 0                 # Reserved
dc default_handler, 0   # Interrupt fault
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
    ldi r0, 15
    ldi r1, 16

    if
        cmp r0, r1
    is gt
        ldi r2, 1
    else
        ldi r2, 2
    fi

    if
        cmp r0, r1
    is lt
        ldi r3, 1
    else
        ldi r3, 2
    fi

    ldi r0, 0

    if
        tst r0
    is z
        ldi r0, 4
    fi

    ldi r7, 15

    while
        tst r7
    stays nz
        dec r7
        inc r4
    wend

    ldi r7, 14

    do
        dec r7
        inc r5

        tst r7
    until z

    halt

end.
