asect 0

start:
    nop
    br start
    nop
    br start
    nop
    br start
    nop
    br start

    ldi r0, 0xaabb
    nop
    nop

    if
        tst r0
    is nz
        dec r0
        add r0, 16
    else
        inc r0
        sub r1, 10
    fi

    int 90

    while
        tst r0
    stays nz
        dec r0
    wend

    halt

end.