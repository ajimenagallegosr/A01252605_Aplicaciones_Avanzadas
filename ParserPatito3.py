import ply.yacc as yacc
from LexerPatito import tokens



def p_prueba(p):
    'prueba : body'
    print("biennn")

def p_type_int(p):
    'type : INT_TYPE'
    pass

def p_type_float(p):
    'type : FLOAT_TYPE'

def p_body(p):
    'body : LBRACES lista_statements RBRACES'
    print("body check!")
    pass

def p_lista_statements_vacio(p):
    'lista_statements : '
    pass

def p_lista_statements_statements(p):
    'lista_statements : statement lista_statements'
    pass

def p_statement_printfunc(p):
    'statement : print_func'
    print("✅ Entró a printfunc")
    pass

def p_statement_condition(p):
    'statement : condition'
    pass

def p_statement_cycle(p):
    'statement : cycle'
    pass

def p_statement_opcion(p):
    'statement : ID opcion_id'
    print(f"✅ Statement con ID: {p[1]}")
    pass

def p_print_func_placeholder(p):
    'print_func : PRINT LPARENTESIS elemento_impresion lista_elementos RPARENTESIS SEMICOLON'
    pass

def p_elemento_impresion_exp(p):
    'elemento_impresion : expresion'
    pass

def p_elemento_impresion_string(p):
    'elemento_impresion : CTE_STRING'
    pass

def p_lista_elementos_recursiva(p):
    'lista_elementos : COMMA elemento_impresion lista_elementos'
    pass

def p_lista_elementos_vacia(p):
    'lista_elementos : '
    pass

def p_expresion_placeholder(p):
    'expresion : '
    pass


def p_condition_placeholder(p):
    'condition : '
    pass

def p_cycle_placeholder(p):
    'cycle : '
    pass

def p_opcionid_fcall(p):
    'opcion_id : f_call'
    pass

def p_opcionid_assign(p):
    'opcion_id : assign'
    pass

def p_f_call_placeholder(p):
    'f_call : '
    pass

def p_assign_placeholder(p):
    'assign : '
    pass

def p_error(p):
    if p:
        print(f"❌ Error de sintaxis en '{p.value}' (línea {p.lineno})")
    else:
        print("❌ Error de sintaxis al final del archivo")

parser = yacc.yacc()