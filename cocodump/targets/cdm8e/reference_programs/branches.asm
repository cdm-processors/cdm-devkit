asect 0

label_2:
    ldi r0, 15

    bhs 0x40

    crc

    goto vs, label

    ldi r0, 25

    jmp 0xab00

    add r0, r1

    br label_2

asect 0xff00

    ldi r0, 15

label:
    xor r3, r3

    ldi r3, 25

end.