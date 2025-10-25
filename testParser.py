# test_parser.py
from ParserPatito3 import parser

codigo = '''
{
print("Hola");
print(x, "mundo");
variable
print("final");
}
'''

parser.parse(codigo)


