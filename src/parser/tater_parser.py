import ply.lex as lex;

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
    'to': 'TO'
}

tokens  = list(reserved.values())
tokens += ['LARROW', 'SYMBOL', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE']
tokens += ['LBRACKET', 'RBRACKET', 'POUND', 'COLON']
tokens += ['PLUS', 'MINUS', 'DIVIDE', 'TIMES', 'POWER', 'EQASSIGN']
tokens += ['AND', 'OR', 'NOT']
tokens += ['EQ', 'NOTEQ', 'LT', 'GT', 'LTEQ', 'GTEQ']
tokens += ['SEMI', 'BAR']
tokens += ['CHAR', 'STRING', 'NUMBER', 'TRUE', 'FALSE']
