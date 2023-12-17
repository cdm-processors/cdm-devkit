asect 0x00

start:
    setsp 0xf0

    ldi r0, 0xab
    ldi r1, 0x55
    st r0, r1
    ld r0, r3

    ldi r0, number
    ldc r0, r1

    ldi r2, 0xdc

    ldi r0, 0xff
    st r0, r0

    halt

asect 0xf0
number:
    dc 0xbb

end.