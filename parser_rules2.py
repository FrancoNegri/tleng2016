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

#-----------------------------------------------------------------------------
#Operadores de variables:
#VarsOps -> --SMM | ++SMM | SMM
def p_varsOps1(subexpressions):
	'''varsOps : MENOSMENOS sMM 
	| MASMAS sMM
	| sMM 
	| MENOSMENOS varYVals 
	| MASMAS varYVals'''
def p_sMM(subexpressions):
	'''sMM : varYVals MASMAS
	| varYVals MENOSMENOS'''

#-----------------------------------------------------------------------------
#Asignaciones:

#ACA HAGO CAMBIOS RELEVANTES!


def p_varAsig1(subexpressions):
	'''varAsig : ID MENOSEQ varAsig '''
def p_varAsig2(subexpressions):
	'''varAsig : ID MASEQ varAsig '''
def p_varAsig3(subexpressions):
	'''varAsig : ID MULEQ varAsig '''
def p_varAsig4(subexpressions):
	'''varAsig : ID DIVEQ varAsig '''
def p_varAsig5(subexpressions):
	'''varAsig : ID '=' varAsig'''	
#Casos base
def p_varAsig6(subexpressions):
	'''varAsig : ID MASEQ valores '''	
def p_varAsig7(subexpressions):
	'''varAsig : ID MENOSEQ valores '''	
def p_varAsig8(subexpressions):
	'''varAsig : ID MULEQ valores '''	
def p_varAsig9(subexpressions):
	'''varAsig : ID DIVEQ valores '''	
def p_varAsig10(subexpressions):
	'''varAsig : ID '=' valores '''



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