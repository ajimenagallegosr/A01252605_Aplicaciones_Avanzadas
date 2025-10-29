import ply.yacc as yacc
from LexerPatito import tokens


def p_program(p):
    'program : PROGRAM ID SEMICOLON declaraciones funciones MAIN body END'
    print("Programa válido")

def p_declaraciones_vars(p):
    'declaraciones : vars'
    pass

def p_declaraciones_vacias(p):
    'declaraciones : '
    pass

def p_funciones_recursivo(p):
    'funciones : funcs funciones'
    pass

def p_funciones_vacias(p):
    'funciones : '
    pass

def p_vars(p):
    'vars : VAR declaracion_var lista_declaraciones'
    pass

def p_declaracion_var(p):
    'declaracion_var : lista_identificadores COLON type SEMICOLON'
    print(f"Declaración de variable(s): {p[1]}")
    pass

def p_lista_identificadores_mult(p):
    'lista_identificadores : ID COMMA lista_identificadores'
    p[0] = [p[1]] + p[3]
    pass

def p_lista_identificadores_ind(p):
    'lista_identificadores : ID'
    p[0] = [p[1]]
    pass

def p_lista_declaraciones(p):
    'lista_declaraciones : declaracion_var lista_declaraciones'
    pass

def p_lista_declaraciones_vacia(p):
    'lista_declaraciones : '
    pass

def p_type_int(p):
    'type : INT_TYPE'
    print("Tipo detectado: INT")
    pass

def p_type_float(p):
    'type : FLOAT_TYPE'
    print("Tipo detectado: FLOAT")
    pass

def p_body(p):
    'body : LBRACES lista_statements RBRACES'
    print("body detectado")
    pass

def p_lista_statements_vacio(p):
    'lista_statements : '
    pass

def p_lista_statements_statements(p):
    'lista_statements : statement lista_statements'
    pass

def p_statement_printfunc(p):
    'statement : print_func'
    print("Statement: PRINT")
    pass

def p_statement_condition(p):
    'statement : condition'
    pass

def p_statement_cycle(p):
    'statement : cycle'
    pass

def p_statement_opcion(p):
    'statement : ID opcion_id'
    print(f"Statement con ID: {p[1]}")
    pass

def p_opcionid_fcall(p):
    'opcion_id : f_call'
    pass

def p_opcionid_assign(p):
    'opcion_id : assign'
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

def p_assign(p):
    'assign : EQUALS expresion SEMICOLON'
    print("Asignación detectada")
    pass

def p_cycle(p):
    'cycle : WHILE LPARENTESIS expresion RPARENTESIS DO body SEMICOLON'
    print("WHILE detectado")
    pass

def p_condition(p):
    'condition : IF LPARENTESIS expresion RPARENTESIS body part_else'
    pass

def p_part_else_body(p):
    'part_else : ELSE body'
    print("IF & ELSE detectado")
    pass

def p_part_else_vacia(p):
    'part_else : '
    print("IF detectado")
    pass

def p_expresion(p):
    'expresion : exp comparacion'
    print("Expresión detectada")
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

def p_exp(p):
    'exp : termino suma_resta'
    pass

def p_suma_resta_suma(p):
    'suma_resta : PLUS termino suma_resta'
    pass

def p_suma_resta_resta(p):
    'suma_resta : MINUS termino suma_resta'
    pass

def p_suma_resta_vacia(p):
    'suma_resta : '
    pass

def p_termino(p):
    'termino : factor mult_div'
    pass

def p_mult_div_mult(p):
    'mult_div : TIMES factor mult_div'
    pass

def p_mult_div_div(p):
    'mult_div : DIVIDE factor mult_div'
    pass

def p_mult_div_vacio(p):
    'mult_div : '
    pass

def p_factor_agrupacion(p):
    'factor : agrupacion'
    pass

def p_factor_signo(p):
    'factor : signo_unario'
    pass

def p_factor_valor(p):
    'factor : valor'
    pass

def p_agrupacion(p):
    'agrupacion : LPARENTESIS expresion RPARENTESIS'
    pass

def p_signo_unario_suma(p):
    'signo_unario : PLUS valor'
    pass

def p_signo_unario_resta(p):
    'signo_unario : MINUS valor'
    pass

def p_valor_id(p):
    'valor : ID'
    pass

def p_valor_cte(p):
    'valor : cte'
    pass

def p_cte_int(p):
    'cte : CTE_INT'
    pass

def p_cte_float(p):
    'cte : CTE_FLOAT'
    pass

def p_funcs(p):
    'funcs : VOID ID LPARENTESIS parametros RPARENTESIS LBRACKETS bloque_funcion RBRACKETS SEMICOLON'
    print(f"Nombre de función detectada: {p[2]}")
    pass

def p_parametros_recursivo(p):
    'parametros : parametro lista_parametros'
    pass

def p_parametros_vacio(p):
    'parametros : '
    pass

def p_parametro(p):
    'parametro : ID COLON type'
    pass

def p_lista_parametros_recursivo(p):
    'lista_parametros : COMMA parametro lista_parametros'
    pass

def p_lista_parametros_vacia(p):
    'lista_parametros : '
    pass

def p_bloque_funcion_variables(p):
    'bloque_funcion : vars body'
    pass

def p_bloque_funcion_body(p):
    'bloque_funcion : body'
    pass

def p_f_call(p):
    'f_call : LPARENTESIS argumentos RPARENTESIS SEMICOLON'
    print("F_CALL detectado")
    pass

def p_argumentos_lista(p):
    'argumentos : expresion lista_argumentos'
    pass

def p_argumentos_vacia(p):
    'argumentos : '
    pass

def p_lista_argumentos_lista(p):
    'lista_argumentos : COMMA expresion lista_argumentos'
    pass

def p_lista_argumentos_vacia(p):
    'lista_argumentos : '
    pass

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' (línea {p.lineno})")
    else:
        print("Error de sintaxis al final del archivo")

parser = yacc.yacc()