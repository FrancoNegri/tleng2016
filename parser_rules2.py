from lexer_rules import tokens

# Para el arbol sintactico
class Node:
    def __init__(self,type,children=None,leaf=None):
         self.type = type
         if children:
              self.children = children
         else:
              self.children = [ ]
         self.leaf = leaf

# Simbolo inicial

precedence = (
	('right','?'),
	('left','OR'),
	('left','AND'),
	('left','EQEQ','DISTINTO'),
	('left' '<', '>'),
	('right', 'MULEQ','DIVEQ'),
	('right', 'MASEQ','MENOSEQ'),
	('right', '='),
	('left', '+','-'),
	('left','*','/','%'),
	('left', '^'),
	('left','UNIMAS', 'UNIMENOS'),
	('left','NOT'),	
	('left','MASMAS','MENOSMENOS'),
	('left','MASMASIZQ','MENOSMENOSIZQ'),		
)

def p_varYVals(subexpressions):
	'''varYVals : ID'''

def p_varOps(subexpressions):
	'''varOps : ID MASMAS'''

def p_funcInt(subexpressions):
	'''funcInt : LENGTH'''

def p_funcBool(subexpressions):
	'''funcBool : COLINEALES'''

def p_funcString(subexpressions):
	'''funcString : CAPITALIZAR'''

def p_varExpresion(subexpressions):
	'''varExpresion : varExpresion '+' varExpresion 
	| varExpresion '-' varExpresion 
	| varExpresion '*' varExpresion 
	| varExpresion '/' varExpresion 
	| varExpresion '%' varExpresion 
	| varExpresion '^' varExpresion 
	| '(' '-' '(' varExpresion ')' ')' %prec UNIMENOS
	| '(' '+' '(' varExpresion ')' ')' %prec UNIMAS
	| varExpresion '?' varExpresion ':' varExpresion 
	| varExpresion OR varExpresion 
	| varExpresion EQEQ varExpresion 
	| varExpresion DISTINTO varExpresion 
	| varExpresion '>' varExpresion 
	| varExpresion '<' varExpresion 
	| '(' varExpresion ')' 
	| varYVals 
	| varOps 
	| INT 
	| FLOAT 
	| BOOL 
	| STRING 
	| funcInt 
	| funcBool 
	| funcString'''

#--------------------------------------------------------------------------------------
# Caso error

def p_error(token):
    message = "[Syntax error]"
    if token is not None:
        message += "\ntype:" + token.type
        message += "\nvalue:" + str(token.value)
        message += "\nline:" + str(token.lineno)
        message += "\nposition:" + str(token.lexpos)
    raise Exception(message)