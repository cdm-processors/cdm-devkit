asect 0x00
ldi r1, 228
stv r1, 127

macro tes/0
xor r0, r0
xor r3, r3
mend

macro tes2/0

xor r1, r1
tes
xor r2, r2
mend


ldi r0, 1
ldi r1, 2
ldi r2, 3
ldi r3, 4

tes2
stv r1, 127
halt
end













