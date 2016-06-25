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
	'''loop : WHILE '(' expBool ')' bloque'''
def p_loop2(subexpressions):
	'''loop : DO bloque WHILE '(' expBool ')' ';' '''
def p_loop3(subexpressions):
	'''loop : FOR '(' varAsig ';' expBool ';' varsOps ')' bloque '''

# ---------------------------------------------------------------------------------------
#Control:

# Modifico para que el else sea opcional
# IF-> if(ExpBool) then Bloque Else
# Else -> else Bloque | lambda
def p_if(subexpressions):
	'''if : IF '(' expBool ')' THEN bloque else'''

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
	'''funcInt : MULTIESCALAR '(' vec ',' eMat ',' param ')' '''

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
def p_param1(subexpressions):
	'''param : expBool'''

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
#Aca agrego que los valores sean registros. Dentro de las asignaciones se debe poder hacer  alumno  = {nombre: "asd"}

def p_valores1(subexpressions):
	'''valores : eMat'''
def p_valores2(subexpressions):
	'''valores : expBool'''
def p_valores3(subexpressions):
	'''valores : expString'''
def p_valores4(subexpressions):
	'''valores : varYVals'''
def p_valores5(subexpressions):
	'''valores : funcReturn'''
def p_valores6(subexpressions):
	'''valores : reg'''
#Esto faltaba si se quiere hacer algo como variable = alumno.nombre. O sea, tiene sentido que alumno.nombre sea un valor
def p_valores7(subexpressions):
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
	if len(subexpressions) > 2:
		indexSMM = 2
	else:
		indexSMM = 1

	variable = subexpressions[indexSMM]
	tipoVariable = variable["type"]
	nombreVariable = variable["name"]

	if tipoVariable != "int":
		raise Exception("Se esperaba tipo int")

# SMM -> ID++ | ID--
# Aca hay un problema, varYVals contiene a valores de vectores, que no
# pueden aplicarse ++ o --
# Tambien falta el caso base ID
def p_sMM(subexpressions):
	'''sMM : ID MASMAS
	| ID MENOSMENOS
	| ID'''
	variable = subexpressions[1]
	tipoVariable = variable["type"]
	nombreVariable = variable["name"]
	subexpressions[0] = {"type" : tipoVariable, "name": nombreVariable}

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

precedence = (
    ('right', 'MULEQ','DIVEQ'),
    ('right', 'MASEQ','MENOSEQ'),
    ('right', '='),
    
)

#-----------------------------------------------------------------------------
#Operaciones binarias enteras

#EMat -> EMat '+' P | EMat - P | P

def p_eMat_plus(subexpressions):
    '''eMat : eMat '+' p'''
def p_eMat_minus(subexpressions):
    '''eMat : eMat '-' p'''
def p_eMat(subexpressions):
    '''eMat : p'''

#P -> P * Exp | P / Exp | P % Exp | Exp

def p_p1(subexpressions):
    '''p : p '*' exp'''
def p_p2(subexpressions):
    '''p : p '/' exp'''
def p_p3(subexpressions):
    '''p : p '%' exp'''
def p_p4(subexpressions):
    '''p : exp'''

#Exp -> Exp ^ ISing | ISing
def p_exp(subexpressions):
	'''exp : exp '^' iSing'''
def p_exp2(subexpressions):
	'''exp : iSing'''

#ISing -> -Paren | '+'Paren | Paren
def p_iSing1(subexpressions):
	'''iSing : '-' paren'''
def p_iSing2(subexpressions):
	'''iSing : '+' paren'''
def p_iSing3(subexpressions):
	'''iSing : paren'''

#Paren -> (EMat) | int | VarYVals | float | VarsOps| FuncInt
def p_paren1(subexpressions):
	'''paren : '(' eMat ')' '''
def p_paren2(subexpressions):
	'''paren : INT'''
def p_paren3(subexpressions):
	'''paren : varYVals'''
def p_paren4(subexpressions):
	'''paren : FLOAT'''
def p_paren5(subexpressions):
	'''paren : varsOps'''
def p_paren6(subexpressions):
	'''paren : funcInt'''

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

#-----------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------
# Expresiones booleanas

# ExpBool -> Or ? ExpBool : ExpBool  | Or
def p_expBool1(subexpressions):
	'''expBool : or '?' expBool ':' expBool'''

def p_expBool2(subexpressions):
	'''expBool : or'''

# Or -> Or or And | And
def p_or1(subexpressions):
	'''or : or OR and'''

def p_or2(subexpressions):
	'''or : and'''

# And ->  And and Eq | Eq
def p_and1(subexpressions):
	'''and : and AND eq'''

def p_and2(subexpressions):
	'''and : eq'''

# Eq -> Eq == TBool |  Eq != TBool | Mayor 
def p_eq1(subexpressions):
	'''eq : eq EQEQ tBool'''

def p_eq2(subexpressions):
	'''eq : eq DISTINTO tBool'''

def p_eq3(subexpressions):
	'''eq : mayor'''

# Mayor -> TCompare > TCompare | Menor
def p_mayor1(subexpressions):
	'''mayor : tCompare '>' tCompare'''
	tokens = [subexpressions[1], subexpressions[3]]
	if not chequearTipo(tokens, ["int", "float"]):
		raise SemanticException("Se esperaba tipo int o float")

def p_mayor2(subexpressions):
	'''mayor : menor'''

# Menor -> TCompare < TCompare | Not 
def p_menor3(subexpressions):
	'''menor : tCompare '<' tCompare'''
	tokens = [subexpressions[1], subexpressions[3]]
	if not chequearTipo(tokens, ["int", "float"]):
		raise SemanticException("Se esperaba tipo int o float")

def p_menor4(subexpressions):
	'''menor : not'''

# Not ->  not Not | TBool 
def p_not1(subexpressions):
	'''not :  NOT not'''

def p_not2(subexpressions):
	'''not :  tBool'''

# TBool -> (ExpBool) | bool | VarYVals | FuncBool
def p_tBool3(subexpressions):
	'''tBool : '(' expBool ')' '''

def p_tBool4(subexpressions):
	'''tBool : BOOL'''

def p_tBool5(subexpressions):
	'''tBool : varYVals'''
	tokens = [subexpressions[1]]
	if not chequearTipo(tokens, ["bool"]):
		raise SemanticException("Se esperaba tipo bool")

def p_tBool6(subexpressions):
	'''tBool : funcBool'''

# TCompare -> EMat | VarsOps | VarYVals
def p_tCompare1(subexpressions):
	'''tCompare : eMat'''
	subexpressions[0] = {"type" : "int"}

def p_tCompare2(subexpressions):
	'''tCompare : varsOps'''
	varsOps = subexpressions[1]
	subexpressions[0] = {"type" : varsOps["type"]}

def p_tCompare3(subexpressions):
	'''tCompare : varYVals'''
	varYVals = subexpressions[1]
	subexpressions[0] = {"type" : varYVals["type"]}

# Le saco funcInt ya que esta en eMat

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








