asect 0

    dw 0
    halt
    wait
    ei
    di
    jsr 0xff00
    rti
    pupc
    popc
    pusp
    posp
    pups
    pops

    push r1
    pop r2
    ldi r3, 0xaabb
    jsrr r4
    ldsp r5
    stsp r6
    ldps fp
    stps r0
    ldpc r1
    stpc r2
    addsp r3

    move r4, r5

    ldw r1, r2
    ldb r2, r3
    ldsb r3, r4
    lcw r1, r2
    lcb r2, r3
    lcsb r3, r4
    stw r5, r6
    stb r6, fp

    lsw r1, 16
    lsw r2, -16
    lsb r3, 17
    lsb r4, -17
    lssb r5, 18
    lssb r6, -19
    ssw fp, 10
    ssw r1, -12
    ssb r2, 12
    ssb r3, -13
    ldi r1, 5
    ldi r2, -5
    add r3, 15
    sub r3, 15
    cmp r5, 10
    cmp fp, -15

    int 15
    reset 2
    push 15
    push -17
    addsp 16
    addsp -18

    jsr jsr_label
    nop
jsr_label:
    jsr jsr_label

    ldw r1, r1, r2
    ldb r2, r2, r3
    ldsb r3, r3, r4
    lcw r1, r1, r2
    lcb r2, r2, r3
    lcsb r3, r3, r4
    stw r5, r5, r6
    stb r6, r6, fp

    br 0xff00

    shl r1
    shr r1, 2
    shra r2, r3, 3
    rol r3, r4, 4
    ror r4, r5, 5
    rcl r3, r4, 4
    rcr r4, r5, 5

    neg r0
    not r1, r2
    sxt r2, r3
    scl r3, r4

    bit r3, r2
    cmp r5, r4

    and r0, r1
    or r1, r2, r3
    xor r1, r2, r3
    bic r1, r2, r3
    add r1, r2, r3
    addc r1, r2, r3
    sub r1, r2, r3
    subc r1, r2, r3

    br br_label
    nop
br_label:
    br br_label

end.
