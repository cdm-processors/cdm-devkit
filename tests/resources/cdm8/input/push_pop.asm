asect 0x00

start:
    setsp 0xf0

    ldi r0, 1
    ldi r1, 2
    ldi r2, 3
    ldi r3, 4

    pushall
    popall
    pushall

    ldi r0, 0xaa
    push r0
    pop r1
    push r1

    ldi r0, 0xff
    st r0, r0

    halt

end.