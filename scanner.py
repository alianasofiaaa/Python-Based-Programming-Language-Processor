import ply.lex as lex

# BEGIN LEXICAL ANALYZER DEFINITION
#reserved words
reserved={
    'if':'IF',
    'then':'THEN',
    'else':'ELSE',
    'let':'LET',
    'val':'VAL',
    'func':'FUNC',
    'end':'END',
    'in':'IN',
    'nil':'NIL',
    'false':'FALSE',
    'true':'TRUE',
    'exec':'EXEC'
}

#token list
tokens=[
    'ID',
    'ID_FUNC',
    'NUMBER',
    'STRING',

    #operators
    'EQUAL',
    'LESSTHAN',
    'GREATERTHAN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'DOT',
    'AND',
    'OR',

    #delimeters
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'ASSIGN'
] + list(reserved.values())

#operators
t_EQUAL = r'='
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_DOT = r'\.'
t_AND = r'&'
t_OR = r'\|'

#delimiters
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\['
t_RBRACE = r'\]'
t_COMMA = r','
t_ASSIGN = r':='

#uppercase
def t_ID_FUNC(t):
    r'[A-Z][A-Za-z0-9_\']*'
    return t

#lowercase
def t_ID(t):
    r'[a-z][A-Za-z0-9_\']*'
    if t.value in reserved:
        t.type=reserved[t.value]
    return t

#number rule
def t_NUMBER(t):
    r'\d+'
    t.value=int(t.value)
    return t

#string rule for double quotes
def t_STRING(t):
    r'"[^"\n]*"'
    return t

#ignore spaces, tabs, return
t_ignore=' \t\r'

#ignore comments
def t_COMMENT(t):
    r'//.*'
    pass

#keep track of line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#error handling
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#build lexer
lexer=lex.lex()

    
# END LEXICAL ANALYZER DEFINITION

#build lexer
lexer=lex.lex()
