import ply.yacc as yacc
from LexerPatito import tokens
import semantic as semantic
        
def reduce_oper(op):
    prec = {'+': 2, '-': 2, '*': 3, '/': 3, '<': 1, '>': 1, '!=': 1, '==': 1}
    print(op)

    while semantic.PilaOper and semantic.PilaOper[-1] != '(' and prec.get(semantic.PilaOper[-1], 0) >= prec.get(op, 0):
        temp_op = semantic.PilaOper.pop()
        right = semantic.PilaO.pop()
        left = semantic.PilaO.pop()
        temp = semantic.new_temp()
        semantic.generate_quad(temp_op, left, right, temp)
        print("gen 1")
        semantic.PilaO.append(temp)
    
    if op == ')':
        while semantic.PilaOper and semantic.PilaOper[-1] != '(':
            temp_op = semantic.PilaOper.pop()
            right = semantic.PilaO.pop()
            left = semantic.PilaO.pop()
            temp = semantic.new_temp()
            semantic.generate_quad(temp_op, left, right, temp)
            print("gen 1")
            semantic.PilaO.append(temp)
        semantic.PilaOper.pop()
        return
    
    semantic.PilaOper.append(op)

def p_program(p):
    'program : PROGRAM create_dirfunc ID create_id SEMICOLON declaraciones funciones MAIN body END clean_program'
    print("Programa válido")

def p_clean_program(p):
    'clean_program :'
    print("Paso 6 (Final), Eliminando DirFunc y tabla global")
    semantic.print_quads()

    # comentados por test
    #semantic2.func_dir = None
    #semantic2.current_function = None

def p_create_dirfunc(p):
    'create_dirfunc :'
    semantic.func_dir = semantic.FunctionDirectory()
    semantic.current_function = None
    print("Paso 1, Directorio de funciones creado")

def p_create_id(p):
    'create_id :'
    program_name = p[-1]
    semantic.func_dir.add_function(program_name, 'program')
    semantic.current_function = program_name
    print(f"Paso 2, Nombre de programa registrado: '{program_name}'")

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
    tipo = semantic.current_type
    lista = p[1]

    for ident in lista:
        semantic.func_dir.add_var(semantic.current_function, ident, tipo)
        print(f"Paso 5, Variable agregada: {ident} ({tipo}) en {semantic.current_function} Var Table")
    pass

def p_lista_identificadores(p):
    'lista_identificadores : ID lista_identificadores_prima'
    if p[2] is None:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]
    
    print(f"Paso 3, Variable detectada '{p[0]}'")

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
    semantic.current_type = p[1]
    p[0] = p[1]

    print(f"Paso 4/11, Tipo de variable(s) '{p[0]}'")
    pass

def p_body(p):
    'body : LBRACES lista_statements RBRACES'
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
    right = semantic.PilaO.pop()
    left = p[-1]
    semantic.generate_quad('=', right, None, left)


def p_cycle(p):
    'cycle : WHILE LPARENTESIS expresion RPARENTESIS DO body SEMICOLON'
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
    while semantic.PilaOper and semantic.PilaOper[-1] != '(':
        temp_op = semantic.PilaOper.pop()
        right = semantic.PilaO.pop()
        left = semantic.PilaO.pop()
        temp = semantic.new_temp()
        semantic.generate_quad(temp_op, left, right, temp)
        print("gen 2")
        semantic.PilaO.append(temp)


def p_comparacion(p):
    '''comparacion : GREATER add_op exp
                   | LESS add_op exp
                   | DIFFERENT add_op exp
                   | STRICT_EQUAL add_op exp
                   | empty'''
    pass

def p_exp(p):
    'exp : termino suma_resta'
    pass

def p_suma_resta(p):
    '''suma_resta : PLUS add_op termino suma_resta
                  | MINUS add_op termino suma_resta
                  | empty'''
    pass

def p_termino(p):
    'termino : factor mult_div'
    pass

def p_mult_div(p):
    '''mult_div : TIMES add_op factor mult_div
                | DIVIDE add_op factor mult_div
                | empty'''
    pass


def p_factor(p):
    '''factor : agrupacion
              | signo_unario
              | cte
              | ID id_opcion'''
    if len(p) == 3 and p.slice[1].type == 'ID':
        print(p[1])
        semantic.PilaO.append(p[1])
    elif len(p) == 2 and isinstance(p[1], (int, float, str)):
        semantic.PilaO.append(p[1])
        print(p[1])


def p_id_opcion(p):
    '''id_opcion : f_call
                 | empty'''
    pass

def p_agrupacion(p):
    'agrupacion : LPARENTESIS push_paren expresion RPARENTESIS close_paren'
    pass

def p_push_paren(p):
    'push_paren :'
    semantic.PilaOper.append('(')
    print("push (")

def p_close_paren(p):
    'close_paren :'
    reduce_oper(')')
    print("pop )")


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
    # Convierte el valor del token a tipo numérico real
    if p.slice[1].type == 'CTE_INT':
        val = int(p[1])
    else:
        val = float(p[1])
    p[0] = val
    pass


def p_funcs(p):
    'funcs : prepare_new_func funcs_type add_current_type ID add_function LPARENTESIS start_func_vars parametros RPARENTESIS LBRACES bloque_funcion RBRACES end_func SEMICOLON'

def p_prepare_new_func(p):
    'prepare_new_func :'
    semantic.current_type = None
    semantic.current_function = None
    print("Paso 7, Preparando para nueva función")

def p_funcs_type(p):
    '''funcs_type : VOID
                  | type'''
    p[0] = p[1]

def p_add_current_type(p):
    'add_current_type :'
    semantic.current_type = p[-1]
    print(f"Paso 8, Tipo de funcion detectada '{p[-1]}")

def p_add_function(p):
    'add_function :'
    func_name = p[-1]
    func_type = semantic.current_type

    print(f"Paso 9, Registrado '{func_name}' con '{func_type}'")
    semantic.func_dir.add_function(func_name, func_type)

    semantic.current_function = func_name

def p_start_func_vars(p):
    'start_func_vars :'
    semantic.func_dir.directory[semantic.current_function]['vars'] = semantic.VarTable()
    print(f"Paso 10: VarTable creada para función '{semantic.current_function}'")

def p_parametros(p):
    '''parametros : parametro lista_parametros
                  | empty'''
    
    pass

def p_parametro(p):
    'parametro : ID COLON type'
    param_name = p[1]
    param_type = p[3]

    semantic.func_dir.add_var(semantic.current_function, param_name, param_type)
    
    print(f"Paso 11: Parámetro agregado '{param_name}' tipo '{param_type}' a función '{semantic.current_function}'")

    pass

def p_lista_parametros(p):
    '''lista_parametros : COMMA parametro lista_parametros
                        | empty'''
    pass

def p_bloque_funcion(p):
    '''bloque_funcion : vars body
                      | body'''
    pass

def p_end_func(p):
    'end_func :'
    print(f"Paso 12: Eliminando VarTable de función '{semantic.current_function}'")
    #comentados en los test
    #semantic2.func_dir.directory[semantic2.current_function]['vars'] = None
    #semantic2.current_function = None


def p_f_call(p):
    'f_call : LPARENTESIS argumentos RPARENTESIS'
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

# para los cuadraticos
def p_add_op(p):
    'add_op :'
    op = p[-1]
    reduce_oper(op)

parser = yacc.yacc()