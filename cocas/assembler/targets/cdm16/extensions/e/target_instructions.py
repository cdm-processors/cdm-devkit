from ....cdm16.target_instructions import (
    Handler,
    op1,
    op2
)

handlers = [
    Handler(op1, {'ldssp': 14, 'stssp': 15}),
    Handler(op2, {'swpw': 2, 'swpb': 3})
]
