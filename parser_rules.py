from lexer_rules import tokens

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
	'''paren : varsYvals'''
def p_paren4(subexpressions):
	'''paren : FLOAT'''
def p_paren5(subexpressions):
	'''paren : varsOps'''
def p_paren6(subexpressions):
	'''paren : funcInt'''

#Operaciones con strings

#ExpString -> ExpString '+' string | string | VarYVals | FuncString
def p_expString1(subexpressions):
	'''expString : expString '+' STRING'''
def p_expString2(subexpressions):
	'''expString : STRING'''
def p_expString3(subexpressions):
	'''expString : varsYvals'''
def p_expString4(subexpressions):
	'''expString : FuncString'''

#Registros:
#Reg -> {U}
def p_reg(subexpressions):
	'''reg :  '{' campos '}' '''

#U -> campo: Valores, U | campo: Valores
#campo no es nada en la gramatica, pero creo que en realidad es cualquier string
#La segunda aparicion de : creara conflictos?
def p_campos1(subexpressions):
	'''campos : STRING ':' valores ',' campos'''
def p_campos2(subexpressions):
	'''campos : valores'''

#Operadores de variables:
#VarsOps -> --SMM | '+''+'SMM | SMM
def p_varsOps1(subexpressions):
	'''varsOps : MENOSMENOS sMM'''
def p_varsOps2(subexpressions):
	'''varsOps : MASMAS sMM'''
def p_varsOps3(subexpressions):
	'''varsOps : sMM'''

#SMM -> VarYVals'++' | VarYVals--
def p_sMM1(subexpressions):
	'''sMM : varYvals MASMAS'''
def p_sMM2(subexpressions):
	'''sMM : varYvals MENOSMENOS'''

#Asignaciones:

#VarAsig -> SIgual *= Valores | SIgual /= Valores | SIgual
def p_varAsig1(subexpressions):
	'''varAsig : sIgual POREQ valores'''
def p_varAsig2(subexpressions):
	'''varAsig : sIgual DIVEQ valores'''
def p_varAsig3(subexpressions):
	'''varAsig : sIgual'''

#SIgual -> Asig '+'= Valores |  Asig -= Valores | Asig
def p_sIgual1(subexpressions):
	'''sIgual : asig MASEQ valores'''
def p_sIgual2(subexpressions):
	'''sIgual : asig MENOSEQ valores'''
def p_sIgual3(subexpressions):
	'''sIgual : asig'''

#Asig -> var = Valores  | var = Vec          
def p_asig1(subexpressions):
	'''asig : ID '=' valores'''
def p_asig2(subexpressions):
	'''asig : ID '=' vec '''

#Vectores  y variables

#Vec ->  var = [Elem] 
def p_vec1(subexpressions):
	'''vec : ID '=' '[' elem ']' '''
#Elem-> Valores, Elem | Valores
def p_elem1(subexpressions):
	'''elem : valores ',' elem'''
def p_elem2(subexpressions):
	'''elem : valores'''

#Valores -> EMat | ExpBool | ExpString | VarYVals | FuncReturn | Reg
#Aca agrego que los valores sean registros. Dentro de las asignaciones se debe poder hacer  alumno  = {nombre: "asd"}
#Tambien falta ver el caso , que dice en el tp, siguiente: alumno.nombre = "asd"
def p_valores1(subexpressions):
	'''valores : eMat'''
def p_valores2(subexpressions):
	'''valores : expBool'''
def p_valores3(subexpressions):
	'''valores : expString'''
def p_valores4(subexpressions):
	'''valores : varYvals'''
def p_valores5(subexpressions):
	'''valores : funcReturn'''
def p_valores6(subexpressions):
	'''valores : reg'''

#VarYVals -> var | VecVal
def p_varYvals1(subexpressions):
	'''varYvals : ID'''
def p_varYvals2(subexpressions):
	'''varYvals : vecVal'''

#VecVal ->  var M
def p_vecVal1(subexpressions):
	'''vecVal : ID m'''		

#M -> [int] | [int] M

def p_m1(subexpressions):
	'''m : '[' INT ']' '''
def p_m2(subexpressions):
	''' m : '[' INT ']' m '''

#M -> ExpBool | lambda
#Este M no tiene nada que ver con el M de arriba, que se usa en el parametro de una funcion. Lo cambio
def p_param1(subexpressions):
	'''param : expBool'''
def p_param2(subexpressions):
	'''param : '''

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
	type_token1 = subexpressions[1].type
	type_token2 = subexpressions[2].type
	if type_token1 != "int" or type_token2 != "int":
		raise SemanticException("Se esperaba tipo int")

def p_mayor2(subexpressions):
	'''mayor : menor'''

# Menor -> TCompare < TCompare | Not 
def p_menor3(subexpressions):
	'''menor : tCompare '<' tCompare'''

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
	'''tBool : varsYvals'''

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

# Funciones auxiliares 

# Chequea si una lista de subexpresiones tienen igual tipo
# Usar como chequearTipo("int", *subexps)
def chequearTipo(type, *subexps):
	subexps = list(subexps)

	for subexp in subexps:
		if subexp["type"] != type:
			return False

	return True








