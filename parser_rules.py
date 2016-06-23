from lexer_rules import tokens

#Operaciones binarias enteras

#EMat → EMat + P | EMat - P | P

def p_eMat_plus(subexpressions):
    'eMat : eMat + p'
def p_eMat_plus(subexpressions):
    'eMat : eMat - p'
def p_eMat_plus(subexpressions):
    'eMat : p'

#P → P * Exp | P / Exp | P % Exp | Exp

def p_p(subexpressions):
    'p : p * exp'
def p_p(subexpressions):
    'p : p / exp'
def p_p(subexpressions):
    'p : p % exp'
def p_p(subexpressions):
    'p : exp'

#Exp → Exp ^ ISing | ISing
def p_exp(subexpressions):
	'exp : exp ^ iSing'
def p_exp(subexpressions):
	'exp : iSing'

#ISing → -Paren | +Paren | Paren
def p_iSing(subexpressions):
	'iSing : -paren'
def p_iSing(subexpressions):
	'iSing : +paren'
def p_iSing(subexpressions):
	'iSing : paren'

#Paren → (EMat) | int | VarYVals | float | VarsOps| FuncInt
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

#ExpString → ExpString + string | string | VarYVals | FuncString
def p_expString(subexpressions):
	'expString : expString + STRING'
def p_expString(subexpressions):
	'expString : STRING'
def p_expString(subexpressions):
	'expString : varsYvals'
def p_expString(subexpressions):
	'expString : FuncString'

#Registros:
#Reg → {U}
def p_reg(subexpressions):
	'reg : {campos}'

#U -> campo: Valores, U | campo: Valores
#campo no es nada en la gramatica, pero creo que en realidad es cualquier string
#La segunda aparicion de : creará conflictos?
def p_campos(subexpressions):
	'campos : STRING: valores, campos'
def p_campos(subexpressions):
	'campos : valores'

#Operadores de variables:
#VarsOps → --SMM | ++SMM | SMM
def p_varsOps(subexpressions):
	'varsOps : --sMM'
def p_varsOps(subexpressions):
	'varsOps : ++sMM'
def p_varsOps(subexpressions):
	'varsOps : sMM'

#SMM → VarYVals++ | VarYVals--
def p_sMM(subexpressions):
	'sMM : varYvals++'
def p_sMM(subexpressions):
	'sMM : varYvals--'

#Asignaciones:

#VarAsig → SIgual *= Valores | SIgual /= Valores | SIgual
def p_varAsig(subexpressions):
	'varAsig : sIgual POREQ valores'
def p_varAsig(subexpressions):
	'varAsig : sIgual DIVEQ valores'
def p_varAsig(subexpressions):
	'varAsig : sIgual'

#SIgual → Asig += Valores |  Asig -= Valores | Asig
def p_sIgual(subexpressions):
	'sIgual : asig MASEQ valores'
def p_sIgual(subexpressions):
	'sIgual : asig MENOSEQ valores'
def p_sIgual(subexpressions):
	'sIgual : asig'

#Asig → var = Valores  | var = Vec          
def p_asig(subexpressions):
	'asig : VAR = valores'
def p_asig(subexpressions):
	'asig : VAR = vec'

#Vectores  y variables

#Vec →  var = [Elem] 
def p_vec(subexpressions):
	'vec : VAR = [elem]'	
#Elem→ Valores, Elem | Valores
def p_elem(subexpressions):
	'elem : valores, elem'
def p_elem(subexpressions):
	'elem : valores'

#Valores → EMat | ExpBool | ExpString | VarYVals | FuncReturn | Reg
#Acá agrego que los valores sean registros. Dentro de las asignaciones se debe poder hacer  alumno  = {nombre: "asd"}
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

#VarYVals → var | VecVal
def p_varYvals(subexpressions):
	'varYvals : VAR'
def p_varYvals(subexpressions):
	'varYvals : vecVal'

#VecVal →  var M
def p_vecVal(subexpressions):
	'vecVal : VAR m'		

#M → [int] | [int] M

def p_m(subexpressions):
	'm : [INT]'
def p_m(subexpressions):
	'm : [INT] m'

#M → ExpBool | 𝝺
#Este M no tiene nada que ver con el M de arriba, que se usa en el parametro de una funcion. Lo cambio
def p_param(subexpressions):
	'param : expBool'
def p_param(subexpressions):
	'param : '












