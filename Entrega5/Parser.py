import ply.yacc as yacc
from Lexer import tokens
import Semantic as semantic
import Memory as memory
import json

def clean_quad():
    operator = semantic.PilaOper.pop()
    right = semantic.PilaO.pop()
    left = semantic.PilaO.pop()
    right_type = semantic.PilaT.pop()
    left_type = semantic.PilaT.pop()

    result_type = semantic.semantic_cube[operator].get((left_type, right_type))

    if result_type is None:
        raise TypeError(f"Semantic error can apply {operator} to {left_type} and {right_type}")
    
    temp = semantic.new_temp()

    if result_type == 'int':
        memory.allocate("TempInt", temp)
    elif result_type == 'float':
        memory.allocate("TempFloat", temp)
    else:
        memory.allocate("TempBool", temp)

    semantic.generate_quad(operator, left, right, temp)
    semantic.PilaO.append(temp)
    semantic.PilaT.append(result_type)

def procces_quad(op):
    prec = {'+': 2, '-': 2, '*': 3, '/': 3, '<': 1, '>': 1, '!=': 1, '==': 1}

    while semantic.PilaOper and semantic.PilaOper[-1] and prec.get(semantic.PilaOper[-1], 0) >= prec.get(op, 0):
        clean_quad()

    semantic.PilaOper.append(op)

def p_program(p):
    'program : PROGRAM create_dirfunc ID create_id SEMICOLON declarations functions MAIN add_main_quad body END clean_program'
    print("Programa válido")

def p_add_main_quad(p):
    'add_main_quad :'
    main_d = len(semantic.QuadList)
    semantic.QuadList[0][3] = main_d
    semantic.QuadListMemory[0][3] = main_d
    pass

def p_create_dirfunc(p):
    'create_dirfunc :'
    semantic.func_dir = semantic.FunctionDirectory()
    semantic.current_function = None
    print("Step 1: Global function directory created")

def p_create_id(p):
    'create_id :'
    program_name = p[-1]
    semantic.func_dir.add_function(program_name, 'program', None, [])
    semantic.current_function = program_name
    print(f"Step 2, Program '{program_name}' name registered")

def p_clean_program(p):
    'clean_program :'
    print("Step 5 (Final), Delete global table")
    semantic.print_quads()
    print(memory.ConstantInt)

    output = {
        "quadruples": semantic.QuadListMemory,
        "constants": {
            "int": memory.ConstantInt,
            "float": memory.ConstantFloat,
            "string": memory.ConstantString
        }
    }

    with open("output.json", "w") as f:
        json.dump(output, f, indent=4)

    print("Archivo output.json generado")
    
    # comentados por test
    #semantic.func_dir = None
    #semantic.current_function = None

def p_declarations(p):
    '''declarations : vars
                    | empty '''
    pass

def p_functions(p):
    '''functions : funcs functions
                 | empty'''
    pass

def p_vars(p):
    'vars : VAR var_declaration var_declaration_list'
    pass

def p_var_declaration(p):
    'var_declaration : identifier_list COLON type SEMICOLON'
    pass

def p_identifier_list(p):
    'identifier_list : ID add_to_var_table identifier_list_tail'
    pass

def p_identifier_list_tail(p):
    '''identifier_list_tail : COMMA ID add_to_var_table identifier_list_tail
                            | empty'''
    pass

def p_add_to_var_table(p):
    '''add_to_var_table : '''
    variable = p[-1]
    print("Step 3, variable detected", variable)
    semantic.temp_ids.append(variable)

def p_var_declaration_list(p):
    '''var_declaration_list : var_declaration var_declaration_list
                           | empty'''
    pass

def p_type(p):
    '''type : INT_TYPE current_type
            | FLOAT_TYPE current_type'''
    p[0] = p[1]
    pass

def p_current_type(p):
    'current_type :'
    if p[-1] not in ['int', 'float']:
        raise SyntaxError(f"Tipo inválido '{p[-1]}'")
    tipo = p[-1]
    semantic.current_type = tipo
    print(f"Step 4, Variables with type '{semantic.current_type}'")
    print("Step 4, adding variables to var table")
    while semantic.temp_ids:
        semantic.func_dir.add_var(semantic.current_function, semantic.temp_ids.pop(0), tipo) #se agrega la de las dirreciones
    pass

def p_body(p):
    'body : LBRACES statement_list RBRACES'
    pass

def p_statement_list(p):
    '''statement_list : statement statement_list
                      | empty'''
    pass

