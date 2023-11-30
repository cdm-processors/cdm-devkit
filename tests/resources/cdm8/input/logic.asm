asect 0x00

start:
    setsp 0xf0

    ldi r0, 0b101
    ldi r1, 0b010
    or r0, r1
    push r1

    ldi r0, 0b101
    ldi r1, 0b111
    and r0, r1
    push r1

    ldi r0, 0b111
    ldi r1, 0b001
    xor r0, r1
    push r1

    ldi r0, 0b101
    not r0
    push r0

    ldi r0, 0xff
    st r0, r0

    halt

end.