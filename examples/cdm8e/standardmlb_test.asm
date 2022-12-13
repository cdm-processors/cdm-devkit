# macros that work: tst, clr, shl, ldv, stv, ei, di
asect 0x00

ldi r0, 123
ldi r1, 66

ei


xor r0, r0

di 

xor r0, r0


halt
end