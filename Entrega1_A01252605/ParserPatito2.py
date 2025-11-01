import ply.yacc as yacc
from LexerPatito import tokens


def p_program(p):
    'program : PROGRAM ID SEMICOLON declaraciones funciones MAIN body END'
    print("Programa válido")

def p_declaraciones(p):
    '''declaraciones : vars
                     | empty '''
    pass

def p_funciones(p):
    '''funciones : funcs funciones
                 | empty'''
    pass

def p_vars(p):
    'vars : VAR declaracion_var lista_declaraciones'
    pass

def p_declaracion_var(p):
    'declaracion_var : lista_identificadores COLON type SEMICOLON'
    print(f"Declaración de variable(s): {p[1]}")
    pass

def p_lista_identificadores(p):
    'lista_identificadores : ID lista_identificadores_prima'
    pass

def p_lista_identificadores_prima(p):
    '''lista_identificadores_prima : COMMA ID lista_identificadores_prima
                                    | empty'''
    pass

def p_lista_declaraciones(p):
    '''lista_declaraciones : declaracion_var lista_declaraciones
                           | empty'''
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

def p_lista_statements(p):
    '''lista_statements : statement lista_statements
                        | empty'''
    pass

def p_statement(p):
    '''statement : print_func
                 | condition
                 | cycle
                 | ID opcion_id'''
    pass

def p_opcion_id(p):
    '''opcion_id : f_call
                 | assign'''
    pass

def p_print_func(p):
    'print_func : PRINT LPARENTESIS elemento_impresion lista_elementos RPARENTESIS SEMICOLON'
    pass

def p_elemento_impresion(p):
    '''elemento_impresion : expresion
                          | CTE_STRING'''
    pass

def p_lista_elementos(p):
    '''lista_elementos : COMMA elemento_impresion lista_elementos
                       | empty'''
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

def p_part_else(p):
    '''part_else : ELSE body
                 | empty'''
    pass

def p_expresion(p):
    'expresion : exp comparacion'
    print("Expresión detectada")
    pass

def p_comparacion(p):
    '''comparacion : GREATER exp
                   | LESS exp
                   | DIFFERENT exp
                   | empty'''
    pass

def p_exp(p):
    'exp : termino suma_resta'
    pass

def p_suma_resta(p):
    '''suma_resta : PLUS termino suma_resta
                  | MINUS termino suma_resta
                  | empty'''
    pass

def p_termino(p):
    'termino : factor mult_div'
    pass

def p_mult_div(p):
    '''mult_div : TIMES factor mult_div
                | DIVIDE factor mult_div
                | empty'''
    pass

def p_factor(p):
    '''factor : agrupacion
              | signo_unario
              | valor'''
    pass

def p_agrupacion(p):
    'agrupacion : LPARENTESIS expresion RPARENTESIS'
    pass

def p_signo_unario(p):
    '''signo_unario : PLUS valor
                    | MINUS valor'''
    pass

def p_valor(p):
    '''valor : ID
             | cte'''
    pass

def p_cte(p):
    '''cte : CTE_INT
           | CTE_FLOAT'''
    pass

def p_funcs(p):
    'funcs : VOID ID LPARENTESIS parametros RPARENTESIS LBRACKETS bloque_funcion RBRACKETS SEMICOLON'
    print(f"Nombre de función detectada: {p[2]}")
    pass

def p_parametros(p):
    '''parametros : parametro lista_parametros
                  | empty'''
    pass

def p_parametro(p):
    'parametro : ID COLON type'
    pass

def p_lista_parametros(p):
    '''lista_parametros : COMMA parametro lista_parametros
                        | empty'''
    pass

def p_bloque_funcion(p):
    '''bloque_funcion : vars body
                      | body'''
    pass

def p_f_call(p):
    'f_call : LPARENTESIS argumentos RPARENTESIS SEMICOLON'
    print("F_CALL detectado")
    pass

def p_argumentos(p):
    '''argumentos : expresion lista_argumentos
                  | empty'''
    pass

def p_lista_argumentos(p):
    '''lista_argumentos : COMMA expresion lista_argumentos
                        | empty'''
    pass

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' (línea {p.lineno})")
    else:
        print("Error de sintaxis al final del archivo")

def p_empty(p):
    'empty :'
    pass

parser = yacc.yacc()