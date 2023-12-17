asect 0x00

start:
    setsp 0xf0

    # test code here

    ldi r0, 0xff
    st r0, r0

    halt

end.