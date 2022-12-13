asect 0x00
start: ext
jmp start



rsect test
start>
push r0
push r1
push r2
    ldi r2, 0
    print_loop:
    ld r0, r1
    tst r1
    goto z, printend
    st r2, r1
    inc r0

    goto true, print_loop
    printend:
pop r2
pop r1
pop r0
rts

halt

end