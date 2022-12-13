asect 0x00
jsr first




asect 0x1234
first:
jsr second
inc r1
crc
inc r1
crc
inc r1
crc
inc r1
crc
inc r1
crc
inc r1
crc
inc r1
crc
halt




asect 0x5678
second:
inc r2
crc
inc r2
crc
inc r2
crc
inc r2
crc
inc r2
crc
inc r2
crc
halt


end