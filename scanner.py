from typing import List, Tuple

class Scanner:
    line = ''

    def __init__(self, input):
        self.input = input
    
    def s(self, line, position, tokens, length) -> int:
        s = 's'
        position += 1
        if position < length and line[position] == 't':
            position += 1
            s += 't'
            if position < length and line[position] == 'o':
                position += 1
                s += 'o'
                if position < length and line[position] == 'e':
                    s += 'e'
                    tokens.append((0, 'store'))
                    return position + 1
        elif position < length and line[position] == 'u':
            position += 1
            s += 'u'
            if position < length and line[position] == 'b':
                s += 'b'
                tokens.append((2, 'sub'))
                return position + 1
        self.error = True
        if position < length:
            s += line[position]
        tokens.append((11, '\'%s\' is not a vaid word' % (s)))
        return length -1
    
    def l(self, line, position, tokens, length) -> int:
        s = 'l'
        position += 1
        if position < length and line[position] == 'o':
            s += 'o'
            position += 1
            if position < length and line[position] == 'a':
                s += 'a'
                position += 1
                if position < length and line[position] == 'd':
                    s += 'd'
                    position += 1
                    if position < length and line[position] == 'I':
                        s += 'I'
                        tokens.append((1, 'loadI'))
                        return position + 1
                    else:
                        tokens.append((0, 'load'))
                        return position
        elif position < length and line[position] == 's':
            s += 's'
            position += 1
            if position < length and line[position] == 'h':
                s += 'h'
                position += 1
                if position < length and line[position] == 'i':
                    s += 'i'
                    position += 1
                    if position < length and line[position] == 'f':
                        s += 'f'
                        position += 1
                        if position < length and line[position] == 't':
                            s += 't'
                            tokens.append((2, 'lshift'))
                            return position + 1
        self.error = True
        if position < length:
            s += line[position]
        tokens.append((11, '\'%s\' is not a valid word' % (s)))
        return length -1
    
    def r(self, line, position, tokens, length) -> int:
        s = 'r'
        position += 1
        if position < length and line[position] == '0' and line[position] <= '9':
                while position < length and line[position] >= '0' and line[position] <= '9':
                    s += line[position]
                    position += 1
                tokens.append((6, s))
                return position
        elif position < length and line[position] == 's':
            s += 's'
            position += 1
            if position < length and line[position] == 'h':
                s += 'h'
                position += 1
                if position < length and line[position] == 'i':
                    s += 'i'
                    position += 1
                    if position < length and line[position] == 'f':
                        s += 'f'
                        position += 1
                        if position < length and line[position] == 't':
                            s += 't'
                            tokens.append((2, 'rshift'))
                            return position + 1
        self.error = True
        if position < length:
            s += line[position]
        tokens.append((11, '\'%s\' is not a vaid word' % (s)))
        return length -1
    
    def m(self, line, position, tokens, length) -> int:
        s = 'm'
        position += 1
        if position < length and line[position] == 'u':
            s += 'u'
            position += 1
            if position < length and line[position] == 'l':
                s += 'l'
                position += 1
                if position < length and line[position] = 't':
                    s += 't'
                    tokens.append((2, 'mult'))
                    return position + 1
        self.error = True
        if position < length:
            s += line[position]
        tokens.append((11, '\'%s\' is not a vaid word' % (s)))
        return length -1
    
    def a(self, line, position, tokens, length) -> int:
        s = 'a'
        position += 1
        if position < length and line[position] == 'd':
            s += 'd'
            position += 1
            if position < length and line[position] == 'd':
                s += 'd'
                tokens.append((2, 'add'))
                return position + 1
        self.error = True
        if position < length:
            s += line[position]
        tokens.append((11, '\'%s\' is not a vaid word' % (s)))
        return length -1
    
    def n(self, line, position, tokens, length) -> int:
        s = 'n'
        position += 1
        if position < length and line[position] == 'o':
            s += 'd'
            position += 1
            if position < length and line[position] == 'p':
                s += 'p'
                tokens.append((4, 'nop'))
                return position + 1
        self.error = True
        if position < length:
            s += line[position]
        tokens.append((11, '\'%s\' is not a vaid word' % (s)))
        return length -1
    
    def o(self, line, position, tokens, length) -> int:
        s = 'o'
        position += 1
        if position < length and line[position] == 'u':
            s += 'u'
            position += 1
            if position < length and line[position] == 't':
                s += 't'
                position += 1
                if position < length and line[position] == 'p':
                    s += 'p'
                    position += 1
                    if position < length and line[position] == 'u':
                        s += 'u'
                        position += 1
                        if position < length and line[position] == 't':
                            s += 't'
                            tokens.append((3, 'output'))
                            return position + 1
        self.error = True
        if position < length:
            s += line[position]
        tokens.append((11, '\'%s\' is not a vaid word' % (s)))
        return length -1
    
    def into(self, line, position, tokens, length) -> int:
        s = '='
        position += 1
        if position < length and line[position] == '>':
            s += '>'
            tokens.append((8, '=>'))
            return position + 1
        self.error = True
        if position < length:
            s += line[position]
        tokens.append((11, '\'%s\' is not a vaid word' % (s)))
        return length -1

    def comma(self, line, position, tokens, length) -> int:
        if line[position] == ',':
            tokens.append((7, ','))
            return position + 1
        self.error = True
        if position < length:
            s += line[position]
        tokens.append((11, '\'%s\' is not a vaid word' % (s)))
        return length -1

    def newline(self, line, position, tokens, length) -> int:
        if line[position] == '\n':
            tokens.append((10, '\n'))
            return position + 1
        self.error = True
        if position < length:
            s += line[position]
        tokens.append((11, '\'%s\' is not a vaid word' % (s)))
        return length -1
    
    def comment(self, line, position, tokens, length) -> int:
        s = '/'
        position += 1
        if position < length and line[position] == '/':
            s += '/'
            return length - 1
        self.error = True
        if position < length:
            s += line[position]
        tokens.append((11, '\'%s\' is not a vaid word' % (s)))
        return length - 1
    
    def constant(self, line, position, tokens, length) -> int:
        num = 0
        while position < length and line[position] >= '0' and line[position] <= '9':
            i = ord(line[position]) - ord('0')
            position += 1
            num = num * 10 + i
        tokens.append((5, str(num)))
        return position
    
    def parse(self) -> List[List[Tuple]]:
        result = []
        inputfile = open(self.input, 'r')
        tokens = []
        while True:
            line = inputfile.readline()
            if not line:
                break
            length = len(line)
            self.error = False
            tokens = []
            position = 0 
            op = False
            comment = False
            while position < length:
                if position == length - 1:
                    if line[position] == '\n':
                        tokens.append((10, '\n'))
                        break
                    if comment:
                        break
                if op and not self.error:
                    op = False
                    if line[position] == ' ' or line[position] == '\t':
                        position += 1
                    else:
                        tokens.append((11, 'no space after op'))
                        position = length - 1
                    continue
                if self.error:
                    if line[position] == '\n':
                        position = self.newline(line, position, tokens, length)
                    break
                if line[position] == ' ' or line[position] == '\t':
                    position += 1
                    continue
                elif line[position] == 's':
                    position = self.s(line, position, tokens, length)
                    op = True
                elif line[position] == 'l':
                    position = self.(line, position, tokens, length)
                    op = True
                elif line[position] == 'r':
                    position = self.r(line, position, tokens, length)
                elif line[position] == 'm':
                    position = self.m(line, position, tokens, length)
                    op = True
                elif line[position] == 'a':
                    position = self.a(line, position, tokens, length)
                    op = True
                elif line[position] == 'n':
                    position = self.n(line, position, tokens, length)
                elif line[position] == 'o':
                    position = self.o(line, position, tokens, length)
                    op = True
                elif line[position] == '=':
                    position = self.into(line, position, tokens, length)
                elif line[position] == ',':
                    position = self.comma(line, position, tokens, length)
                elif line[position] == '\n':
                    tokens.append((10, '\n'))
                    break
                elif line[position] == '/':
                    position = self.comment(line, position, tokens, length)
                    comment = True
                elif line[position] <= '9' and line[position] >= '0':
                    position = self.constant(line, position, tokens, length)
                else:
                    if position == length - 1:
                        if comment:
                            break
                        else:
                            tokens.append((11, '\'%s\' is not a valid word' % (line[position])))
                            position += 1
                    else: 
                        tokens.append((11, '\'%s\' is not a valid word' % (line[position])))
                        position = length - 1
                result.append(tokens)
            if len(tokens) == 0 or tokens[-1][0] != 10:
                tokens.append((10, '\n'))
            result.append([(9, '')])
            return result
