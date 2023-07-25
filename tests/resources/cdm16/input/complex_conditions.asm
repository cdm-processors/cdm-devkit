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

ldi r0, 15

if
    tst r0
is lt, and
    tst r0
is lt, or
    tst r0
is gt, and
    tst r0
is gt
    push 1 #
else
    push 2
fi


if
    tst r0
is lt, and
    tst r0
is gt, and
    tst r0
is lt, and
    tst r0
is gt
    push 1
else
    push 2 #
fi


if
    tst r0
is lt, and
    tst r0
is lt, or
    tst r0
is gt
    push 1 #
else
    push 2
fi


if
    tst r0
is gt, and
    tst r0
is gt, and
    tst r0
is gt, and
    tst r0
is lt
    push 1
else
    push 2 #
fi


if
    tst r0
is lt, or
    tst r0
is lt, and
    tst r0
is gt, and
    tst r0
is gt
    push 1
else
    push 2 #
fi

halt
end
