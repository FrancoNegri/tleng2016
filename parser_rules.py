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

#Tengo dudas con
def p_g1(subexpressions):
  '''g : linea g  '''
  subexpressions[0] = toString(subexpressions) 
def p_g2(subexpressions):
  '''g : COMMENT g  '''
  subexpressions[0] = toString(subexpressions) 


def p_g3(subexpressions):
  '''g : empty'''
  subexpressions[0] = toString(subexpressions)

def p_linea(subexpressions):
  '''linea : lAbierta '''  
  subexpressions[0] = toString(subexpressions)

def p_linea1(subexpressions):
  '''linea : lCerrada'''
  subexpressions[0] = toString(subexpressions)



def p_lAbierta(subexpressions):
  '''lAbierta : IF '(' cosaBooleana ')' linea
  | IF '(' cosaBooleana ')' '{' g '}' ELSE lAbierta 
  | IF '(' cosaBooleana ')' lCerrada ELSE lAbierta 
  | IF '(' cosaBooleana ')' '{' g '}'
  | loop  lAbierta  '''
  subexpressions[0] = toString(subexpressions)

#Saco el bloque cerrado, ver si lo puedo meter de vuelta para mas claridad
def p_lCerrada1(subexpressions):
  '''lCerrada : sentencia'''
  subexpressions[0] = toString(subexpressions)

#UHm, esto esta bien??
# def p_lCerrada2(subexpressions):
#   '''lCerrada : COMMENT lCerrada'''
#   subexpressions[0] = toString(subexpressions)

def p_com(subexpressions):
  '''com : COMMENT com
  | empty '''


def p_lCerrada3(subexpressions):
  '''lCerrada : IF '(' cosaBooleana ')' '{' g '}' ELSE '{' g '}'
  | IF '(' cosaBooleana ')' lCerrada ELSE '{' g '}'
  | IF '(' cosaBooleana ')' COMMENT com lCerrada ELSE '{' g '}'
  | IF '(' cosaBooleana ')' '{' g '}' ELSE lCerrada
  | IF '(' cosaBooleana ')' lCerrada ELSE lCerrada
  | IF '(' cosaBooleana ')' COMMENT com lCerrada ELSE lCerrada
  | IF '(' cosaBooleana ')' lCerrada ELSE  COMMENT com lCerrada
  | IF '(' cosaBooleana ')' COMMENT com lCerrada ELSE  COMMENT com lCerrada '''
  subexpressions[0] = toString(subexpressions)

def p_lCerrada4(subexpressions):
  '''lCerrada : loop '{' g '}' 
  | loop lCerrada 
  | loop COMMENT com lCerrada '''

  subexpressions[0] = toString(subexpressions)

def p_lCerrada5(subexpressions):
  '''lCerrada : DO '{' g '}' WHILE '(' valores ')' ';' 
  | DO lCerrada WHILE '(' valores ')' ';' 
  | DO COMMENT com lCerrada WHILE '(' valores ')' ';' '''
  subexpressions[0] = toString(subexpressions)

def p_sentencia1(subexpressions):
  '''sentencia : varsOps  ';' '''
  subexpressions[0] = toString(subexpressions)

def p_sentencia2(subexpressions):
  '''sentencia : func ';' '''
  subexpressions[0] = toString(subexpressions)

def p_sentencia3(subexpressions):
  '''sentencia : varAsig ';' '''
  subexpressions[0] = toString(subexpressions)

def p_sentencia4(subexpressions):
  '''sentencia : RETURN ';' '''
  subexpressions[0] = toString(subexpressions)

def p_sentencia5(subexpressions):
  '''sentencia : ';' '''
  subexpressions[0] = toString(subexpressions)

#Ojo, estoy usando valores, habria que chequear tipos...

def p_loop1(subexpressions):
  '''loop : WHILE '(' valores ')' '''
  subexpressions[0] = toString(subexpressions)


def p_loop3(subexpressions):
  '''loop : FOR '(' primParam ';' valores ';' tercerParam ')' '''
  subexpressions[0] = toString(subexpressions)

#en el tercer parametro del for pongo varOps, pero en realidad puede ser mas general(!), es lo que discutimos en clase.

#Este puede ser util para otras cosas de mas abajo. Ver como reemplazar !

def p_cosaBooleana(subexpressions):
  '''cosaBooleana : expBool
  | valoresBool'''
  subexpressions[0] = toString(subexpressions)

def p_primParam(subexpressions):
  '''primParam : varAsig
  | empty'''
  subexpressions[0] = toString(subexpressions)

