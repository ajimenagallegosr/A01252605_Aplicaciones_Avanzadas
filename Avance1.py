# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
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

#regex for simple tokens

t_equal = r'\='
t_plus = r'\+'
t_minus = r'-'
t_times = r'\*'
t_divide = r'/'
t_greater =
t_less =
t_different =
t_rparentesis =
t_lparentesis =
t_rbrackets =
t_lbrackets = 
t_colon =
t_semicolon =
t_comma = 

