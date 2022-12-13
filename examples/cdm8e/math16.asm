rsect math

# to implement:
# add16 ok
# neg16 ok
# sub16 ok
# mul8
# div18
# mul16
# div16

# TODO: rsect and separate file

# r0, r1 - addresses of operands
# r2 - address of result
add16>
minus_one: ext
ten: ext


pushall
    push r2         # no we can pop return address

    ld r0, r2
    inc r0
    ld r0, r3       # r2, r3 now contain first operand


    ld r1, r0
    inc r1
    ld r1, r1       # r0, r1 now contain fecond operand

    add r0, r2      # r2 = low(answer)
    addc r1, r3     # r3 = high(answer)

    pop r0          # r0 = result address

    st r0, r2
    inc r0
    st r0, r3

popall
rts


# r0 - source
# r1 - destination
neg16>
pushall

    ld r0, r2
    inc r0
    ld r0, r3

    not r2
    not r3

    push r1

    ldi r0, 0
    ldi r1, 1

    add r1, r2
    add r0, r3

    pop r1

    st r1, r2
    inc r1
    st r1, r3

popall
rts


# r0, r1 - addresses of operands
# r2 - address of result
sub16>
pushall
    addsp -sub16._

    move r0, r3  # op1
    move r1, r0  # op2
    ldsa r1, sub16.tmp


    jsr neg16

    move r3, r0
    ldsa r1, sub16.tmp


    jsr add16

    addsp sub16._

popall
rts


# r0 - source
# r1 - dest
copy16>
pushall

    ld r0, r2
    st r1, r2

    inc r0
    inc r1

    ld r0, r2
    st r1, r2

popall
rts


# r0 - input address
# r0 - sign bit (output)
# works in place
abs16>
push r1
push r2
    inc r0
    ld r0, r1
    if
        tst r1
    is mi
        dec r0
        move r0, r1

        jsr neg16

        ldi r0, 1

    else
        ldi r0, 0

    fi

pop r2
pop r1
rts



# r0 address of input
# r0 - 0 if null, 1 else
is_not_null16>
push r1
    ld r0, r1

    if
        tst r1
    is nz
        ldi r0, 1

    else
        inc r0
        ld r0, r1
        if
            tst r1
        is nz
            ldi r0, 1
        else
            ldi r0, 0
        fi
    fi

pop r1
rts





# r0, r1 - addresses of operands
# r2 - address of result
mul16>
pushall
    addsp -mul16._

    
    ldsa r3, mul16.return_addr
    st r3, r2

    # move r0, r2
    move r1, r3
    ldsa r1, mul16.op1

    jsr copy16

    move r3, r0
    ldsa r1, mul16.op2
    jsr copy16


    # now we must get rid of signs
    # and save result's sign bit
    xor r3, r3
    ldsa r0, mul16.op1
    jsr abs16

    xor r0, r3

    ldsa r0, mul16.op2
    jsr abs16

    xor r0, r3

    ldsa r0, mul16.sign
    st r0, r3


    # now we must initialize acc
    ldsa r0, mul16.acc
    ldi r3, 0
    st r0, r3
    inc r0
    st r0, r3
    dec r0


    while
        ldsa r0, mul16.op2
        jsr is_not_null16
        tst r0
    stays nz

        ldsa r0, mul16.op1
        ldsa r1, mul16.acc
        move r1, r2
        jsr add16

        ldsa r0, mul16.op2
        ldi r1, low(minus_one)
        move r0, r2
        jsr add16

    wend

    if
        ldsa r0, mul16.sign
        ld r0, r0
        tst r0
    is nz
        ldsa r0, mul16.acc
        move r0, r1
        jsr neg16

    fi

    ldsa r1, mul16.return_addr
    ld r1, r1
    ldsa r0, mul16.acc

    jsr copy16

    addsp mul16._

popall
rts

# r0 - address of number to shift
# works in-place
shl16>
pushall

    ld r0, r2 # low
    inc r0
    ld r0, r3 # hight
    dec r0

    move r0, r0 # clear carry
    shl r2
    shl r3

    st r0, r2
    inc r0
    st r0, r3
popall
rts


# r0 - first num
# r1 - second number
# r0 - one if greater or equals
greater_or_equals_16>
push r1
push r2
push r3

    addsp -2

    ldsa r2, 0
    jsr sub16

    inc r2

    if
        ld r2, r2
        tst r2
    is mi
        ldi r0, low(0)
    else
        ldi r0, low(1)
    fi


    addsp 2


pop r3
pop r2
pop r1
rts


