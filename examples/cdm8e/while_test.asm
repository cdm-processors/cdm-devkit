asect 0x00

ldi r0, 17
jsr func
halt



func:
# сумма четных чисел до r0, не больше 50
push r1
push r2
push r3

move r0, r3
xor r0, r0

while
tst r3
stays nz

    dec r3

    ldi r2, 50

    if 
    cmp r0, r2
    is gt
        break
    fi

    ldi r2, 1
    if
    and r3, r2
    tst r2
    is nz
        continue
    fi

    add r3, r0
    

wend


pop r3
pop r2
pop r1
rts




halt
end