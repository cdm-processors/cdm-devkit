asect 0x00
goto true, long_goto_test
start:
ldi r0, 0x01
push r0
ldi r0, 0x00
push r0
ldi r0, 0b10000000
push r0
rti

# here we can place some constants
how_dare_you:
dc "How dare you interrupt me", 0x0a, 0x00
calculating:
dc "Calculating r0 fib number", 0x0a, 0x00
done:
dc "Done, your answer in r0", 0x0a, 0x00
first_vec:
dc "First vector", 0x0a, 0x00



# assemnle should be able to push to bytes label onto stack
# or at least define macro to enable interrupts
asect 0x0100
ldi r0, low(calculating)
jsr print

ldi r0, 8
jsr fib

push r0
ldi r0, low(done)
jsr print
pop r0

halt

print:
push r0
push r1
push r2
ldi r2, 0
loop:
ldc r0, r1
tst r1
goto z, printend
st r2, r1
inc r0

goto true, loop
printend:
pop r2
pop r1
pop r0
rts


fib:
push r3
ldi r3, 2
cmp r0, r3
goto lt, fibend

dec r0
push r0
jsr fib
move r0, r3
pop r0

dec r0
push r0
jsr fib
add r0, r3
pop r0
move r3, r0


fibend:
pop r3
rts


asect 0xf1ff
zero_vect_handler:
push r0
ldi r0, low(first_vec)
jsr print
pop r0
rti

asect 120
# this is here to test debug codegen
long_goto_test:
goto true, start


asect 0xf2fe
first_vect_handler:
push r0
ldi r0, low(how_dare_you)
jsr print
pop r0
rti


asect 0xffe0
# pcl, pch, ps
#first vector
dc low(0xff), low(0xf1), low(0x00)
ds 1
# scond vector
dc low(0xfe), low(0xf2), low(0x00)
ds 1

end