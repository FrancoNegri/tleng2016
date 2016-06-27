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
	'''g : sentencia g  '''

def p_g2(subexpressions):
	'''g : ctrl g'''

def p_g3(subexpressions):
	'''g : empty'''

#S ->  VarOps ; | Func ;| return ;| varAsig;
def p_sentencia1(subexpressions):
	'''sentencia : varsOps  ';' '''
def p_sentencia2(subexpressions):
	'''sentencia : func ';' '''

#Esta tendria que ir para mi
#def p_sentencia3(subexpressions):
# '''sentencia : valores ';' '''

def p_sentencia3(subexpressions):
	'''sentencia : varAsig ';' '''

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
	'''if : IF '(' expBool ')' bloque else'''

def p_else1(subexpressions):
	'''else : ELSE bloque '''

def p_else2(subexpressions):
	'''else : empty'''

#Bloque -> S | {G}
def p_bloque1(subexpressions):
	'''bloque : sentencia ';' '''
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

# FuncString -> capitalizar(eMat)
def p_funcString(subexpressions):
	'''funcString : CAPITALIZAR '(' eMat ')' '''

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
	'''vec : '[' elem ']' '''
#Elem-> Valores, Elem | Valores
def p_elem1(subexpressions):
	'''elem : valores ',' elem'''
def p_elem2(subexpressions):
	'''elem : valores'''

#Valores -> EMat | ExpBool | eMat | VarYVals | FuncReturn | Reg


def p_valores(subexpressions):
  '''valores : eMat
  | expBool
  | reg
  | INT
  | FLOAT
  | STRING
  | BOOL
  | varYVals
  | varsOps
  | vec
  | ID '.' valoresCampos
  | RES'''

def p_valoresCampos(subexpressions):
	'''valoresCampos : ID
	| END
	| BEGIN'''
#VarYVals -> var | VecVal
def p_varYVals1(subexpressions):
	'''varYVals : ID'''
def p_varYVals2(subexpressions):
	'''varYVals : vecVal'''

#VecVal ->  var M
def p_vecVal1(subexpressions):
	'''vecVal : ID m'''		

#M -> [int] | [int] M

#Aca se volvio un poco turbio, pero debe poder pasar esto g[b] 
#Entonces, mas general deberia poder pasar g[h[t[a]]] mientras los tipos anden :)
def p_m1(subexpressions):
	'''m : '[' INT ']' '''
def p_m2(subexpressions):
	''' m : '[' INT ']' m '''
def p_m3(subexpressions):
  ''' m : '[' varYVals ']' m '''
def p_m4(subexpressions):
  ''' m : '[' varYVals ']' '''

#Registros:
#Reg -> {U}
def p_reg(subexpressions):
	'''reg :  '{' campos '}' '''

#U -> campo: Valores, U | campof: Valores
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
	'''varsOps : MENOSMENOS varYVals 
	| MASMAS varYVals
	| varYVals MASMAS 
	| varYVals MENOSMENOS'''
	

#-----------------------------------------------------------------------------
#Asignaciones:

#Dejo las asignaciones no ambiguas como estaban antes
def p_valoresAsig(subexpressions):
  '''valoresAsig : valores'''

#Aca pongo varYvals por este caso g[a] = b;

def p_varAsig(subexpressions):
  '''varAsig : varYVals MULEQ valoresAsig
  | varYVals DIVEQ valoresAsig
  | varYVals MASEQ valoresAsig
  | varYVals MENOSEQ valoresAsig
  | varYVals '=' valoresAsig
  | ID '.' ID '=' valoresAsig'''


#-----------------------------------------------------------------------------
#Operaciones binarias enteras

# Coloco string aqui, luego chequeamos tipos para cuando se use
# las operaciones solo para INT
def p_valoresMat(subexpressions):
  '''valoresMat : INT
  | FLOAT
  | funcInt
  | varYVals
  | varsOps
  | STRING'''

#EMat -> EMat '+' P | EMat - P | P
def p_eMat(subexpressions):
    '''eMat : eMat '+' p
    | eMat '-' p
    | valoresMat '+' p
    | valoresMat '-' p
    | eMat '+' valoresMat
    | eMat '-' valoresMat
    | valoresMat '+' valoresMat
    | valoresMat '-' valoresMat
    | p'''

#P -> P * Exp | P / Exp | P % Exp | Exp

