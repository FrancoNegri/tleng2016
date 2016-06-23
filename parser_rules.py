from lexer_rules import tokens

#Operaciones binarias enteras

#EMat -> EMat + P | EMat - P | P

def p_eMat_plus(subexpressions):
    'eMat : eMat + p'
def p_eMat_plus(subexpressions):
    'eMat : eMat - p'
def p_eMat_plus(subexpressions):
    'eMat : p'

#P -> P * Exp | P / Exp | P % Exp | Exp

def p_p(subexpressions):
    'p : p * exp'
def p_p(subexpressions):
    'p : p / exp'
def p_p(subexpressions):
    'p : p % exp'
def p_p(subexpressions):
    'p : exp'

#Exp -> Exp ^ ISing | ISing
def p_exp(subexpressions):
	'exp : exp ^ iSing'
def p_exp(subexpressions):
	'exp : iSing'

#ISing -> -Paren | +Paren | Paren
def p_iSing(subexpressions):
	'iSing : -paren'
def p_iSing(subexpressions):
	'iSing : +paren'
def p_iSing(subexpressions):
	'iSing : paren'

#Paren -> (EMat) | int | VarYVals | float | VarsOps| FuncInt
def p_paren(subexpressions):
	'paren : (eMat)'
def p_paren(subexpressions):
	'paren : INT'
def p_paren(subexpressions):
	'paren : varsYvals'
def p_paren(subexpressions):
	'paren : FLOAT'
def p_paren(subexpressions):
	'paren : varsOps'
def p_paren(subexpressions):
	'paren : funcInt'

#Operaciones con strings

#ExpString -> ExpString + string | string | VarYVals | FuncString
def p_expString(subexpressions):
	'expString : expString + STRING'
def p_expString(subexpressions):
	'expString : STRING'
def p_expString(subexpressions):
	'expString : varsYvals'
def p_expString(subexpressions):
	'expString : FuncString'

#Registros:
#Reg -> {U}
def p_reg(subexpressions):
	'reg : {campos}'

#U -> campo: Valores, U | campo: Valores
#campo no es nada en la gramatica, pero creo que en realidad es cualquier string
#La segunda aparicion de : creara conflictos?
def p_campos(subexpressions):
	'campos : STRING: valores, campos'
def p_campos(subexpressions):
	'campos : valores'

#Operadores de variables:
#VarsOps -> --SMM | ++SMM | SMM
def p_varsOps(subexpressions):
	'varsOps : --sMM'
def p_varsOps(subexpressions):
	'varsOps : ++sMM'
def p_varsOps(subexpressions):
	'varsOps : sMM'

#SMM -> VarYVals++ | VarYVals--
def p_sMM(subexpressions):
	'sMM : varYvals++'
def p_sMM(subexpressions):
	'sMM : varYvals--'

#Asignaciones:

#VarAsig -> SIgual *= Valores | SIgual /= Valores | SIgual
def p_varAsig(subexpressions):
	'varAsig : sIgual POREQ valores'
def p_varAsig(subexpressions):
	'varAsig : sIgual DIVEQ valores'
def p_varAsig(subexpressions):
	'varAsig : sIgual'

#SIgual -> Asig += Valores |  Asig -= Valores | Asig
def p_sIgual(subexpressions):
	'sIgual : asig MASEQ valores'
def p_sIgual(subexpressions):
	'sIgual : asig MENOSEQ valores'
def p_sIgual(subexpressions):
	'sIgual : asig'

#Asig -> var = Valores  | var = Vec          
def p_asig(subexpressions):
	'asig : VAR = valores'
def p_asig(subexpressions):
	'asig : VAR = vec'

#Vectores  y variables

#Vec ->  var = [Elem] 
def p_vec(subexpressions):
	'vec : VAR = [elem]'	
#Elem-> Valores, Elem | Valores
def p_elem(subexpressions):
	'elem : valores, elem'
