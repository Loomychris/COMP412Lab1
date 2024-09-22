import sys
from scanner import Scanner
from parser import Parser

table = ['MEMOP', 'LOADI', 'ARITHOP', 'OUTPUT', 'NOP', 'CONST', 'REG', 'COMMA', 'INTO', 'ENDFILE', 'NEWLINE']
one_flag = False
too_many = False
h = False
r = False
p = False
s = False
filename = ''
for arg in sys.argv:
    if arg == '-r':
        r = True
        if one_flag:
            too_many = True
        else: 
            one_flag = True
    elif arg == '-h':
        h = True
        if one_flag:
            too_many = True
        else:
            one_flag = True
        break
    elif arg == '-p':
        if one_flag:
            too_many = True
        else:
            one_flag = True
    elif arg == 's':
        s = True
        if one_flag:
            too_many = True
        else:
            one_flag = True
    elif arg[-2:] == '.i':
        filename = arg
if too_many:
    print("Too many command line flags!\n Try '-h for information on command-line syntax", file = sys.stderr)
if len(sys.argv) == 0:
   print("Input should be formatted as follows:\n" + 
         "412fe –h : help flag\n" +
         "412fe -s <name> : reads file <name> and prints list of tokens from scanner\n"
         "412fe -p <name> : reads file <name> and reports success or fail, and prints errors if needed\n"
         "412fe -r <name> : reads file <name> and prints intermediate format\n"
   )
   exit(1)
if not s and not p and not r and not h:
   p = True
if len(filename) == 0 and not h:
   print("ERROR: Invalid Filename (needs to be a .i file)!", file = sys.stderr)
   exit(1)
if h:
   print("Input should be formatted as follows:\n" + 
         "412fe –h : help flag\n" +
         "412fe -s <name> : reads file <name> and prints list of tokens from scanner\n"
         "412fe -p <name> : reads file <name> and reports success or fail, and prints errors if needed\n"
         "412fe -r <name> : reads file <name> and prints intermediate format\n"
   )
   exit(0)
elif r:
   scanner = Scanner(filename)
   result = scanner.parse()
   parser = Parser(result, filename)
   if parser.parse()== 0:
      head = parser.head
      while head:
         print(head)
         head = head.next
   else:
      for er in parser.errors:
         print(er)
      print('\nDue to syntax errors, run terminates.') 
   exit(0)
elif p:
   scanner = Scanner(filename)
   result = scanner.parse()
   parser = Parser(result, filename)
   if parser.parse()== 0:
      print(f"Parse Succeeded, finding {parser.operations} ILOC operations")
   else:
      errs = 0
      for er in parser.errors:
         errs += 1
         print(er)
      print(f'\nanthony_lab1 found {errs} errors in {filename}')
   exit(0)
elif s:
   scanner = Scanner(filename)
   result = scanner.parse()
   line = 1
   for lst in result:
      for token in lst:
         if token[0] == 11:
            print(f'ERROR {line}: {token[1]}')
         else:
            if token[1] == '\n':
               print(f'{line}: < {table[token[0]]}, "\\n" >')
            else:
               print(f'{line}: < {table[token[0]]}, "{token[1]}" >')
      line += 1
   exit(0)
else:
   print("Input should be formatted as follows:\n" + 
         "412fe –h : help flag\n" +
         "412fe -s <name> : reads file <name> and prints list of tokens from scanner\n"
         "412fe -p <name> : reads file <name> and reports success or fail, and prints errors if needed\n"
         "412fe -r <name> : reads file <name> and prints intermediate format\n"
   )
   exit(1)