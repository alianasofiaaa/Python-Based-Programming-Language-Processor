import ply.yacc as yacc
from scanner import tokens

precedence = (
    ('left','OR'),
    ('left','AND'),
    ('left','EQUAL'),
    ('left','LESSTHAN','GREATERTHAN'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('left','DOT')
)

def p_global_facts_exec(p):
    'global_facts : facts exec_line'
    p[0] = {'type': 'program', 'facts': p[1], 'exec': p[2]}

def p_global_facts_noexec(p):
    'global_facts : facts'
    p[0] = {'type': 'program', 'facts': p[1]}

def p_facts_func(p):
    'facts : func_def facts'
    p[0] = [p[1]] + p[2]

def p_facts_assign(p):
    'facts : assign facts'
    p[0] = [p[1]] + p[2]

def p_facts_empty(p):
    'facts :'
    p[0] = []

def p_func_def(p):
    'func_def : FUNC ID_FUNC LBRACE params RBRACE ASSIGN stm END'
    p[0] = {'type': 'func_def', 'name': p[2], 'params': p[4], 'body': p[7]}

def p_params_multifunc(p):
    'params : ID_FUNC COMMA params'
    p[0] = [p[1]] + p[3]

def p_params_multiid(p):
    'params : ID COMMA params'
    p[0] = [p[1]] + p[3]

def p_params_singlefunc(p):
    'params : ID_FUNC'
    p[0] = [p[1]]

def p_params_singleid(p):
    'params : ID'
    p[0] = [p[1]]

def p_assign(p):
    'assign : VAL ID ASSIGN stm END'
    p[0] = {'type': 'assign', 'id': p[2], 'value': p[4]}

def p_exec_line(p):
    'exec_line : EXEC stm'
    p[0] = {'type': 'exec', 'stm': p[2]}

def p_stm_func(p):
    'stm : ID_FUNC LBRACE args RBRACE'
    p[0] = {'type': 'call', 'name': p[1], 'args': p[3]}

def p_args_func(p):
    'args : ID_FUNC COMMA args'
    p[0] = [{'type': 'id_func', 'value': p[1]}] + p[3]

def p_args_stm(p):
    'args : stm COMMA args'
    p[0] = [p[1]] + p[3]

def p_args_singlefunc(p):
    'args : ID_FUNC'
    p[0] = [{'type': 'id_func', 'value': p[1]}]

def p_args_singlestm(p):
    'args : stm'
    p[0] = [p[1]]

def p_stm_binop(p):
    '''stm : stm PLUS stm
           | stm MINUS stm
           | stm TIMES stm
           | stm DIVIDE stm
           | stm DOT stm
           | stm LESSTHAN stm
           | stm GREATERTHAN stm
           | stm EQUAL stm
           | stm AND stm
           | stm OR stm'''
    p[0] = {'type': 'binop', 'op': p[2], 'left': p[1], 'right': p[3]}

def p_stm_values(p):
    '''stm : STRING
           | NUMBER
           | TRUE
           | FALSE
           | NIL'''
    value = p[1]
    if value == 'true':
        value = True
    elif value == 'false':
        value = False
    elif value == 'nil':
        value = None
    p[0] = {'type': 'value', 'value': value}

def p_stm_id(p):
    'stm : ID'
    p[0] = {'type': 'id', 'value': p[1]}

def p_stm_group(p):
    'stm : LPAREN stm RPAREN'
    p[0] = p[2]

def p_stm_if(p):
    'stm : IF stm THEN stm ELSE stm END'
    p[0] = {'type': 'if', 'condition': p[2], 'then': p[4], 'else': p[6]}

def p_stm_let(p):
    'stm : LET facts IN stm END'
    p[0] = {'type': 'let', 'facts': p[2], 'body': p[4]}

def p_error(p):
    if p:
        print(f"Syntax error in input: {p.lineno}")
    else:
        print("Syntax error in input: EOF")

parser = yacc.yacc()