def p_elem(subexpressions):
	'elem : valores'

#Valores -> EMat | ExpBool | ExpString | VarYVals | FuncReturn | Reg
#Aca agrego que los valores sean registros. Dentro de las asignaciones se debe poder hacer  alumno  = {nombre: "asd"}
#Tambien falta ver el caso , que dice en el tp, siguiente: alumno.nombre = "asd"
def p_valores(subexpressions):
	'valores : eMat'
def p_valores(subexpressions):
	'valores : expBool'
def p_valores(subexpressions):
	'valores : expString'
def p_valores(subexpressions):
	'valores : varYvals'
def p_valores(subexpressions):
	'valores : funcReturn'
def p_valores(subexpressions):
	'valores : reg'

#VarYVals -> var | VecVal
def p_varYvals(subexpressions):
	'varYvals : VAR'
def p_varYvals(subexpressions):
	'varYvals : vecVal'

#VecVal ->  var M
def p_vecVal(subexpressions):
	'vecVal : VAR m'		

#M -> [int] | [int] M

def p_m(subexpressions):
	'm : [INT]'
def p_m(subexpressions):
	'm : [INT] m'

#M -> ExpBool | lambda
#Este M no tiene nada que ver con el M de arriba, que se usa en el parametro de una funcion. Lo cambio
def p_param(subexpressions):
	'param : expBool'
def p_param(subexpressions):
	'param : '

# ---------------------------------------------------------------------------------------

# Expresiones booleanas

# ExpBool -> Or ? ExpBool : ExpBool  | Or
def p_expBool(subexpressions):
	'expBool : or ? expBool : expBool'

def p_expBool(subexpressions):
	'expBool : or'

# Or -> Or or And | And
def p_or(subexpressions):
	'or : or OR and'

def p_or(subexpressions):
	'or : and'

# And ->  And and Eq | Eq
def p_and(subexpressions):
	'and : and AND eq'

def p_and(subexpressions):
	'and : eq'

# Eq -> Eq == TBool |  Eq != TBool | Mayor 
def p_eq(subexpressions):
	'eq : eq EQEQ tBool'

def p_eq(subexpressions):
	'eq : eq DISTINTO tBool'

def p_eq(subexpressions):
	'eq : mayor'

# Mayor -> TCompare > TCompare | Menor
def p_mayor(subexpressions):
	'mayor : tCompare > tCompare'
	type_token1 = subexpressions[1].type
	type_token2 = subexpressions[2].type
	if type_token1 != "int" or type_token2 != "int":
		raise SemanticException("Se esperaba tipo int")

def p_mayor(subexpressions):
	'mayor : menor'

# Menor -> TCompare < TCompare | Not 
def p_menor(subexpressions):
	'menor : tCompare < tCompare'

def p_menor(subexpressions):
	'menor : not'

# Not ->  not Not | TBool 
def p_not(subexpressions):
	'not :  NOT not'

def p_not(subexpressions):
	'not :  tBool'

# TBool -> (ExpBool) | bool | VarYVals | FuncBool
def p_tBool(subexpressions):
	'tBool : ( expBool )'

def p_tBool(subexpressions):
	'tBool : BOOL'

def p_tBool(subexpressions):
	'tBool : varsYvals'

def p_tBool(subexpressions):
	'tBool : funcBool'

# TCompare -> EMat | VarsOps | VarYVals
def p_tCompare(subexpressions):
	'tCompare : eMat'
	subexpressions[0] = {"type" : "int"}

def p_tCompare(subexpressions):
	'tCompare : varsOps'
	varsOps = subexpressions[1]
	subexpressions[0] = {"type" : varsOps["type"]}

def p_tCompare(subexpressions):
	'tCompare : varYVals'
	varYVals = subexpressions[1]
	subexpressions[0] = {"type" : varYVals["type"]}

# Le saco funcInt ya que esta en eMat

#--------------------------------------------------------------------------------------













