from ....cdm16.target_instructions import (
    Handler,
    op2
)

handlers = [
    Handler(op2, {'umul':12,'smul':13,'udiv':14, 'sdiv':15})
]
