import ply.yacc as yacc
from LexerPatito import tokens

def p_program(p):
    'program : PROGRAM ID SEMICOLON declaraciones funciones MAIN body END'
    print("✅ Programa válido")

def p_declaraciones_vars(p):
    'declaraciones : vars'
    pass

def p_declaraciones_vacias(p):
    'declaraciones : '
    pass

def p_funciones_recursivo(p):
    'funciones : func funciones'
    pass

def p_funciones_vacias(p):
    'funciones : '
    pass

def p_func_placeholder(p):
    'func : '
    pass

def p_vars_placeholder(p):
    'vars : '
    pass




def p_body(p):
    'body : LBRACES estatutos RBRACES'
    pass

def p_estatutos_vacios(p):
    'estatutos : '
    pass




def p_error(p):
    if p:
        print(f"❌ Error de sintaxis en '{p.value}' (línea {p.lineno})")
    else:
        print("❌ Error de sintaxis al final del archivo")

parser = yacc.yacc()