from scanner import Scanner
from parser import Parser
import time

table = ['MEMOP', 'LOADI', 'ARITHOP', 'OUTPUT', 'NOP', 'CONST', 'REG', 'COMMA', 'INTO', 'ENDFILE', 'NEWLINE']

start = time.time()
scan = Scanner("T128k.i")

result = scan.parse()
print(f'scanner elapsed: {time.time() - start}')
start = time.time()
parse = Parser(result, "T128k.i")
parse.parse()
print(f'parse elapsed: {time.time() - start}')