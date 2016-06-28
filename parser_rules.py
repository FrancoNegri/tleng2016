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

#Generalizo la gramatica con linea, puede ser una sentencia o un comentario
def p_g1(subexpressions):
	'''g : linea g  '''

def p_g3(subexpressions):
	'''g : empty'''

def p_linea(subexpressions):
  '''linea : lAbierta
  | lCerrada'''

def p_lAbierta(subexpressions):
   '''lAbierta : IF '(' cosaBooleana ')' linea
  | IF '(' cosaBooleana ')' bloqueCerrado ELSE lAbierta 
  | loop  lAbierta '''

def p_bloqueCerrado(subexpressions):
  '''bloqueCerrado : lCerrada
  | '{' g '}' '''

def p_lCerrada(subexpressions):
  '''lCerrada : sentencia
  | COMMENT lCerrada
  | IF '(' cosaBooleana ')' bloqueCerrado ELSE bloqueCerrado
  | loop bloqueCerrado 
  | DO bloqueCerrado WHILE '(' cosaBooleana ')' ';' '''


def p_sentencia1(subexpressions):
	'''sentencia : varsOps  ';' '''
def p_sentencia2(subexpressions):
	'''sentencia : func ';' '''
def p_sentencia3(subexpressions):
	'''sentencia : varAsig ';' '''
def p_sentencia4(subexpressions):
	'''sentencia : RETURN ';' '''
def p_sentencia5(subexpressions):
  '''sentencia : ';' '''

def p_loop1(subexpressions):
  '''loop : WHILE '(' cosaBooleana ')' '''
#def p_loop2(subexpressions):
 # '''loop : DO lCerrada WHILE '(' expBool ')' ';' '''
def p_loop3(subexpressions):
  '''loop : FOR '(' primParam ';' cosaBooleana ';' tercerParam ')' '''


#en el tercer parametro del for pongo varOps, pero en realidad puede ser mas general(!), es lo que discutimos en clase.

#Este puede ser util para otras cosas de mas abajo. Ver como reemplazar !

def p_cosaBooleana(subexpressions):
  '''cosaBooleana : expBool
  | valoresBool'''

def p_primParam(subexpressions):
  '''primParam : varAsig
  | empty'''

def p_tercerParam(subexpressions):
  '''tercerParam : varsOps
  | varAsig
  | func
  | empty'''


# ---------------------------------------------------------------------------------------
#Control:

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



#ATENCION: para simplificar, o no, hice que las funciones tomen valores. Despues hay que restringirle el tipo 
#La otra opcion es ir separando , x ej, la primera recibiria un emat o valorMat. Asi con los otros

def p_funcInt1(subexpressions):
	'''funcInt : MULTIESCALAR '(' valores ',' valores   param ')' '''


def p_funcInt2(subexpressions):
	'''funcInt : LENGTH '(' valores ')' '''

# FuncString -> capitalizar(eMat)
#Aca lo mismo que en la de arriba, recibe un "string"

def p_funcString(subexpressions):
	'''funcString : CAPITALIZAR '(' valores ')' '''

# FuncBool -> colineales(Vec,Vec )
def p_funcBool(subexpressions):
	'''funcBool : COLINEALES '(' valores ',' valores ')' '''

# FuncVoid -> print(Valores) 
def p_funcVoid(subexpressions):
	'''funcVoid : PRINT '(' valores ')' '''

#Parametros de las funciones:

def p_param1(subexpressions):
	'''param : ',' valores'''

def p_param2(subexpressions):
	'''param : empty'''

def p_empty(subexpressions):
	'''empty : '''

#-----------------------------------------------------------------------------
#Vectores  y variables


def p_vec1(subexpressions):
	'''vec : '[' elem ']' '''
#Elem-> Valores, Elem | Valores
def p_elem1(subexpressions):
	'''elem : valores ',' elem'''
def p_elem2(subexpressions):
	'''elem : valores'''



def p_valores(subexpressions):
  '''valores : eMat
  | expBool
  | funcReturn
  | reg
  | INT
  | FLOAT
  | STRING
  | BOOL
  | varYVals
  | varsOps
  | vec
  | ternario
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

#Aca agrego int y float y emat y STRING porque si no lo que sigue no se puede generar
#(x > 5 ? y : 10) o f ? 3 : x + 5
#Esto tambien daria lugar a cosas como 
#(2? 3 : 4) que tiene cierto sentido (porque 2 es siempre true). Si no, se puede filtrar con atributos.

def p_valoresBool(subexpressions):
  '''valoresBool : BOOL
  | funcBool
  | varYVals
  | varsOps
  '''

# ExpBool -> Or ? ExpBool : ExpBool  | Or
#Aca agrego combinaciones que faltaban
def p_ternario(subexpressions):
  '''ternario : valoresBool '?' valores ':' valores  
  | expBool '?' valores ':' valores
  | '(' ternario ')' '''

# Or -> Or or And | And
def p_expBool(subexpressions):
  '''expBool : expBool OR and
  | valoresBool OR and
  | expBool OR valoresBool
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
  '''eq : eq EQEQ mayor
  | eq DISTINTO mayor
  | tCompare EQEQ mayor
  | tCompare DISTINTO mayor
  | eq EQEQ tCompare
  | eq DISTINTO tCompare
  | tCompare EQEQ tCompare
  | tCompare DISTINTO tCompare
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








