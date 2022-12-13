_mem_addr = 15

# TODO: logisim sets carry flag on decrease for unknown reason
code = """
asect 0x00
ldi r0, """ + str(_mem_addr) + """
ldi r1, 4
st r0, r1
inc r0
inc r1
st r0, r1
inc r0
dec r1
st r0, r1
ld r0, r0
halt 
end
"""

r0 = 4
mem = {
    _mem_addr: [4, 5, 4]
}