def p_statement(p):
    '''statement : print_func
                 | condition
                 | cycle
                 | RETURN expression SEMICOLON make_return
                 | ID id_option
                 | LBRACKETS statement_list RBRACKETS'''
    pass

"""def p_make_return(p):
    'make_return :'
    
    ret_type = semantic.func_dir.directory[semantic.current_function]['type']
    if ret_type != 'void':
        temp = semantic.new_temp()

        # reservar memoria
        if ret_type == 'int':
            memory.allocate("TempInt", temp)
        elif ret_type == 'float':
            memory.allocate("TempFloat", temp)
        else:
            memory.allocate("TempBool", temp)

        semantic.QuadList.append(['Return', None, None, temp])
        semantic.QuadListMemory.append(['Return', None, None, temp])

        semantic.PilaO.append(temp)
        semantic.PilaT.append(ret_type)
    pass"""

def p_make_return(p):
    'make_return :'
    ret_type = semantic.func_dir.directory[semantic.current_function]['type']
    value = semantic.PilaO.pop()
    value_type = semantic.PilaT.pop()

    if ret_type != value_type:
        raise TypeError(f"Return type {value_type} does not match function type {ret_type}")

    # si quieres guardar en un temp especial, si no, puedes usar value directo
    semantic.QuadList.append(['Return', value, None, None])
    semantic.QuadListMemory.append(['Return', semantic.func_dir.get_address(semantic.current_function, value), None, None])


def p_id_option(p):
    '''id_option : f_call SEMICOLON
                 | assign'''
    pass

def p_print_func(p):
    'print_func : PRINT LPARENTESIS print_element print_element_list RPARENTESIS SEMICOLON'
    pass

def p_print_element_expr(p):
    'print_element : expression' #Quads print Int or Float or Variable
    value_print = semantic.PilaO.pop()
    semantic.PilaT.pop()
    semantic.generate_quad('PRINT', None, None, value_print)
    pass

def p_print_element_str(p):
    'print_element : CTE_STRING'
    value_print = p[1]
    semantic.generate_quad('PRINT', None, None, value_print)
    pass


def p_print_element_list(p):
    '''print_element_list : COMMA print_element print_element_list
                          | empty'''
    pass

def p_assign(p):
    'assign : EQUALS expression SEMICOLON generate_assign_quad'
    pass

def p_generate_assign_quad(p): # Make the ASSIGN 
    'generate_assign_quad :'
    target = p[-4]
    source = semantic.PilaO.pop()
    
    source_type = semantic.PilaT.pop()
    target_type = semantic.func_dir.get_var_type(semantic.current_function, target)

    result_type = semantic.semantic_cube['='].get((target_type, source_type), "error")
    
    if result_type == "error" or result_type is None:
        raise TypeError(f"Syntax error can't assign {source_type} to {target_type} in '{target}'")

    semantic.generate_quad('=', source, None, target )

def p_cycle(p):
    'cycle : WHILE add_while LPARENTESIS expression RPARENTESIS add_while_false DO body SEMICOLON add_while_final_s'
    pass

# Semantic for while
def p_add_while(p):
    'add_while :'
    step_add = len(semantic.QuadList)
    semantic.PilaGoTo.append(step_add)
    pass

def p_add_while_false(p):
    'add_while_false :'
    step_add = len(semantic.QuadList)
    semantic.PilaGoTo.append(step_add)
    goTo = semantic.PilaO.pop()
    semantic.generate_quad("GOTOF", goTo, None, None)

def p_add_while_final_s(p):
    'add_while_final_s :'
    edit_goTo = semantic.PilaGoTo.pop()
    goTo = semantic.PilaGoTo.pop()

    semantic.generate_quad("GOTO", None, None, None)

    semantic.QuadList[len(semantic.QuadList) - 1][3] = goTo
    semantic.QuadListMemory[len(semantic.QuadList) - 1][3] = goTo

    semantic.QuadList[edit_goTo][3] = len(semantic.QuadList)
    semantic.QuadListMemory[edit_goTo][3] = len(semantic.QuadList)


def p_condition(p):
    'condition : IF LPARENTESIS expression RPARENTESIS add_if body else_part SEMICOLON add_endif'
    pass

def p_else_part(p):
    '''else_part : add_else ELSE body
                 | empty'''
    pass

# Semantic for if - else
def p_add_if(p):
    'add_if :'
    step_add = len(semantic.QuadList)
    semantic.PilaGoTo.append(step_add)
    goTo = semantic.PilaO.pop()
    semantic.generate_quad("GOTOF", goTo, None, None)
    pass

