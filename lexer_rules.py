reserved = {
'begin' : 'BEGIN',
'end' : 'END',
'while' : 'WHILE',
'for' : 'FOR',
'if' : 'IF',
'else' : 'ELSE',
'do' : 'DO',
'res' : 'RES',
'return' : 'RETURN',
'AND' : 'AND',
'OR' : 'OR',
'NOT' : 'NOT',
'print' : 'PRINT',
'multiplicacionEscalar': 'MULTIESCALAR',
'capitalizar': 'CAPITALIZAR',
'colineales': 'COLINEALES',
'print': 'PRINT',
'length': 'LENGTH',
}

literals = [
'+',
'-',
'*',
'/',
'^',
'%',
'<',
'>',
'=',
'!',
'{',
'}',
'(',
')',
'[',
']',
'?',
':',
';',
',',
'.'
]

tokens = [
#Tipos:
'STRING',
'FLOAT',
'BOOL',
'INT',
#Operadores Del sistema:
'COMMENT',
'ID',
'EQEQ',
'DISTINTO',
'MENOSEQ',
'MASEQ',
'MULEQ',
'DIVEQ',
'MASMAS',
'MENOSMENOS'
] + list(reserved.values())

# t_STRING = r''' " .*? " '''
def t_STRING(token):
    r''' " .*? " '''
    atributos = {}
    atributos["type"] = "string"
    atributos["value"] = token.value
    token.value = atributos
    return token

t_EQEQ = r"=="
t_DISTINTO = r"!="
t_MENOSEQ = r"-="
t_MASEQ = r"\+="
t_MULEQ = r"\*="
t_DIVEQ = r"/="
t_MASMAS = r"\+\+"
t_MENOSMENOS = r"--"

def t_BOOL(token) : 
    r"true | false"
    atributos = {}
    atributos["type"] = "bool"
    atributos["value"] = token.value
    token.value = atributos
    return token

def t_FLOAT(token):
    r"[-]?[0-9] \. [0-9]*"
    atributos = {}
    atributos["type"] = "int"
    atributos["value"] = token.value
    token.value = atributos
    return token

def t_INT(token) : 
    r"[-]?[1-9][0-9]* | 0"
    atributos = {}
    atributos["type"] = "int"
    atributos["value"] = token.value
    token.value = atributos
    return token

def t_ID(token):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t = token.value
    tipo = reserved.get(token.value)   
    if t.lower() not in reserved and t.upper() not in reserved and t != "multiplicacionEscalar":
            tipo = 'ID'
    token.type = tipo
    atributos = {}
    atributos["value"] = token.value
    atributos["var"] = token.value
    atributos["type"] = "noType"
    token.value = atributos
    return token

def t_NEWLINE(token):
  r"\n+"
  token.lexer.lineno += len(token.value)

def t_COMMENT(token):
    r'\#.*'
    return token

t_ignore  = ' \t'

def t_error(token):
    message = "Token desconocido:"
    message += "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise Exception(message)
