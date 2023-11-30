asect 0x00

start:
    setsp 0xf0

    ldi r0, 4
    ldi r1, 6
    add r0, r1
    push r1

    ldi r0, 255
    ldi r1, 5
    add r0, r1
    ldi r0, 4
    ldi r1, 6
    addc r0, r1
    push r1

    ldi r0, 6
    ldi r1, 4
    sub r0, r1
    push r1

    ldi r0, 0xee
    move r0, r3
    push r3

    ldi r0, 15
    neg r0
    push r0

    ldi r0, 20
    inc r0
    push r0
    dec r0
    push r0

    ldi r0, 0b10
    shra r0
    push r0
    shla r0
    push r0

    ldi r0, 0xff
    shra r0
    push r0

    # ldi r0, 0x80  # In this CdM-8 implementation 
    # rol r0        # rol is replaced with swan
    # push r0       # idk what to do now

    ldi r0, 20
    dec r0          # Set C
    ldi r0, 0b10
    shr r0
    push r0

    ldi r0, 0x80
    rol r0
    push r0

    ldi r0, 0xff
    st r0, r0

    halt

end.