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

#S ->  VarOps ; | Func ;
def p_sentencia1(subexpressions):
	'''sentencia : varsOps ';' '''
def p_sentencia2(subexpressions):
	'''sentencia : func ';' '''

# Faltaban las asignaciones y el print
def p_sentencia3(subexpressions):
	'''sentencia : varAsig ';' '''

def p_sentencia4(subexpressions):
	'''sentencia : funcVoid ';' '''

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
	'''else : '''

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
def p_param(subexpressions):
	'''param : expBool'''

def p_param(subexpressions):
	'''param : empty'''

def p_empty(subexpressions):
	'''empty : '''

#-----------------------------------------------------------------------------
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
	'''valores : varYVals'''
def p_valores5(subexpressions):
	'''valores : funcReturn'''
def p_valores6(subexpressions):
	'''valores : reg'''

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

#-----------------------------------------------------------------------------
#Operadores de variables:
#VarsOps -> --SMM | '+''+'SMM | SMM
def p_varsOps1(subexpressions):
	'''varsOps : MENOSMENOS sMM'''

def p_varsOps2(subexpressions):
	'''varsOps : MASMAS sMM'''

def p_varsOps3(subexpressions):
	'''varsOps : sMM'''

# Aca hay un problema, varYVals contiene a valores de vectores, que no
# pueden aplicarse ++ o --
def p_sMM1(subexpressions):
	'''sMM : ID MASMAS'''
	tokens = [subexpressions[1]]
	if not chequearTipo(tokens, ["int"]):
		raise SemanticException("Se esperaba tipo int")

def p_sMM2(subexpressions):
	'''sMM : ID MENOSMENOS'''
	tokens = [subexpressions[1]]
	if not chequearTipo(tokens, ["int"]):
		raise SemanticException("Se esperaba tipo int")

#-----------------------------------------------------------------------------
#Asignaciones:

#VarAsig -> SIgual *= Valores | SIgual /= Valores | SIgual
def p_varAsig1(subexpressions):
	'''varAsig : sIgual MULEQ valores'''
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

# Falta el caso base, los ID
def p_asig2(subexpressions):
	'''asig : ID '''

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








