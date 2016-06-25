from lexer_rules import tokens
from lexer_rules import literals

# Simbolo inicial
start = 'g'

# ---------------------------------------------------------------------------------------
#Sentencias:

#G -> SG | CtrlG
def p_g1(subexpressions):
	'''g : sentencia g'''

def p_g3(subexpressions):
	'''g : empty'''


# Faltaban las asignaciones, el print y el return
def p_sentencia3(subexpressions):
	'''sentencia : varAsig  '''

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
	'''loop : WHILE '(' param ')' bloque'''
def p_loop2(subexpressions):
	'''loop : DO bloque WHILE '(' param ')' ';' '''
def p_loop3(subexpressions):
	'''loop : FOR '(' varAsig ';' param ';' varsOps ')' bloque '''

# ---------------------------------------------------------------------------------------
#Control:

# Modifico para que el else sea opcional
# IF-> if(ExpBool) then Bloque Else
# Else -> else Bloque | lambda
def p_if(subexpressions):
	'''if : IF '(' param ')' THEN bloque else'''

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

# FuncInt -> multiplicacionEscalar(Vec, EMat, Param) | length(Vec)

#vec en realidad es la definicion de un vector o sea, a = [1,1]. Esto puede tener sentido o no, pero tambien podriamos pasarle una variable_
#que ya es un vector como multiescalar(vector,2,) 
def p_funcInt1(subexpressions):
	'''funcInt : MULTIESCALAR '(' vec ',' param ',' param ')' '''

def p_funcInt2(subexpressions):
	'''funcInt : LENGTH '(' vec ')' '''

# FuncString -> capitalizar(ExpString)
def p_funcString(subexpressions):
	'''funcString : CAPITALIZAR '(' expString ')' '''

# FuncBool -> colineales(Vec,Vec )
def p_funcBool(subexpressions):
	'''funcBool : COLINEALES '(' vec ',' vec ')' '''

# FuncVoid -> print(Valores) 
def p_funcVoid(subexpressions):
	'''funcVoid : PRINT '(' valores ')' '''

#M -> ExpBool | lambda
#Este M no tiene nada que ver con el M de arriba, que se usa en el parametro de una funcion. Lo cambio
def p_param2(subexpressions):
	'''param : empty'''

def p_empty(subexpressions):
	'''empty : '''

#-----------------------------------------------------------------------------
#Vectores  y variables

#Esta produccion creo que no tiene sentido, porque en las producciones de asignaciones hacemos:
#asig -> var =  vec o sea a = a = [1,2]. Deberia quedar solo la parte entre corchetes, la lista. Esto tendria sentido para cuando hacemos tambien:
#multiescalar([1,2,3],mas cosas) eso tendria mas sentido que hacer una asignacion de vector en el primer parametros
#Vec ->  id = [Elem] 
def p_vec1(subexpressions):
	'''vec : ID '=' '[' elem ']' '''
#Elem-> Valores, Elem | Valores
def p_elem1(subexpressions):
	'''elem : valores ',' elem'''
def p_elem2(subexpressions):
	'''elem : valores'''

#Valores -> EMat | ExpBool | ExpString | VarYVals | FuncReturn | Reg
def p_valores1(subexpressions):
	'''valores : varYVals'''
def p_valores2(subexpressions):
	'''valores : funcReturn'''
def p_valores3(subexpressions):
	'''valores : reg'''
#Esto faltaba si se quiere hacer algo como variable = alumno.nombre. O sea, tiene sentido que alumno.nombre sea un valor
def p_valores4(subexpressions):
	'''valores : ID '.' ID '''

#VarYVals -> var | VecVal
def p_varYVals1(subexpressions):
	'''varYVals : ID'''
def p_varYVals2(subexpressions):
	'''varYVals : vecVal'''

#VecVal ->  var M
def p_vecVal1(subexpressions):
	'''vecVal : ID m'''		

#M -> [int] | [int] M

def p_m1(subexpressions):
	'''m : '[' INT ']' '''
def p_m2(subexpressions):
	''' m : '[' INT ']' m '''

#Registros:
#Reg -> {U}
def p_reg(subexpressions):
	'''reg :  '{' campos '}' '''

#U -> campo: Valores, U | campo: Valores
#campo no es nada en la gramatica, pero creo que en realidad es cualquier string(!)
#Me parece que mejore el campo es un ID (!)
def p_campos1(subexpressions):
	'''campos : ID ':' valores ',' campos'''
def p_campos2(subexpressions):
	'''campos : valores'''


#-----------------------------------------------------------------------------
#Operadores de variables:
#VarsOps -> --SMM | ++SMM | SMM
def p_varsOps1(subexpressions):
	'''varsOps : MENOSMENOS sMM 
	| MASMAS sMM
	| sMM'''
	
def p_sMM(subexpressions):
	'''sMM : ID MASMAS
	| ID MENOSMENOS
	| ID'''

#-----------------------------------------------------------------------------
#Asignaciones:


def p_varAsig1(subexpressions):
	'''varAsig : ID MASEQ varAsig '''

def p_varAsig2(subexpressions):
	'''varAsig : ID '=' varAsig'''
def p_varAsig4(subexpressions):
	'''varAsig : ID '=' valores '''
def p_varAsig3(subexpressions):
	'''varAsig : ID MASEQ valores '''	
precedence = (
    ('right', '='),
    ('right', 'MASEQ'),
)


#-----------------------------------------------------------------------------
#Operaciones con strings

#ExpString -> ExpString '+' string | string | VarYVals | FuncString
def p_expString1(subexpressions):
	'''expString : expString '+' STRING'''
def p_expString2(subexpressions):
	'''expString : STRING'''
def p_expString3(subexpressions):
	'''expString : varYVals'''
def p_expString4(subexpressions):
	'''expString : funcString'''


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

#------------------------------------------------------------------------------
# Funciones auxiliares 

# Chequea si todos los elementos de la lista de subexpresiones son de 
# algun tipo de la lista tipos
def chequearTipo(subexps, tipos):

	for subexp in subexps:
		if subexp["type"] not in tipos:
			return False

	return True








