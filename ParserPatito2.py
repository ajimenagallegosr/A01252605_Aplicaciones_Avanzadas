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

def p_vars(p):
    'vars : VAR declaracion_var lista_declaraciones'
    pass

def p_declaracion_var(p):
    'declaracion_var : lista_identificadores COLON type SEMICOLON'
    pass

def p_lista_identificadores_mult(p):
    'lista_identificadores: ID COMMA lista_identificadores'
    pass

def p_lista_identificadores_ind(p):
    'lista_identificadores : ID'
    pass

def p_lista_declaraciones_nula(p):
    'lista_declaraciones : '
    pass

def p_lista_declaraciones(p):
    'lista_declaraciones : declaracion_var lista_declaraciones'
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