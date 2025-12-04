import ply.yacc as yacc
from Lexer import tokens
        
def p_program(p):
    'program : PROGRAM ID SEMICOLON declarations functions MAIN body END'
    print("Programa válido")

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
    'identifier_list : ID identifier_list_tail'
    pass

def p_identifier_list_tail(p):
    '''identifier_list_tail : COMMA ID identifier_list_tail
                            | empty'''
    pass

def p_var_declaration_list(p):
    '''var_declaration_list : var_declaration var_declaration_list
                           | empty'''
    pass

def p_type(p):
    '''type : INT_TYPE
            | FLOAT_TYPE'''
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
    'print_element : expression'
    pass

def p_print_element_str(p):
    'print_element : CTE_STRING'
    pass


def p_print_element_list(p):
    '''print_element_list : COMMA print_element print_element_list
                          | empty'''
    pass

def p_assign(p):
    'assign : EQUALS expression SEMICOLON'
    pass

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
    pass


def p_comparison(p):
    '''comparison : GREATER exp
                  | LESS exp
                  | DIFFERENT exp
                  | STRICT_EQUAL exp
                  | empty'''
    pass

def p_exp(p):
    'exp : term add_sub'
    pass

def p_add_suba(p):
    '''add_sub : PLUS term add_sub
                  | MINUS term add_sub
                  | empty'''
    pass

def p_term(p):
    'term : factor mult_div'
    pass

def p_mult_div(p):
    '''mult_div : TIMES factor mult_div
                | DIVIDE factor mult_div
                | empty'''
    pass


def p_factor(p):
    '''factor : grouping
              | unary_sign
              | cte
              | ID id_func_option'''
    pass

def p_id_func_option(p):
    '''id_func_option : f_call
                      | empty'''
    pass

def p_grouping(p):
    'grouping : LPARENTESIS expression RPARENTESIS'
    pass

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
    pass


def p_funcs(p):
    'funcs : funcs_type ID LPARENTESIS parameters RPARENTESIS LBRACES function_block RBRACES SEMICOLON'

def p_funcs_type(p):
    '''funcs_type : VOID
                  | type'''
    pass

def p_parameters(p):
    '''parameters : parameter parameter_list
                  | empty'''
    
    pass

def p_parameter(p):
    'parameter : ID COLON type'
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


parser = yacc.yacc()