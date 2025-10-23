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
    'print' : 'PRINT'
}

#tokens sin regex
tokens = [
    'ID',
    'CTE_INT',
    'CTE_FLOAT',
    'CTE_STRING',
    'EQUALS',
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
    'COMMA'
] + list(reserved.values())

#Regex for simple tokens

t_equal = r'\='
t_plus = r'\+'
t_minus = r'-'
t_times = r'\*'
t_divide = r'/'
t_greater = r'<'
t_less = r'>'
t_different = r'!='
t_rparentesis = r'\)'
t_lparentesis = r'\()'
t_rbrackets = r'\]'
t_lbrackets = r'\[]'
t_colon = r':'
t_semicolon = r';'
t_comma = r','

# Regex rule with some action code

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'\"\.*?\"'
    t.value = t.value[1:-1]
    return t