# r0, r1 - addresses of operands
# r2 - address of result (and remainder after it)
div16>
pushall
    addsp -div16._
    
    ldsa r3, div16.return_addr
    st r3, r2

    # move r0, r2
    move r1, r3
    ldsa r1, div16.n

    jsr copy16

    move r3, r0
    ldsa r1, div16.d
    jsr copy16


    # now we must get rid of signs
    # and save result's sign bit

    xor r3, r3
    ldsa r0, div16.n
    jsr abs16

    xor r0, r3

    ldsa r0, div16.d
    jsr abs16

    xor r0, r3

    ldsa r0, div16.sign
    st r0, r3


    # now we must initialize acc
    # q = 0
    ldsa r0, div16.q
    ldi r3, 0
    st r0, r3
    inc r0
    st r0, r3
    
    # r = 0
    ldsa r0, div16.r
    ldi r3, 0
    st r0, r3
    inc r0
    st r0, r3

    xor r3, r3

    while
        ldi r0, 16
        cmp r3, r0
    stays lt
        inc r3

        # r = r << 1
        ldsa r0, div16.r
        jsr shl16

        # r(0) = n(15), then n = n << 1
        if
            ldsa r0, div16.n
            inc r0
            ld r0, r0 # high byte 
            ldi r1, 0b10000000
            and r1, r0
            tst r0
        is nz
            ldsa r0, div16.r
            ld r0, r1
            ldi r2, 1
            or r2, r1
            st r0, r1
        fi

        ldsa r0, div16.n 
        jsr shl16


        ldsa r0, div16.q
        jsr shl16

        if
            ldsa r0, div16.r
            ldsa r1, div16.d
            jsr greater_or_equals_16
            tst r0

        is nz
            # r = r - d
            ldsa r0, div16.r
            ldsa r1, div16.d
            move r0, r2
            jsr sub16

            # q(15)
            ldsa r0, div16.q
            ld r0, r1
            ldi r2, low(1)
            or r2, r1
            st r0, r1

        fi
    wend

    


    if
        ldsa r0, div16.sign
        ld r0, r0
        tst r0
    is nz
        ldsa r0, div16.q
        move r0, r1
        jsr neg16

    fi

    ldsa r1, div16.return_addr
    ld r1, r1
    ldsa r0, div16.q

    jsr copy16

    ldsa r1, div16.return_addr
    ld r1, r1
    inc r1
    inc r1
    ldsa r0, div16.r

    jsr copy16
    


    addsp div16._
popall
rts


# r0 - addres of number to print
print16>
pushall
    addsp -print16._

    ldsa r1, print16.quot

    jsr copy16

    move r1, r0
    jsr abs16

    ldsa r1, print16.sign
    st r1, r0

    ldsa r3, print16.str_end

    dec r3
    xor r0, r0

    st r3, r0

    do
        ldsa r0, print16.quot
        ldi r1, low(ten)

        move r0, r2

        jsr div16

        ldsa r0, print16.rem
        ld r0, r0
        ldi r1, "0"
        add r1, r0

        st r3, r0

        dec r3

        ldsa r0, print16.quot
        jsr is_not_null16
        tst r0



    until z

    if
        ldsa r0, print16.sign
        ld r0, r0
        tst r0

    is nz
        ldi r0, "-"
        st r3, r0

    else
        inc r3
    fi

    move r3, r0
    jsr print

    addsp print16._
popall
rts


# r0 - address of zero-terminated string
print>
push r0
push r1
push r2
    ldi r2, 0
    while
        ld r0, r1
        tst r1
    stays nz
        st r2, r1
        inc r0
    wend
pop r2
pop r1
pop r0
rts


# r0 - destination address
read16>
pushall
    addsp -read16._

    ldsa r2, read16.return_addr
    st r2, r0

    xor r1, r1

    ldsa r0, read16.digit
    st r0, r1
    inc r0
    st r0, r1

    ldsa r0, read16.num
    st r0, r1
    inc r0
    st r0, r1

    while
        xor r0, r0
        ld r0, r0
        ldi r1, low(0x0a)
        cmp r0, r1
    stays ne

        if
            tst r0
        is z
            continue
        fi

        xor r1, r1
        st r1, r0

        ldi r1, "0"
        sub r0, r1

        ldsa r0, read16.digit
        st r0, r1

        ldsa r0, read16.num
        ldi r1, low(ten)
        move r0, r2

        jsr mul16

        ldsa r1, read16.digit
        jsr add16

    wend

    ldsa r0, read16.num
    ldsa r1, read16.return_addr
    ld r1, r1
    jsr copy16

    xor r0, r0
    ldi r1, low(0x0a)

    st r0, r1

    addsp read16._
popall
rts


tplate mul16
rem: ds 2
sign: ds 1
acc: ds 2
op1: ds 2
op2: ds 2
return_addr: ds 1
rem_addr: ds 1

tplate div16
sign: ds 1
n: ds 2
d: ds 2
q: ds 2
r: ds 2
return_addr: ds 1

tplate sub16
tmp: ds 2


tplate print16
# max lenght is 5 (65535) + 1 (-) + 1 (null terminator) = 7
str: ds 7
str_end:
quot: ds 2
rem: ds 2
sign: ds 1


tplate read16
digit: ds 2
num: ds 2
return_addr: ds 1


end