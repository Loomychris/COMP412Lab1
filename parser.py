from typing import List, Tuple
from intermediate import Intermediate

class Parser:
    
    def __init__(self, input: List[List[Tuple]], filename: str):
        self.input = input
        self.filename = filename
        self.head = None
        self.curr = None
        self.operations = 0
        self.errors = []
    
    def addIntermediate(self, newItem: Intermediate):
        if not self.head:
            self.head = newItem
            self.current = newItem
            newItem.next = None
            newItem.prev = None
        else: 
            self.current.next = newItem
            newItem.prev = self.current
            self.current = new newItem
    
    def processMemOp(self, line, position, lineNum):
        error = '' 
        extra = False
        if line[position][0] == 0:
            position += 1
            if line[position][0] == 6:
                position += 1
                if line[position][0] == 8:
                    position += 1 
                    if line[position][0] == 6:
                        position += 1
                        if line[position][0] == 10:
                            position += 1
                            inter = Intermediate(
                                line = lineNum,
                                opcode = line[position -5][1],
                                op1 = [line[position-4][1], -1, -1, -1],
                                op3 = [line[position-2][1], -1, -1, -1]
                            )
                            self.addIntermediate(inter)
                            self.operations += 1
                            return position
                        else:
                            error = 'ERROR %d: extra token at end of line "%s"' % (lineNum, line[position][1])
                            extra = True
                    else:
                        error = 'ERROR %d: missing target register in load or store' % (lineNum)
                else:
                    error = 'ERROR %d: missing \'=>\' in %s' % (lineNum)
            else:
                error = 'ERROR %d: missing source register in load or store' % (lineNum)
        if line[position][0] == 11:
            self.errors.append('ERROR %d: %s' % (lineNum, line[position][1]))
        elif len(error) > 0:
            self.errors.append(error)
        return -1
    
    def processArithOp(self, line, position, lineNum):
        error = ''
        extra = False
        if line[position][0] == 2:
            opcode = line[position][1]
            position += 1
            if line[position][0] == 6:
                position += 1
                if line[position][0] == 7:
                    position += 1 
                    if line[position][0] == 6:
                        position += 1
                        if line[position][0] == 8:
                            position += 1
                            if line[position][0] == 6:
                                position += 1
                                if line[position][0] == 10:
                                    position += 1
                                    inter = Intermediate(
                                        line = lineNum,
                                        opcode = opcode,
                                        op1 = [line[position-6][1], -1, -1, -1],
                                        op2 = [line[position-4][1], -1, -1, -1],
                                        op3 = [line[position-2][1], -1, -1, -1]
                                    )
                                    self.addIntermediate(inter)
                                    self.operations += 1
                                    return position
                                else:
                                    error = 'ERROR %d: extra token at end of line "%s"' % (lineNum, line[position][1])
                                    extra = True
                            else:
                                error = 'ERROR %d: missing target register in %s' % (lineNum, opcode)
                        else:
                            error = 'ERROR %d: missing \'=>\' in %s' % (lineNum, opcode)
                    else:
                        error = 'ERROR %d: missing second source register in %s' % (lineNum, opcode)
                else:
                    error = 'ERROR %d: missing comma in %s' % (lineNum, opcode)
            else:
                error = 'ERROR %d: missing first source register in %s' % (lineNum, opcode)
        if line[position][0] == 11:
            self.errors.append('ERROR %d %s' % (lineNum, line[position][1]))
        elif len(error) > 0:
            self.errors.append(error)
        return -1

    def processLoadI(self, line, position, lineNum):
        error = ''
        extra = False
        if line[position][0] == 1:
            position += 1
            if line[position][0] == 5:
                position += 1
                if line[position][0] == 8:
                    position += 1 
                    if line[position][0] == 6:
                        position += 1
                        if line[position][0] == 10:
                            position += 1
                            inter = Intermediate(
                                line = lineNum,
                                opcode = line[position -5][1],
                                op1 = [line[position-4][1], -1, -1, -1],
                                op3 = [line[position-2][1], -1, -1, -1]
                            )
                            self.addIntermediate(inter)
                            self.operations += 1
                            return position
                        else:
                            error = 'ERROR %d: extra token at end of line "%s"' % (lineNum, line[position][1])
                            extra = True
                    else:
                        error = 'ERROR %d: missing target register in loadI' % (lineNum)
                else:
                    error = 'ERROR %d: missing \'=>\' in loadI' % (lineNum)
            else:
                error = 'ERROR %d: missing constant in loadI' % (lineNum)
        if line[position][0] == 11:
            self.errors.append('ERROR %d: %s' % (lineNum, line[position][1]))
        elif len(error) > 0:
            self.errors.append(error)
        return -1
    
    def processNop(self, line, position, lineNum):
        