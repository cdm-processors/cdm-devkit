asect 0x00

start:
    setsp 0xf0

    ldi r0, 15
    ldi r1, 17

    while
        cmp r0, r1
    stays lt
        inc r0
    wend

    push r0

    ldi r0, 15
    ldi r1, 0

    do
        inc r1
        dec r0
    until z

    push r1

    ldi r3, 0xff

    if
        tst r3
    is nz
        push r3
    fi

    ldi r0, 0xff
    st r0, r0

    halt

end.