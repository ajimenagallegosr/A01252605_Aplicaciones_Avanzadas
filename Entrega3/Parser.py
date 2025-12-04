import ply.yacc as yacc
from Lexer import tokens
import Semantic as semantic

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
    semantic.generate_quad(operator, left, right, temp)
    semantic.PilaO.append(temp)
    semantic.PilaT.append(result_type)

def procces_quad(op):
    print("entro")
    prec = {'+': 2, '-': 2, '*': 3, '/': 3, '<': 1, '>': 1, '!=': 1, '==': 1}

    while semantic.PilaOper and semantic.PilaOper[-1] and prec.get(semantic.PilaOper[-1], 0) >= prec.get(op, 0):
        clean_quad()

    semantic.PilaOper.append(op)

def p_program(p):
    'program : PROGRAM create_dirfunc ID create_id SEMICOLON declarations functions MAIN body END clean_program'
    print("Programa válido")

def p_create_dirfunc(p):
    'create_dirfunc :'
    semantic.func_dir = semantic.FunctionDirectory()
    semantic.current_function = None
    print("Step 1: Global function directory created")

def p_create_id(p):
    'create_id :'
    program_name = p[-1]
    semantic.func_dir.add_function(program_name, 'program')
    semantic.current_function = program_name
    print(f"Step 2, Program '{program_name}' name registered")

def p_clean_program(p):
    'clean_program :'
    print("Step 5 (Final), Delete global table")
    semantic.print_quads()
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
        semantic.func_dir.add_var(semantic.current_function, semantic.temp_ids.pop(0), tipo)
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
                 | RETURN expression
                 | ID id_option
                 | LBRACKETS statement_list RBRACKETS'''
    pass

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
    semantic.generate_quad('print', None, None, value_print)
    pass

def p_print_element_str(p):
    'print_element : CTE_STRING'
    value_print = p[1]
    semantic.generate_quad('print', None, None, value_print)
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
    'cycle : WHILE LPARENTESIS expression RPARENTESIS DO body SEMICOLON'
    pass

def p_condition(p):
    'condition : IF LPARENTESIS expression RPARENTESIS body else_part SEMICOLON'
    pass

def p_else_part(p):
    '''else_part : ELSE body
                 | empty'''
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
    if len(p) == 3 and p.slice[1].type == 'ID': #If is ID append to pila operandos and appends its type
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
    'funcs : prepare_new_func funcs_type add_current_type ID add_function LPARENTESIS start_func_vars parameters RPARENTESIS LBRACES function_block RBRACES SEMICOLON end_func'

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
    semantic.func_dir.add_function(func_name, semantic.current_type)
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
    #comentados en los test
    #semantic.func_dir.directory[semantic.current_function]['vars'] = None
    #semantic.current_function = None

def p_parameters(p):
    '''parameters : parameter parameter_list
                  | empty'''
    
    pass

def p_parameter(p):
    'parameter : ID COLON type'
    param_name = p[1]
    param_type = p[3]
    semantic.func_dir.add_var(semantic.current_function, param_name, param_type)
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

def p_f_call(p):
    'f_call : LPARENTESIS arguments RPARENTESIS'
    pass

def p_arguments(p):
    '''arguments : expression argument_list
                 | empty'''
    pass

def p_argument_list(p):
    '''argument_list : COMMA expression argument_list
                     | empty'''
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