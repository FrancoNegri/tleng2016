reserved = {
'begin' : 'BEGIN',
'end' : 'END',
'while' : 'WHILE',
'for' : 'FOR',
'if' : 'IF',
'then' : 'THEN',
'else' : 'ELSE',
'do' : 'DO',
'res' : 'RES',
'return' : 'RETURN',
'true' : 'TRUE',
'false' : 'FALSE',
'and' : 'AND',
'or' : 'OR',
'not' : 'NOT'
}

tokens = [
#Tipos:
'STRING',
'FLOAT',
#'BOOL'
'INT',
'VAR',
#Funciones:
'MULTIESCALAR',
'CAPITALIZAR',
'COLINEALES',
'PRINT',
'LENGTH',
#Operadores Del sistema:
'DOBLEPUNTO',
'PUNTOCOMA',
'COMA',
'COMENT',
'LLLAVE', 
'RLLAVE' ,
'LPAREN',
'RPAREN',
'LCORCHETE',
'RCORCHETE',
'INTERR',             
# ?
#Operadores Matem:
'MAS',
'MULTI',
'DIV',
'RESTA',
'EXP',
'MOD',
'IGUAL',
'MENOR',
'MAYOR',
'ID',
] + list(reserved.values())

t_STRING = r''' " .* " '''

t_MAS = r"\+"

def t_INT(token) : 
	r"[-]?[1-9][0-9]*"
	token.value = int(token.value)
	return token

def t_FLOAT(token):
	r"[-]?[1-9] \. [0-9]*"
	token.value = float(token.value)
	return token

def t_ID(token):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    token.type = reserved.get(token.value,'ID')    # Check for reserved words
    return token

def t_NEWLINE(token):
  r"\n+"
  token.lexer.lineno += len(token.value)

def t_COMMENT(t):
    r'\#.*'
    pass

t_ignore  = ' \t'

def t_error(token):
    message = "Token desconocido:"
    message += "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise Exception(message)