def p_add_else(p):
    'add_else :'
    semantic.generate_quad("GOTO", None, None, None)
    ifFalseS = semantic.PilaGoTo.pop()
    ifFalseGo = len(semantic.QuadList)
    step_add = len(semantic.QuadList)
    semantic.PilaGoTo.append(step_add - 1)
    semantic.QuadList[ifFalseS][3] = ifFalseGo
    semantic.QuadListMemory[ifFalseS][3] = ifFalseGo
    pass

def p_add_endif(p):
    'add_endif :'
    step_add = len(semantic.QuadList)
    ifT = semantic.PilaGoTo.pop()
    semantic.QuadList[ifT][3] = step_add
    semantic.QuadListMemory[ifT][3] = step_add
    pass


def p_expression(p):
    'expression : exp comparison'
    while semantic.PilaOper and semantic.PilaOper[-1] != '(': # When an expression is finish we must do the quad
        clean_quad()
    pass


def p_comparison(p):
    '''comparison : GREATER add_op exp
                  | LESS add_op exp
                  | DIFFERENT add_op exp
                  | STRICT_EQUAL add_op exp
                  | GREATER_EQUAL add_op exp
                  | LESS_EQUAL add_op exp
                  | empty'''
    pass

def p_exp(p):
    'exp : term add_sub'
    pass

def p_add_suba(p):
    '''add_sub : PLUS add_op term add_sub
                  | MINUS add_op term add_sub
                  | empty'''
    pass

def p_term(p):
    'term : factor mult_div'
    pass

def p_mult_div(p):
    '''mult_div : TIMES add_op factor mult_div
                | DIVIDE add_op factor mult_div
                | empty'''
    pass


def p_factor(p):
    '''factor : grouping
              | unary_sign
              | cte
              | ID id_func_option'''
    if len(p) == 3 and p[2] is not None:
        return
    
    elif len(p) == 3 and p[2] is None: #If is ID append to pila operandos and appends its type
        semantic.PilaO.append(p[1]) 
        var_type = semantic.func_dir.get_var_type(semantic.current_function, p[1])
        semantic.PilaT.append(var_type)

    elif len(p) == 2 and isinstance(p[1], (int, float)): #If is cte append to pila operandos and appends its type
        semantic.PilaO.append(p[1])
        if isinstance(p[1], int):
            semantic.PilaT.append("int")
        else:
            semantic.PilaT.append("float")
    pass

def p_id_func_option(p):
    '''id_func_option : f_call
                      | empty'''
    if p.slice[1].type == 'empty':
        p[0] = None      # NO es función
    else:
        p[0] = "fcall"   # SÍ es función
    pass

def p_grouping(p):
    'grouping : LPARENTESIS push_paren expression RPARENTESIS close_paren' #Asociation taking parenteses into account
    pass

def p_push_paren(p):
    'push_paren :'
    semantic.PilaOper.append('(')

def p_close_paren(p):
    'close_paren :'
    while semantic.PilaOper[-1] != '(':
        clean_quad()
    semantic.PilaOper.pop()

def p_unary_sign(p):
    '''unary_sign : PLUS value
                  | MINUS value'''
    pass

def p_value(p):
    '''value : ID
             | cte'''
    pass

def p_cte(p):
    '''cte : CTE_INT
           | CTE_FLOAT'''
    if p.slice[1].type == 'CTE_INT': # THIS IS SO THAT FACTOR CAN TAKE THE VALUE AND MAKE THE QUADS
        val = int(p[1])
    else:
        val = float(p[1])
    p[0] = val
    pass


def p_funcs(p):
    'funcs : prepare_new_func funcs_type add_current_type ID add_function LPARENTESIS start_func_vars parameters RPARENTESIS restart_param_count LBRACES add_start_fun function_block RBRACES SEMICOLON end_func'

def p_prepare_new_func(p):
    'prepare_new_func :'
    semantic.current_type = None
    semantic.current_function = None
    print("Step 6, Prepare for new func")

def p_funcs_type(p):
    '''funcs_type : VOID
                  | type'''
    p[0] = p[1]
    pass

def p_add_current_type(p):
    'add_current_type :'
    semantic.current_type = p[-1]
    print(f"Step 7, New func type detected '{semantic.current_type}'")
    pass

