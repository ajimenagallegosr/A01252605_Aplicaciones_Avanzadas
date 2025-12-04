# Ana Jimena Gallegos
# a01252605
import ply.lex as lex

# palabras reservadas
reserved = {
    'program' : 'PROGRAM',
    'var' : 'VAR',
    'main' : 'MAIN',
    'end' : 'END',
    'void' : 'VOID',
    'while' : 'WHILE',
    'do' : 'DO',
    'if' : 'IF',
    'else' : 'ELSE',
    'print' : 'PRINT',
    'int': 'INT_TYPE',
    'float': 'FLOAT_TYPE',
    'return': 'RETURN'
}

#tokens sin regex
tokens = [
    'ID',
    'CTE_INT',
    'CTE_FLOAT',
    'CTE_STRING',
    'EQUALS',
    'STRICT_EQUAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'GREATER',
    'LESS',
    'DIFFERENT',
    'RPARENTESIS',
    'LPARENTESIS',
    'RBRACKETS',
    'LBRACKETS',
    'RBRACES',
    'LBRACES',
    'COLON',
    'SEMICOLON',
    'COMMA',
    'GREATER_EQUAL',
    'LESS_EQUAL',
] + list(reserved.values())

#Regex for simple tokens

t_EQUALS = r'\='
t_STRICT_EQUAL = r'\=='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_GREATER = r'>'
t_LESS = r'<'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='
t_DIFFERENT = r'!='
t_RPARENTESIS = r'\)'
t_LPARENTESIS = r'\('
t_RBRACKETS = r'\]'
t_LBRACKETS = r'\['
t_RBRACES = r'\}'
t_LBRACES = r'\{'
t_COLON = r':'
t_SEMICOLON = r';'
t_COMMA = r','

# Regex rule with some action code

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_CTE_FLOAT(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_CTE_INT(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_CTE_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

t_ignore = ' \t\r'

def t_comment(t):
    r'\/\/.*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en línea {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
