asect 0x00
ldi r0, 1
jmp far_place
halt
halt
halt
halt

asect 0x1020
middle:
ldi r2, 3
halt
halt
halt


asect 0x1337
far_place:
ldi r1, 2
jmp middle
halt
end
