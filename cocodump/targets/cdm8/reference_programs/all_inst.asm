asect 0

    move r1, r2
    add r2, r3
    addc r2, r1
    sub r0, r1

label:
    and r0, r2
    or r2, r3
    xor r3, r0
    cmp r2, r3

    not r0
    neg r1
    dec r2
    inc r3

    shr r0
    shla r1
    shra r2
    rol r3

    st r0, r1
    ld r2, r3

    push r0
    pop r1

    ldsa r3, 115

    addsp 101
    setsp 87

    pushall
    popall

    ldi r2, 135

    halt
    wait
    jsr label
    rts
    ioi
    rti
    crc
    osix 15

    br label

    ldc r2, r3


end.