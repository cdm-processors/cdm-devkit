code = """
asect  0x00

if
    ldi r1, 3
    ldi r2, 3
    cmp r1, r2
is hs
    ldi r0, 1
else
    ldi r0, 2
fi


halt
end

"""

r0 = 1