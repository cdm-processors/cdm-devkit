asect 0x00

start:
    setsp 0xf0

    jsr func

    ldi r0, computed_func
    jsrr r0

    ioi

    ldi r0, 0xff
    st r0, r0

    halt

func:
    ldi r1, 0xab
    rts

computed_func:
    ldi r2, 0xcd
    rts

handler:
    ldi r3, 0xef
    rti

asect 0xf0
    dc handler, 0

end.