import ply.yacc as yacc
from LexerPatito import tokens



def p_prueba(p):
    'prueba : body'
    print("biennn")

def p_type_int(p):
    'type : INT_TYPE'
    print("type int detectado")
    pass

def p_type_float(p):
    'type : FLOAT_TYPE'
    print("type float detectado")
    pass

def p_body(p):
    'body : LBRACES lista_statements RBRACES'
    print("body check!")
    pass

def p_lista_statements_vacio(p):
    'lista_statements : '
    print("statements vacio")
    pass

def p_lista_statements_statements(p):
    'lista_statements : statement lista_statements'
    print("statements ")
    pass

def p_statement_printfunc(p):
    'statement : print_func'
    print("✅ Entró a printfunc")
    pass

def p_statement_condition(p):
    'statement : condition'
    print("entro a un if")
    pass

def p_statement_cycle(p):
    'statement : cycle'
    print("entro a un while")
    pass

def p_statement_opcion(p):
    'statement : ID opcion_id'
    print(f"✅ Statement con ID: {p[1]}")
    pass

def p_opcionid_fcall(p):
    'opcion_id : f_call'
    print("📞 Opción ID → FCALL")
    pass

def p_opcionid_assign(p):
    'opcion_id : assign'
    print("✍️ Opción ID → ASSIGN")
    pass

def p_print_func_placeholder(p):
    'print_func : PRINT LPARENTESIS elemento_impresion lista_elementos RPARENTESIS SEMICOLON'
    print("🖨️ PRINTFUNC ejecutada")
    pass

def p_elemento_impresion_exp(p):
    'elemento_impresion : expresion'
    print("✨ Elemento de impresión: EXPRESIÓN")
    pass

def p_elemento_impresion_string(p):
    'elemento_impresion : CTE_STRING'
    print(f"✨ Elemento de impresión: STRING '{p[1]}'")
    pass

def p_lista_elementos_recursiva(p):
    'lista_elementos : COMMA elemento_impresion lista_elementos'
    print("➕ Elemento adicional en PRINT (coma)")
    pass

def p_lista_elementos_vacia(p):
    'lista_elementos : '
    print("🪫 Lista de elementos de impresión vacía")
    pass

def p_assign(p):
    'assign : expresion SEMICOLON'
    print("📝 Asignación detectada (sin operador)")
    pass

def p_cycle(p):
    'cycle : WHILE LPARENTESIS expresion RPARENTESIS DO body SEMICOLON'
    print("🔁 WHILE loop detectado")
    pass

def p_condition(p):
    'condition : IF LPARENTESIS expresion RPARENTESIS body part_else'
    print("IF condición detectada")
    pass

def p_part_else_body(p):
    'part_else : ELSE body'
    print("➕ ELSE detectado")
    pass

def p_part_else_vacia(p):
    'part_else : '
    print("🪫 ELSE vacío")
    pass

def p_expresion(p):
    'expresion : exp comparacion'
    pass

def p_comparacion_mayor(p):
    'comparacion : GREATER exp'
    pass

def p_comparacion_menor(p):
    'comparacion : LESS exp'
    pass

def p_comparacion_diferente(p):
    'comparacion : DIFFERENT exp'
    pass

def p_comparacion_vacia(p):
    'comparacion : '
    pass


def p_exp_placeholder(p):
    'exp : '
    print(f"🧮 EXPRESIÓN detectada (ID): {p[1]}")
    pass

def p_f_call_placeholder(p):
    'f_call : '
    print("📞 FCALL placeholder")
    pass

def p_error(p):
    if p:
        print(f"❌ Error de sintaxis en '{p.value}' (línea {p.lineno})")
    else:
        print("❌ Error de sintaxis al final del archivo")

parser = yacc.yacc()