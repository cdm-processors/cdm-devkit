asect 0x00

start:
    setsp 0xf0

    ldsp r1
    ldsa r3, 0xf

    addsp -16
    ldsp r2

    ldi r0, 0xff
    st r0, r0

    halt

end.