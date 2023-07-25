asect 0x00
ldi r1, 1
ldi r2, 2
save r2
inc r2
save r1
ldi r1, 8
restore
restore r1
halt
end