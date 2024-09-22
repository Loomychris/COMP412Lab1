from typing import List

class Intermediate:
    def __init__(self, next = None, prev = None, line: int = 0, opcode: str = '', op1: List = None, op2: List = None, op3: List = None):
        self.next = next
        self.prev = prev
        self.line = line
        self.opcode = opcode
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
    
    def __str__(self):
        formatter = ['','','']
        if self.opcode == 'load' or self.opcode == 'store':
            formatter[0] = formatter[2] = 's'
        elif self.opcode == 'loadI':
            formatter[0] = 'val'
            formatter[2] = 's'
        elif self.opcode == 'add' or self.opcode == 'sub' or self.opcode == 'mult' or self.opcode == 'lshift' or self.opcode == 'rshift':
            formatter[0] = formatter[1] = formatter[2] = 's'
        elif self.opcode == 'output':
            formatter[0] = 'val '
        
        s0 = s1 = s2 = ''
        if self.op1:
            s0 = self.op1[0]
        if self.op2:
            s1 = self.op2[0]
        if self.op3:
            s2 = self.op3[0]
        return f'{self.line:2}: {self.opcode:6} [ {formatter[0]  + s0} ], [ {formatter[1]  + s1} ], [ {formatter[2]  + s2} ]'

