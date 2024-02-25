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

# Templates
tplate foo
a: ds 7
b: dc "abcd"
c: db 10
d: dw 20
e: ds 984
f: dc 30


# Main program section
rsect main
main>
ldi r0, foo.a
ldi r1, foo.b
ldi r2, foo.c
ldi r3, foo.d
ldi r4, foo.e
ldi r5, foo.f
ldi r6, foo._

end