def p_p(subexpressions):
    '''p : p '*' exp
    | p '/' exp
    | p '%' exp
    | valoresMat '*' exp
    | valoresMat '/' exp
    | valoresMat '%' exp
    | p '*' valoresMat
    | p '/' valoresMat
    | p '%' valoresMat
    | valoresMat '*' valoresMat
    | valoresMat '/' valoresMat
    | valoresMat '%' valoresMat
    | exp
    '''

#Exp -> Exp ^ ISing | ISing
def p_exp(subexpressions):
	'''exp : exp '^' iSing
  | valoresMat '^' iSing
  | exp '^' valoresMat
  | valoresMat '^' valoresMat
  | iSing'''

#ISing -> -Paren | '+'Paren | Paren
def p_iSing(subexpressions):
	'''iSing : '-' paren
  | '+' paren
  | '-' valoresMat
  | '+' valoresMat
  | paren
  '''

#Paren -> (EMat) | int | VarYVals | float | VarsOps| FuncInt
def p_paren1(subexpressions):
	'''paren : '(' eMat ')' '''

# ---------------------------------------------------------------------------------------
# Expresiones booleanas

#Aca agrego int y float y emat porque si no lo que sigue no se puede generar
#(x > 5 ? y : 10) o f ? 3 : x + 5
#Esto tambien daria lugar a cosas como 
#(2? 3 : 4) que tiene cierto sentido (porque 2 es siempre true). Si no, se puede filtrar con atributos.

def p_valoresBool(subexpressions):
  '''valoresBool : BOOL
  | funcBool
  | varYVals
  | varsOps
  | eMat
  | INT
  | FLOAT'''

# ExpBool -> Or ? ExpBool : ExpBool  | Or
#Aca agrego combinaciones que faltaban
def p_expBool(subexpressions):
  '''expBool : or '?' expBool ':' expBool  
  | or '?' expBool ':' valoresBool
  | or '?' valoresBool ':' expBool
  | or '?' valoresBool ':' valoresBool
  | valoresBool '?' expBool ':' expBool
  | valoresBool '?' valoresBool ':' expBool
  | valoresBool '?' expBool ':' valoresBool
  | valoresBool '?' valoresBool ':' valoresBool
  | or'''

# Or -> Or or And | And
def p_or1(subexpressions):
  '''or : or OR and
  | valoresBool OR and
  | or OR valoresBool
  | valoresBool OR valoresBool
  | and'''

# And ->  And and Eq | Eq
def p_and(subexpressions):
  '''and : and AND eq
  | valoresBool AND eq
  | and AND valoresBool
  | valoresBool AND valoresBool
  | eq'''

# Eq -> Eq == TBool |  Eq != TBool | Mayor 
def p_eq(subexpressions):
  '''eq : eq EQEQ parenBool
  | eq DISTINTO parenBool
  | valoresBool EQEQ parenBool
  | valoresBool DISTINTO parenBool
  | eq EQEQ valoresBool
  | eq DISTINTO valoresBool
  | valoresBool EQEQ valoresBool
  | valoresBool DISTINTO valoresBool
  | mayor'''

# TCompare -> EMat | VarsOps | VarYVals
#Aca agrego para que puedan aparecer ints o floats solos por ej 5 < 5, emat no lo captura
def p_tCompare(subexpressions):
  '''tCompare : eMat
  | varsOps
  | varYVals
  | INT 
  | FLOAT'''

# Mayor -> TCompare > TCompare | Menor
def p_mayor(subexpressions):
  '''mayor : tCompare '>' tCompare
  | menor'''

  # if len(subexpressions) > 2:
  #   tokens = [subexpressions[1], subexpressions[3]]
  #   if not chequearTipo(tokens, ["int", "float"]):
  #     raise SemanticException("Se esperaba tipo int o float")


# Menor -> TCompare < TCompare | Not 
def p_menor3(subexpressions):
  '''menor : tCompare '<' tCompare
  | not'''
  # if len(subexpressions) > 2:
  #   tokens = [subexpressions[1], subexpressions[3]]
  #   if not chequearTipo(tokens, ["int", "float"]):
  #     raise SemanticException("Se esperaba tipo int o float")

# Not ->  not Not | TBool 
def p_not(subexpressions):
  '''not :  NOT not
  | NOT valoresBool
  | parenBool'''

# TBool -> (ExpBool) | bool | VarYVals | FuncBool
def p_parenBool(subexpressions):
  '''parenBool : '(' expBool ')' '''
  # if len(subexpressions) == 2:
  #   tokens = [subexpressions[1]]
  #   if not chequearTipo(tokens, ["bool"]):
  #     raise SemanticException("Se esperaba tipo bool")

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








