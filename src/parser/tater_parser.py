import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'switch': 'SWITCH',
    'function': 'FUNCTION',
    'do': 'DO',
    'done': 'DONE',
    'let': 'LET',
    'in': 'IN',
    'set': 'SET',
    'to': 'TO',
    'true': 'TRUE',
    'false': 'FALSE'
}

tokens = list(reserved.values())
tokens += ['LARROW', 'SYMBOL', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE']
tokens += ['LBRACKET', 'RBRACKET', 'POUND', 'COLON']
tokens += ['PLUS', 'MINUS', 'DIVIDE', 'TIMES', 'POWER', 'EQASSIGN']
tokens += ['AND', 'OR', 'NOT']
tokens += ['EQ', 'NOTEQ', 'LT', 'GT', 'LTEQ', 'GTEQ']
tokens += ['SEMI', 'COMMA', 'BAR']
tokens += ['CHAR', 'STRING', 'NUMBER']

t_LARROW = r'\<-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_POUND = r'\#'
t_COLON = r':'
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'\/'
t_TIMES = r'\*'
t_POWER = r'\*\*'
t_EQASSIGN = r'='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_EQ = r'==='
t_NOTEQ = r'!=='
t_LT = r'\<'
t_GT = r'\>'
t_LTEQ = r'\<='
t_GTEQ = r'\>='
t_SEMI = r';'
t_COMMA = r','
t_BAR = r'\|'

def t_SYMBOL(t):
    r'[_a-zA-z][0-9a-zA-Z_\-]+'
    return t

def t_NUMBER(t):
    r'\d+(\.\d)?'
    return t

def t_CHAR(t):
    r'\'.?\''
    return t

def t_STRING(t):
    r'"([^"]*)"'
    return t

LINENO = 1

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    global LINENO
    LINENO += 1

def t_error(t):
    print "Syntax error at {linenb}, {linexp}, unknown: '{value}'".format(
        linenb = t.lexer.lineno,
        linexp = t.lexer.lexpos,
        value = t.value[0]
    )

    t.lexer.skip(1)

t_ignore_COMMENT = r'\#.*'
t_ignore = ' \t'

lexer = lex.lex()

precedences = (
    ('left', 'PLUS', 'MINUS', 'OR'),
    ('left', 'DIVIDE', 'TIMES', 'AND'),
    ('left', 'POWER'),
    ('right', 'UMINUS', 'NOT')
)

def p_empty(p):
    'empty :'
    pass

def p_program(p):
    """
    program : empty
            | function_dec_list
    """
    pass

def p_function_dec_list(p):
    """
    function_dec_list : function_dec SEMI
                      | function_dec SEMI function_dec_list
    """
    pass

def p_function_dec(p):
    """
    function_dec : FUNCTION LPAREN argument_def_list RPAREN EQASSIGN expression
    """
    pass

def p_argument_def_list(p):
    """
    argument_def_list : SYMBOL
                      | SYMBOL argument_def_list_tail
    """
    pass
def p_argument_def_list_tail(p):
    """
    argument_def_list_tail : empty
                           | COMMA argument_def_list
    """
    pass


def p_expression(p):
    """
    expression :
    """
    pass

def binary_expression(p):
    """
    binary_expression :
    """
    pass

def unary_expression(p):
    """
    unary_expression :
    """
    pass

def expression_atom(p):
    """
    expression_atom :
    """
    pass

def function_call_expression(p):
    """
    function_call_expression :
    """
    pass

def if_expression(p):
    """
    if_expression :
    """
    pass

def switch_expression(p):
    """
    switch_expression :
    """
    pass

def let_expression(p):
    """
    let_expression :
    """
    pass

def literal_value(p):
    """
    literal_value :
    """
    pass

def do_block(p):
    """
    do_block :
    """
    pass

#TEST
def test():
    data = """
        "hi Potato!"
        should_not_fail
    """

    parser_input = """
        function (x,y,z) = expression;
        function (i,j,k) = expression;
        function (hallo) = hallo;
    """
    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)

test()
