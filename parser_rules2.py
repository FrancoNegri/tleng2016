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
start = 'g'

# ---------------------------------------------------------------------------------------
#Sentencias:

#G -> SG | CtrlG
def p_g1(subexpressions):
	'''g : sentencia g'''

def p_g2(subexpressions):
	'''g : ctrl g'''

def p_g3(subexpressions):
	'''g : empty'''


#S ->  VarOps ; | Func ;| return ;| varAsig;
def p_sentencia1(subexpressions):
	'''sentencia : varsOps ';' '''
def p_sentencia2(subexpressions):
	'''sentencia : func ';' '''

# Faltaban las asignaciones, el print y el return
def p_sentencia3(subexpressions):
	'''sentencia : varAsig ';' '''

#Esta ya esta capturada en func
#def p_sentencia4(subexpressions):
#	'''sentencia : funcVoid ';' '''

def p_sentencia5(subexpressions):
	'''sentencia : RETURN ';' '''

#Ctrl -> IF| Loop
def p_ctrl1(subexpressions):
	'''ctrl : if'''
def p_ctrl2(subexpressions):
	'''ctrl : loop'''

#Loop -> while(ExpBool) Bloque | do Bloque while(ExpBool); | for(VarAsig; ExpBool; )Bloque
#en el tercer parametro del for pongo varOps, pero en realidad puede ser mas general(!), es lo que discutimos en clase.
def p_loop1(subexpressions):
	'''loop : WHILE '(' varExpresion')' bloque'''
def p_loop2(subexpressions):
	'''loop : DO bloque WHILE '(' varExpresion ')' ';' '''
def p_loop3(subexpressions):
	'''loop : FOR '(' varExpresion ';' varExpresion ';' varOps')' bloque '''

# ---------------------------------------------------------------------------------------
#Control:

# Modifico para que el else sea opcional
# IF-> if(ExpBool) then Bloque Else
# Else -> else Bloque | lambda
def p_if(subexpressions):
	'''if : IF '(' varExpresion ')' THEN bloque else'''

def p_else1(subexpressions):
	'''else : ELSE bloque '''

def p_else2(subexpressions):
	'''else : empty'''

#Bloque -> S | {G}
def p_bloque1(subexpressions):
	'''bloque : sentencia '''
def p_bloque2(subexpressions):
	'''bloque : '{' g '}' '''

#-----------------------------------------------------------------------------
#Funciones

# Func -> FuncReturn | FuncVoid
def p_func1(subexpressions):
	'''func : funcReturn'''

def p_func2(subexpressions):
	'''func : funcVoid'''

# FuncReturn -> FuncInt | FuncString | FuncBool
def p_funcReturn1(subexpressions):
	'''funcReturn : funcInt'''

def p_funcReturn2(subexpressions):
	'''funcReturn : funcString'''

def p_funcReturn3(subexpressions):
	'''funcReturn : funcBool'''

# FuncInt -> multiplicacionEscalar(ID, EMat, Param) | length(Vec)

#vec en realidad es la definicion de un vector o sea, a = [1,1]. Esto puede tener sentido o no, pero tambien podriamos pasarle una variable_
#que ya es un vector como multiescalar(vector,2,) 
def p_funcInt1(subexpressions):
	'''funcInt : MULTIESCALAR '(' varExpresion ',' varExpresion ',' param ')' '''

def p_funcInt2(subexpressions):
	'''funcInt : LENGTH '(' varExpresion ')' '''

# FuncString -> capitalizar(ExpString)
def p_funcString(subexpressions):
	'''funcString : CAPITALIZAR '(' varExpresion ')' '''

# FuncBool -> colineales(Vec,Vec )
def p_funcBool(subexpressions):
	'''funcBool : COLINEALES '(' varExpresion ',' varExpresion ')' '''

# FuncVoid -> print(Valores) 
def p_funcVoid(subexpressions):
	'''funcVoid : PRINT '(' varExpresion ')' '''

#M -> ExpBool | lambda
#Este M no tiene nada que ver con el M de arriba, que se usa en el parametro de una funcion. Lo cambio
def p_param1(subexpressions):
	'''param : varExpresion'''

def p_param2(subexpressions):
	'''param : empty'''

def p_empty(subexpressions):
	'''empty : '''



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