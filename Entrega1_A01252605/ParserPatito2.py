import ply.yacc as yacc
from LexerPatito import tokens
import semantic2


def p_program(p):
    'program : PROGRAM create_dirfunc ID create_id SEMICOLON declaraciones funciones MAIN body END'
    print("Programa válido")

def p_create_dirfunc(p):
    'create_dirfunc :'
    semantic2.func_dir = semantic2.FunctionDirectory()
    semantic2.current_function = None
    print("Directorio de funciones creado")

def p_create_id(p):
    'create_id :'
    program_name = p[-1]
    semantic2.func_dir.add_function(program_name, 'program')
    semantic2.current_function = program_name
    print(f"Nombre de programa registrado: {program_name}")

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
    tipo = semantic2.current_type
    lista = p[1]

    for ident in lista:
        if semantic2.func_dir.var_exists(semantic2.current_function, ident):
            raise Exception(f"ERROR: Multiple declaration of variable '{ident}' in '{semantic2.current_function}")
        semantic2.func_dir.add_var(semantic2.current_function, ident, tipo)
        print(f"Variable declarada: {ident} ({tipo}) en {semantic2.current_function}")
    pass

def p_lista_identificadores(p):
    'lista_identificadores : ID lista_identificadores_prima'
    if p[2] is None:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

    pass

def p_lista_identificadores_prima(p):
    '''lista_identificadores_prima : COMMA ID lista_identificadores_prima
                                    | empty'''
    if len(p) == 4:
        if p[3] is None:
            p[0] = [p[2]]
        else:
            p[0] = [p[2]] + p[3]

    else: 
        p[0] = None
    pass

def p_lista_declaraciones(p):
    '''lista_declaraciones : declaracion_var lista_declaraciones
                           | empty'''
    pass

def p_type(p):
    '''type : INT_TYPE
            | FLOAT_TYPE'''
    semantic2.current_type = p[1]
    p[0] = p[1]
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
                 | ID opcion_id
                 | LBRACKETS lista_statements RBRACKETS'''
    pass

def p_opcion_id(p):
    '''opcion_id : f_call SEMICOLON
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
    'condition : IF LPARENTESIS expresion RPARENTESIS body part_else SEMICOLON'
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
                   | STRICT_EQUAL exp
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
              | cte
              | ID id_opcion'''
    pass

def p_id_opcion(p):
    '''id_opcion : f_call
                 | empty'''
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
    'funcs : prepare_new_func funcs_type add_current_type ID add_function LPARENTESIS parametros RPARENTESIS LBRACES bloque_funcion RBRACES SEMICOLON'
    print(f"Func detectada: {p[3]}")

def p_prepare_new_func(p):
    'prepare_new_func :'
    semantic2.current_type = None
    semantic2.current_function = None
    print("Paso 7: preparando para nueva función")

def p_funcs_type(p):
    '''funcs_type : VOID
                  | type'''
    p[0] = p[1]

def p_add_current_type(p):
    'add_current_type :'
    semantic2.current_type = p[-1]

def p_add_function(p):
    'add_function :'
    func_name = p[-1]
    func_type = semantic2.current_type

    print("registrando '{func_name}' con '{func_type}'")
    semantic2.func_dir.add_function(func_name, func_type)

    semantic2.current_function = func_name



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
    'f_call : LPARENTESIS argumentos RPARENTESIS'
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