def p_tercerParam(subexpressions):
  '''tercerParam : varsOps
  | varAsig
  | func
  | empty'''
  subexpressions[0] = toString(subexpressions)

# ---------------------------------------------------------------------------------------
#Control:

#-----------------------------------------------------------------------------
#Funciones


# Func -> FuncReturn | FuncVoid
def p_func1(subexpressions):
  '''func : funcReturn'''
  subexpressions[0] = toString(subexpressions)

def p_func2(subexpressions):
  '''func : funcVoid'''
  subexpressions[0] = toString(subexpressions)


# FuncReturn -> FuncInt | FuncString | FuncBool
def p_funcReturn1(subexpressions):
  '''funcReturn : funcInt'''
  subexpressions[0] = toString(subexpressions)

def p_funcReturn2(subexpressions):
  '''funcReturn : funcString'''
  subexpressions[0] = toString(subexpressions)

def p_funcReturn3(subexpressions):
  '''funcReturn : funcBool'''
  subexpressions[0] = toString(subexpressions)



#ATENCION: para simplificar, o no, hice que las funciones tomen valores. Despues hay que restringirle el tipo 
#La otra opcion es ir separando , x ej, la primera recibiria un emat o valorMat. Asi con los otros

def p_funcInt1(subexpressions):
  '''funcInt : MULTIESCALAR '(' valores ',' valores   param ')' '''
  subexpressions[0] = toString(subexpressions)


def p_funcInt2(subexpressions):
  '''funcInt : LENGTH '(' valores ')' '''
  subexpressions[0] = toString(subexpressions)

# FuncString -> capitalizar(eMat)
#Aca lo mismo que en la de arriba, recibe un "string"

def p_funcString(subexpressions):
  '''funcString : CAPITALIZAR '(' valores ')' '''
  subexpressions[0] = toString(subexpressions)

# FuncBool -> colineales(Vec,Vec )
def p_funcBool(subexpressions):
  '''funcBool : COLINEALES '(' valores ',' valores ')' '''
  subexpressions[0] = toString(subexpressions)

# FuncVoid -> print(Valores) 
def p_funcVoid(subexpressions):
  '''funcVoid : PRINT '(' valores ')' '''
  subexpressions[0] = toString(subexpressions)

#Parametros de las funciones:

def p_param1(subexpressions):
  '''param : ',' valores'''
  subexpressions[0] = toString(subexpressions)

def p_param2(subexpressions):
  '''param : empty'''
  subexpressions[0] = toString(subexpressions)

def p_empty(subexpressions):
  '''empty : '''
  subexpressions[0] = toString(subexpressions)

#-----------------------------------------------------------------------------
#Vectores  y variables


def p_vec1(subexpressions):
  '''vec : '[' elem ']' '''
  subexpressions[0] = toString(subexpressions)

#Elem-> Valores, Elem | Valores
def p_elem1(subexpressions):
  '''elem : valores ',' elem'''
  subexpressions[0] = toString(subexpressions)