def p_add_function(p):
    'add_function :'
    func_name = p[-1]
    semantic.func_dir.add_function(func_name, semantic.current_type, None, [])
    semantic.current_function = func_name
    print(f"Step 8, New func '{func_name}' added")
    pass

def p_start_func_vars(p):
    'start_func_vars :'
    semantic.func_dir.directory[semantic.current_function]['vars'] = semantic.VarTable(semantic.current_function)
    #print(f"Step 10, VarTable created for func '{semantic.current_function}'") #ESTO LLO TENGO QUE HACER????
    pass

def p_end_func(p):
    'end_func :'
    print(f"Step 10: Deleting var table '{semantic.current_function}'")
    semantic.current_function = list(semantic.func_dir.directory.keys())[0]
    semantic.current_type = None
    semantic.QuadList.append(["ENDFUNC", None, None, None])
    semantic.QuadListMemory.append(["ENDFUNC", None, None, None])
    #comentados en los test
    #semantic.func_dir.directory[semantic.current_function]['vars'] = None

def p_parameters(p):
    '''parameters : parameter parameter_list
                  | empty'''
    
    pass

def p_parameter(p):
    'parameter : ID COLON type'
    param_name = p[1]
    param_type = p[3]
    semantic.func_dir.directory[semantic.current_function]['params'].append(param_type)
    semantic.func_dir.add_var(semantic.current_function, param_name, param_type) #se agrega la de las dirreciones
    print("Step 9, add parameter", param_name, param_type)
    pass

def p_parameter_list(p):
    '''parameter_list : COMMA parameter parameter_list
                      | empty'''
    pass

def p_function_block(p):
    '''function_block : vars body
                      | body'''
    pass

def p_add_start_fun(p):
    'add_start_fun :'
    #print("AQUI EMPIEZA", len(semantic.QuadList)+1)
    semantic.func_dir.directory[semantic.current_function]['startLine'] = len(semantic.QuadList)
    pass

def p_f_call(p):
    'f_call : LPARENTESIS make_era arguments make_go_sub RPARENTESIS'
    pass

def p_make_era(p):
    'make_era :'
    func_name = p[-2]
    semantic.call_function = func_name
    semantic.QuadList.append(["ERA", func_name, None, None])
    semantic.QuadListMemory.append(["ERA", func_name, None, None])
    semantic.parameter_check = 0
    pass

def p_make_go_sub(p):
    'make_go_sub :'
    func = semantic.call_function

    gosub_value = semantic.func_dir.directory[func]['startLine']
    semantic.QuadList.append(["GOSUB", gosub_value, None, None])
    semantic.QuadListMemory.append(["GOSUB", gosub_value, None, None])

    ret_type = semantic.func_dir.directory[func]['type']
    if ret_type != 'void':
        temp = semantic.new_temp()

        # memoria del temporal
        if ret_type == 'int':
            memory.allocate("TempInt", temp)
        elif ret_type == 'float':
            memory.allocate("TempFloat", temp)
        else:
            memory.allocate("TempBool", temp)

        semantic.QuadList.append(["=", func, None, temp])
        semantic.QuadListMemory.append(["=", func, None, temp])

        semantic.PilaO.append(temp)
        semantic.PilaT.append(ret_type)


    semantic.call_function = None


def p_arguments(p):
    '''arguments : expression declare_param argument_list
                 | empty'''
    pass

def p_argument_list(p): #aqui
    '''argument_list : COMMA expression declare_param argument_list 
                     | empty'''
    pass

def p_declare_param(p): #check parameters type
    'declare_param :'
    parameter = semantic.PilaO[-1]
    parameter_type = semantic.PilaT[-1]
    param_check = f"par{semantic.parameter_check+1}"
    if semantic.func_dir.directory[semantic.call_function]['params'][semantic.parameter_check] == parameter_type:
        semantic.QuadList.append(["PARAMETER", parameter, None, param_check])
        semantic.QuadListMemory.append(["PARAMETER", parameter, None, param_check])
        semantic.parameter_check += 1
    else:
         raise TypeError(f"cannot call funct with those parameters")
    pass

def p_restart_param_count(p):
    'restart_param_count :'
    semantic.parameter_check = 0
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' (line {p.lineno})")
    else:
        print("Syntax error at end of file")

def p_empty(p):
    'empty :'
    pass

# for quads TODOS LAS PARTES DONDE LLAME ADD_OP ES UN PUNTO NEURALGICO
def p_add_op(p):
    'add_op :'
    op = p[-1]
    procces_quad(op)

parser = yacc.yacc()