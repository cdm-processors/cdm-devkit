asect 0x00
jmp start

data_start:
first_op: ds 2
second_op: ds 2
result: ds 4
minus_one> dc low(-1), high(-1)
one> dc low(1), high(1)
ten> dc low(10), high(10)

str_op1: dc "Enter operand 1: ", 0
str_op2: dc "Enter operand 2: ", 0
str_op: dc "[+-/=] ", 0
str_result: dc "Result is ", 0

data_end:


asect 0x100
print: ext
read16: ext
add16: ext
print16: ext


start:
jsr fill_ram



# start 
ldi r0, low(str_op1)
jsr print
ldsa r0, low(first_op)
jsr read16


ldi r0, low(str_op2)
jsr print
ldsa r0, low(second_op)
jsr read16


ldi r0, low(first_op)
ldi r1, low(second_op)
ldi r2, low(result)
jsr add16

ldi r0, low(str_result)
jsr print

ldi r0, low(result)
jsr print16



halt

# copies half of first page of ROM to RAM
fill_ram:
pushall
    ldi r0, low(data_start)
    ldi r3, low(data_end)
    do
        ldc r0, r1
        st r0, r1
        inc r0

        cmp r0, r3
    until eq

popall
rts







end




# WYSI