def p_elem2(subexpressions):
  '''elem : valores'''
  subexpressions[0] = toString(subexpressions)

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
  | atributos
  | RES'''
  subexpressions[0] = toString(subexpressions)

def p_atributos(subexpressions):
  '''atributos : ID '.' valoresCampos
  | reg '.' valoresCampos '''
  subexpressions[0] = toString(subexpressions)

def p_valoresCampos(subexpressions):
  '''valoresCampos : varYVals
  | END
  | BEGIN'''
  subexpressions[0] = toString(subexpressions)

def p_ternarioVars(subexpressions):
  '''ternarioVars : valoresBool '?' valoresTernarioVars ':' valoresTernarioVars  
  | valoresBool '?' valoresTernarioVars ':' valoresTernarioMat 
  | valoresBool '?' valoresTernarioMat ':' valoresTernarioVars
  | valoresBool '?' valoresTernarioVars ':' valoresTernarioBool 
  | valoresBool '?' valoresTernarioBool ':' valoresTernarioVars
  | expBool '?' valoresTernarioVars ':' valoresTernarioVars
  | expBool '?' valoresTernarioVars ':' valoresTernarioMat 
  | expBool '?' valoresTernarioMat ':' valoresTernarioVars
  | expBool '?' valoresTernarioVars ':' valoresTernarioBool 
  | expBool '?' valoresTernarioBool ':' valoresTernarioVars  '''

  subexpressions[0] = toString(subexpressions)

def p_valoresTernarioVars(subexpressions):
  '''valoresTernarioVars : varsOps
  | varYVals
  | reg
  | vec
  | ternarioVars
  | '(' ternarioVars ')'
  | atributos
  | RES'''
  subexpressions[0] = toString(subexpressions)

#VarYVals -> var | VecVal
def p_varYVals1(subexpressions):
  '''varYVals : ID'''
  subexpressions[0] = toString(subexpressions)

def p_varYVals2(subexpressions):
  '''varYVals : vecVal
    | vecVal '.' varYVals
  '''
  subexpressions[0] = toString(subexpressions)

#VecVal ->  var M
def p_vecVal1(subexpressions):
  '''vecVal : ID m
  | vec m'''
  subexpressions[0] = toString(subexpressions)

#Aca se volvio un poco turbio, pero debe poder pasar esto g[b] 
#Entonces, mas general deberia poder pasar g[h[t[a]]] mientras los tipos anden :)
#OJO! ACA EN VEZ DE INT PONGO VALORES, HAY QUE CHEQUEAR TIPOS DESPUES....
def p_m1(subexpressions):
  '''m : '[' valores ']' '''
  subexpressions[0] = toString(subexpressions)
def p_m2(subexpressions):
  ''' m : '[' valores ']' m '''
  subexpressions[0] = toString(subexpressions)
# def p_m3(subexpressions):
#   ''' m : '[' varYVals ']' m '''
#   subexpressions[0] = toString(subexpressions)
# def p_m4(subexpressions):
#   ''' m : '[' varYVals ']' '''
#   subexpressions[0] = toString(subexpressions)
# # a[3*4]
# def p_m5(subexpressions):
#  ''' m : '[' eMat ']' m '''
#  subexpressions[0] = toString(subexpressions)
# def p_m6(subexpressions):
#  ''' m : '[' eMat ']' '''
#  subexpressions[0] = toString(subexpressions)


#Registros:
#Reg -> {U}
def p_reg(subexpressions):
  '''reg :  '{' campos '}' '''
  subexpressions[0] = toString(subexpressions)

#U -> campo: Valores, U | campof: Valores
#campo no es nada en la gramatica, pero creo que en realidad es cualquier string(!)
#Me parece que mejore el campo es un ID (!)
def p_campos1(subexpressions):
  '''campos : ID ':' valores ',' campos'''
  subexpressions[0] = toString(subexpressions)
def p_campos2(subexpressions):
  '''campos : ID ':' valores'''
  subexpressions[0] = toString(subexpressions)


#-----------------------------------------------------------------------------
#Operadores de variables:
#VarsOps -> --SMM | ++SMM | SMM
def p_varsOps1(subexpressions):
  '''varsOps : MENOSMENOS varYVals 
  | MASMAS varYVals
  | varYVals MASMAS 
  | varYVals MENOSMENOS'''
  subexpressions[0] = toString(subexpressions)
  
#-----------------------------------------------------------------------------
#Asignaciones:

#Dejo las asignaciones no ambiguas como estaban antes
def p_valoresAsig(subexpressions):
  '''valoresAsig : valores'''
  subexpressions[0] = toString(subexpressions)

#Aca pongo varYvals por este caso g[a] = b;

def p_varAsig(subexpressions):
  '''varAsig : varYVals MULEQ valoresAsig
  | varYVals DIVEQ valoresAsig
  | varYVals MASEQ valoresAsig
  | varYVals MENOSEQ valoresAsig
  | varYVals '=' valoresAsig
  | ID '.' ID '=' valoresAsig'''
  subexpressions[0] = toString(subexpressions)

#-----------------------------------------------------------------------------
#Operaciones binarias enteras

# Coloco string aqui, luego chequeamos tipos para cuando se use
# las operaciones solo para INT

#ACa agrego tambien la funcionString, habria que hacer chequeos despues...
def p_valoresMat(subexpressions):
  '''valoresMat : INT
  | FLOAT
  | atributos
  | funcString
  | funcInt
  | varYVals
  | varsOps
  | STRING
  | '(' ternarioMat ')' '''
  subexpressions[0] = toString(subexpressions)

def p_ternarioMat(subexpressions):
  '''ternarioMat : valoresBool '?' valoresTernarioMat ':' valoresTernarioMat  
  | expBool '?' valoresTernarioMat ':' valoresTernarioMat'''
  subexpressions[0] = toString(subexpressions)

def p_valoresTernarioMat(subexpressions):
  '''valoresTernarioMat : INT
  | FLOAT
  | funcInt
  | STRING
  | eMat
  | ternarioMat
  | '(' ternarioMat ')' '''
  subexpressions[0] = toString(subexpressions)

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
    subexpressions[0] = toString(subexpressions)

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
    subexpressions[0] = toString(subexpressions)

#Exp -> Exp ^ ISing | ISing
def p_exp(subexpressions):
  '''exp : exp '^' iSing
  | valoresMat '^' iSing
  | exp '^' valoresMat
  | valoresMat '^' valoresMat
  | iSing'''
  subexpressions[0] = toString(subexpressions)

#ISing -> -Paren | '+'Paren | Paren
def p_iSing(subexpressions):
  '''iSing : '-' paren
  | '+' paren
  | '-' valoresMat
  | '+' valoresMat
  | paren
  '''
  subexpressions[0] = toString(subexpressions)

#Paren -> (EMat) | int | VarYVals | float | VarsOps| FuncInt
def p_paren1(subexpressions):
  '''paren : '(' eMat ')' 
  | '(' valoresMat ')'
  '''
  subexpressions[0] = toString(subexpressions)

# ---------------------------------------------------------------------------------------
# Expresiones booleanas


def p_valoresBool(subexpressions):
  '''valoresBool : BOOL
  | funcBool
  | varYVals
  | varsOps
  | '('  ternarioBool ')'
  |'''
  subexpressions[0] = toString(subexpressions)

def p_ternarioBool(subexpressions):
  '''ternarioBool : valoresBool '?' valoresTernarioBool ':' valoresTernarioBool  
  | expBool '?' valoresTernarioBool ':' valoresTernarioBool
  '''
  subexpressions[0] = toString(subexpressions)

def p_valoresTernarioBool(subexpressions):
  '''valoresTernarioBool : BOOL
  | funcBool
  | ternarioBool
  | '(' ternarioBool ')'
  | expBool
  '''
  subexpressions[0] = toString(subexpressions)
  
def p_ternario(subexpressions):
  '''ternario : ternarioMat
  | ternarioBool
  | '(' ternarioMat ')'
  | '(' ternarioBool ')'
  | ternarioVars 
  | '(' ternarioVars ')'
  '''
  subexpressions[0] = toString(subexpressions)

# Or -> Or or And | And
def p_expBool(subexpressions):
  '''expBool : expBool OR and
  | valoresBool OR and
  | expBool OR valoresBool
  | valoresBool OR valoresBool
  | and'''
  subexpressions[0] = toString(subexpressions)

# And ->  And and Eq | Eq
def p_and(subexpressions):
  '''and : and AND eq
  | valoresBool AND eq
  | and AND valoresBool
  | valoresBool AND valoresBool
  | eq'''
  subexpressions[0] = toString(subexpressions)

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
  subexpressions[0] = toString(subexpressions)

#Aca pongo que se puedan comparar los ternarios.
#Comparar dos booleanos tiene sentido para neq y eq pero no  para menor o mayor. Se podria filtrar chequeando tipos?
 
def p_tCompare(subexpressions):
  '''tCompare : eMat
  | varsOps
  | varYVals
  | INT
  | funcInt 
  | FLOAT
  | '(' ternarioBool ')' 
  | '(' ternarioMat ')' '''

  subexpressions[0] = toString(subexpressions)

# Mayor -> TCompare > TCompare | Menor
def p_mayor(subexpressions):
  '''mayor : tCompare '>' tCompare
  | menor'''
  subexpressions[0] = toString(subexpressions)

  # if len(subexpressions) > 2:
  #   tokens = [subexpressions[1], subexpressions[3]]
  #   if not chequearTipo(tokens, ["int", "float"]):
  #     raise SemanticException("Se esperaba tipo int o float")


# Menor -> TCompare < TCompare | Not 
def p_menor3(subexpressions):
  '''menor : tCompare '<' tCompare
  | not'''
  subexpressions[0] = toString(subexpressions)
  # if len(subexpressions) > 2:
  #   tokens = [subexpressions[1], subexpressions[3]]
  #   if not chequearTipo(tokens, ["int", "float"]):
  #     raise SemanticException("Se esperaba tipo int o float")
# Not ->  not Not | TBool 
def p_not(subexpressions):
  '''not :  NOT not
  | NOT valoresBool
  | parenBool'''
  subexpressions[0] = toString(subexpressions)

# TBool -> (ExpBool) | bool | VarYVals | FuncBool
def p_parenBool(subexpressions):
  '''parenBool : '(' expBool ')' '''
  subexpressions[0] = toString(subexpressions)
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


def toString(subexpressions):
  res = {}
  res["type"]=""
  res["value"]=[]
  # for exp in subexpressions[1:]:
  #   try:
  #     #print exp["value"]
  #     res["value"].append(str(exp["value"]))
  #   except TypeError:
  #     res["value"].append(str(exp))
  return res

def chequearTipo(subexps, tipos):

  for subexp in subexps:
    if subexp["type"] not in tipos:
      return False

  return True








