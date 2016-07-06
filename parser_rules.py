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

# Para guardar el tipo de las variables
variables = {}
vectores = {}

# Simbolo inicial
start = 'g'

#-----------------------------------------------------------------------------
#Sentencias y estructura general:
#-----------------------------------------------------------------------------

#g -> linea g | COMMENT g | empty 

def p_g1(subexpressions):
  '''g : linea g'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = "tabing" + subexpressions[1]["value"] 
  if(subexpressions[2]["var"] == "Sentencia"):
    subexpressions[0]["value"] += "\n" + subexpressions[2]["value"]
  subexpressions[0]["var"] = "Sentencia" 

def p_g2(subexpressions):
  '''g : COMMENT g  '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = "tabing"
  subexpressions[0]["value"] += subexpressions[1]
  subexpressions[0]["value"] += "\n"
  subexpressions[0]["value"] += subexpressions[2]["value"]
  subexpressions[0]["var"] = "" 

def p_g3(subexpressions):
  '''g : empty'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "Empty" 

#-----------------------------------------------------------------------------
#linea -> lAbierta | lCerrada

def p_linea(subexpressions):
  '''linea : lAbierta '''  
  subexpressions[0] = {}
  subexpressions[0]["value"] = ""
  subexpressions[0]["value"] += toString(subexpressions)

def p_linea1(subexpressions):
  '''linea : lCerrada'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = ""
  subexpressions[0]["value"] += toString(subexpressions)

#-----------------------------------------------------------------------------
#Linea Abierta: Hay por lo menos un IF que no matchea con un else

#lAbierta -> IF (cosaBooleana) linea
def p_lAbierta1(subexpressions):
  '''lAbierta : IF '(' cosaBooleana ')' linea '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["value"] = subexpressions[0]["value"].replace("tabing", "tabing\t")
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------
#lAbirta -> IF (cosasBooleana) {g} ELSE lAbierta

def p_lAbierta2(subexpressions):
  '''lAbierta : IF '(' cosaBooleana ')' '{' g '}' ELSE lAbierta''' 
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

#-----------------------------------------------------------------------------
#lAbirta -> IF (cosasBooleana) {g} ELSE lAbierta
def p_lAbierta3(subexpressions):
  '''lAbierta : IF '(' cosaBooleana ')' lCerrada ELSE lAbierta '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

#-----------------------------------------------------------------------------
#lAbirta -> IF (cosasBooleana) {g} 

def p_lAbierta4(subexpressions):
  '''lAbierta : IF '(' cosaBooleana ')' '{' g '}' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

#-----------------------------------------------------------------------------
#lAbirta -> loop Labierta

def p_lAbierta5(subexpressions):
  '''lAbierta : loop  lAbierta  '''
  subexpressions[0]["value"] = toString(subexpressions[:2])
  subexpressions[0]["value"] += "\ntabing"
  subexpressions[0]["value"] += toString(subexpressions[0:]).replace("tabing", "tabing\t")
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------
#Linea Cerrada: Cualquier sentencia "comun", if-else completos, loops entre llaves, etc

#lCerrada -> sentencia
def p_lCerrada1(subexpressions):
  '''lCerrada : sentencia'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = ""
  subexpressions[0]["value"] += toString(subexpressions)
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------
#lCerrada -> COMMENT com

def p_com(subexpressions):
  '''com : COMMENT com'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = "\ntabing"
  subexpressions[0]["value"] += toString(subexpressions)
  subexpressions[0]["var"] = "" 

def p_com2(subexpressions):
  '''com : empty '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = "\ntabing"
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------
#Las siguientes son las variantes de tener bloques cerrados ELSE bloques cerrados
#Un bloque cerrado puede ser una sentencia unica o un bloque entre llaves
#En cada uno de estos casos puede haber, o no, comentarios. De ahi todas estas combinaciones.

#lCerrada -> IF (cosaBooleana) {g} ELSE {g}

def p_lCerrada3(subexpressions):
  '''lCerrada : IF '(' cosaBooleana ')' '{' g '}' ELSE '{' g '}' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:6])
  subexpressions[0]["value"] += "\n"
  subexpressions[0]["value"] += toString(subexpressions[5:7]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\ntabing"
  subexpressions[0]["value"] += toString(subexpressions[6:10])
  subexpressions[0]["value"] += "\n"
  subexpressions[0]["value"] += toString(subexpressions[9:11]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\ntabing"
  subexpressions[0]["value"] += toString(subexpressions[10:])
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------

def p_lCerrada12(subexpressions):
  '''lCerrada : IF '(' cosaBooleana ')' lCerrada ELSE '{' g '}' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:5])
  subexpressions[0]["value"] += "\n"
  subexpressions[0]["value"] += toString(subexpressions[4:6]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\ntabing"
  subexpressions[0]["value"] += toString(subexpressions[5:10])
  subexpressions[0]["value"] += "\n"
  subexpressions[0]["value"] += toString(subexpressions[9:11]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\ntabing"
  subexpressions[0]["value"] += toString(subexpressions[10:])
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------

def p_lCerrada6(subexpressions):
  '''lCerrada : IF '(' cosaBooleana ')' COMMENT com lCerrada ELSE '{' g '}' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

#-----------------------------------------------------------------------------

def p_lCerrada13(subexpressions):
  '''lCerrada : IF '(' cosaBooleana ')' '{' g '}' ELSE lCerrada '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

#-----------------------------------------------------------------------------

def p_lCerrada14(subexpressions):
  '''lCerrada : IF '(' cosaBooleana ')' lCerrada ELSE lCerrada '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:5])
  subexpressions[0]["value"] += "\n"
  subexpressions[0]["value"] += toString(subexpressions[4:6]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\ntabing"
  subexpressions[0]["value"] += toString(subexpressions[5:7])
  subexpressions[0]["value"] += "\n"
  subexpressions[0]["value"] += toString(subexpressions[6:]).replace("tabing", "tabing\t")
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------

def p_lCerrada15(subexpressions):
  '''lCerrada : IF '(' cosaBooleana ')' COMMENT com lCerrada ELSE lCerrada '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

#-----------------------------------------------------------------------------

def p_lCerrada16(subexpressions):
  '''lCerrada : IF '(' cosaBooleana ')' lCerrada ELSE  COMMENT com lCerrada '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

#-----------------------------------------------------------------------------

def p_lCerrada11(subexpressions):
  '''lCerrada : IF '(' cosaBooleana ')' COMMENT com lCerrada ELSE  COMMENT com lCerrada '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

#-----------------------------------------------------------------------------

def p_lCerrada4(subexpressions):
  '''lCerrada : loop '{' g '}' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = ""
  subexpressions[0]["value"] += toString(subexpressions[:3])
  subexpressions[0]["value"] += "\n"
  subexpressions[0]["value"] += toString(subexpressions[2:4]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\n"
  subexpressions[0]["value"] += toString(subexpressions[3:])
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------

def p_lCerrada7(subexpressions):
  '''lCerrada : loop lCerrada '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = ""
  subexpressions[0]["value"] += toString(subexpressions[:2])
  subexpressions[0]["value"] += "\ntabing"
  subexpressions[0]["value"] += toString(subexpressions[1:]).replace("tabing", "tabing\t")
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------

def p_lCerrada8(subexpressions):
  '''lCerrada : loop COMMENT com lCerrada'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = ""
  subexpressions[0]["value"] += toString(subexpressions[:2])
  #COMMENT es un terminal asi que no tiene el tabbing apropiado segun el sistema este, lo agrego
  subexpressions[0]["value"] += "\n\ttabing" + subexpressions[2]
  subexpressions[0]["value"] += toString(subexpressions[2:4]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += toString(subexpressions[3:]).replace("tabing", "tabing\t")
  subexpressions[0]["var"] = ""

#-----------------------------------------------------------------------------

def p_lCerrada5(subexpressions):
  '''lCerrada : DO '{' g '}' WHILE '(' valores ')' ';' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = ""
  subexpressions[0]["value"] += toString(subexpressions[:3])
  subexpressions[0]["value"] += "\n"
  subexpressions[0]["value"] += toString(subexpressions[2:4]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\n"
  subexpressions[0]["value"] += toString(subexpressions[3:])
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------

def p_lCerrada9(subexpressions):
  '''lCerrada : DO lCerrada WHILE '(' valores ')' ';'  '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = ""
  subexpressions[0]["value"] += toString(subexpressions[:2])
  subexpressions[0]["value"] += "\n\t"
  subexpressions[0]["value"] += toString(subexpressions[1:3]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\n"
  subexpressions[0]["value"] += toString(subexpressions[2:])
  subexpressions[0]["var"] = "" 

#----------------------------------------------------------------------------- 

def p_lCerrada10(subexpressions):
  '''lCerrada :  DO COMMENT com lCerrada WHILE '(' valores ')' ';'  '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = ""
  subexpressions[0]["value"] += toString(subexpressions[:2])
  subexpressions[0]["value"] += "\n\ttabing" + subexpressions[2]
  subexpressions[0]["value"] += toString(subexpressions[2:4]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\n"
  subexpressions[0]["value"] += toString(subexpressions[4:])
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------
#Sentencias basicas
#-----------------------------------------------------------------------------

#sentencia -> varsOps | func ; | varAsig ; | RETURN; | ;

def p_sentencia1(subexpressions):
  '''sentencia : varsOps  ';' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------

def p_sentencia2(subexpressions):
  '''sentencia : func ';' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------

def p_sentencia3(subexpressions):
  '''sentencia : varAsig ';' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------

def p_sentencia4(subexpressions):
  '''sentencia : RETURN ';' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------

def p_sentencia5(subexpressions):
  '''sentencia : ';' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------
#Loop headers
#-----------------------------------------------------------------------------

#loop -> WHILE (valores) | FOR (primerParam ; valores ; tercerParam)

def p_loop1(subexpressions):
  '''loop : WHILE '(' valores ')' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = ""
  subexpressions[0]["value"] += toString(subexpressions)
  subexpressions[0]["var"] = "" 
  chequearTipo([subexpressions[3]],["bool"],". La guarda debe ser un booleano")

#-----------------------------------------------------------------------------

def p_loop3(subexpressions):
  '''loop : FOR '(' primParam ';' valores ';' tercerParam ')' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 
  chequearTipo([subexpressions[5]],["bool"],". El segundo parametro debe ser un booleano")

#en el tercer parametro del for esta varOps, pero en realidad puede ser mas general(!)
#-----------------------------------------------------------------------------

def p_primParam(subexpressions):
  '''primParam : varAsig
  | empty'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 


def p_tercerParam(subexpressions):
  '''tercerParam : varsOps
  | varAsig
  | func
  | empty'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 


def p_cosaBooleana(subexpressions):
  '''cosaBooleana : expBool
  | valoresBool'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------
#Funciones
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# func -> FuncReturn | FuncVoid

def p_func1(subexpressions):
  '''func : funcReturn'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 

def p_func2(subexpressions):
  '''func : funcVoid'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------
# funcReturn -> FuncInt | FuncString | FuncBool

def p_funcReturn(subexpressions):
  '''funcReturn : funcInt
  | funcString
  | funcBool'''
  subexpressions[0] = {}
  subexpressions[0]["value"] =  toString(subexpressions)
  subexpressions[0]["type"] = subexpressions[1]["type"] 

#-----------------------------------------------------------------------------
#funcInt -> MULTIESCALAR( valores, valores param)

def p_funcInt1(subexpressions):
  '''funcInt : MULTIESCALAR '(' valores ',' valores   param ')' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = "vec"
  subexpressions[0]["elems"] = subexpressions[3].get("elems")
  chequearTipo([subexpressions[3]],["vec"])
  #Aca quiero chequear que sea numerico, pero me tirar error
  #chequearTipo([subexpressions[3].get("elems")],["int","float"],"se esperaba vector numerico")
  chequearTipo([subexpressions[5]],["int"])
  if(subexpressions[6]["type"] != ""):
    chequearTipo([subexpressions[6]],["bool"])

#-----------------------------------------------------------------------------
#funcInt -> LENGTH( valores)

def p_funcInt2(subexpressions):
  '''funcInt : LENGTH '(' valores ')' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = "int"
  chequearTipo([subexpressions[3]],["string","vec"])

#-----------------------------------------------------------------------------
#funcString -> CAPIALIZAR(valores)

def p_funcString(subexpressions):
  '''funcString : CAPITALIZAR '(' valores ')' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = "string"
  chequearTipo([subexpressions[3]], ["string"])

#-----------------------------------------------------------------------------
# FuncBool -> colineales(valores,valores )

def p_funcBool(subexpressions):
  '''funcBool : COLINEALES '(' valores ',' valores ')' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = "bool"
  subexpressions[0]["var"] = "" 
  chequearTipo([subexpressions[3],subexpressions[5]], ["vec"])  

#-----------------------------------------------------------------------------
# FuncVoid -> print(Valores) 

def p_funcVoid(subexpressions):
  '''funcVoid : PRINT '(' valores ')' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------
#Parametros de las funciones:
#-----------------------------------------------------------------------------

def p_param1(subexpressions):
  '''param : ',' valores'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 
  subexpressions[0]["type"] = subexpressions[2]["type"]


def p_param2(subexpressions):
  '''param : empty'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 
  subexpressions[0]["type"] = "" 

def p_empty(subexpressions):
  '''empty : '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 


#-----------------------------------------------------------------------------
#Vectores  y variables
#-----------------------------------------------------------------------------


def p_vec(subexpressions):
  '''vec : '[' elem ']' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = "vec"
  subexpressions[0]["elems"] = subexpressions[2]["elems"]

#Elem-> Valores, Elem | Valores
def p_elem(subexpressions):
  '''elem : valores ',' elem
  | valores'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = subexpressions[1]["type"]

  if len(subexpressions) == 2:
    subexpressions[0]["elems"] = [subexpressions[1]["type"]]
  else:
    subexpressions[0]["elems"] = subexpressions[3]["elems"]

  tipoElem = subexpressions[1]["type"]
  subexpressions[0]["elems"].insert(1, tipoElem)

#VecVal ->  var M

def p_vecVal(subexpressions):
  '''vecVal : ID '[' expresion ']'
  | vec '[' expresion ']'
  | vecVal '[' expresion ']'
  '''
  chequearAccesoVector(subexpressions)

  # a. Si el indice es una expresion, no se puede chequear en tiempo de compilacion
  # b. Si el indice es una variable y se le asigno una expresion, idem a.
  # c. Si no pasa a. ni b. entonces en el indice tengo un numero, pero tengo que saber si en el
  # indice hay un valor o una expresion
  # if valorIndice[ "hay una expresion?" ] == true
  #   tipoElemento = vectores[nombreVar1]["elems"][int(valorIndice["value"])]
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = subexpressions[1]["var"]
  subexpressions[0]["type"] = "int"
  subexpressions[0]["elems"] = []

def p_vecVal2(subexpressions):
  '''vecVal : ID '[' INT ']'
  | vec '[' INT ']'
  | vecVal '[' INT ']'
  '''
  chequearAccesoVector(subexpressions)

  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  variableVector = subexpressions[1]["var"]
  
  indice = int(subexpressions[3]["value"])
  elementosVector = vectores[variableVector]["elems"]
  tipoElemento = elementosVector[indice]

  subexpressions[0]["type"] = tipoElemento
  subexpressions[0]["elems"] = []
  subexpressions[0]["var"] = ""

def p_expresion(subexpressions):
  '''expresion : eMat
  | expBool
  | funcReturn
  | reg
  | FLOAT
  | STRING
  | BOOL
  | varYVals
  | varsOps
  | vec
  | ternario
  | atributos
  | RES
  '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

  if subexpressions[1]["type"] in ["vec", "var"]:
    nombreVariable = subexpressions[1]["var"]
    subexpressions[0]["var"] = nombreVariable
    tipo = variables[nombreVariable]["type"]
    if subexpressions[1]["type"] == "vec":
      subexpressions[0]["elems"] = subexpressions[1]["elems"]
  else:
    tipo = subexpressions[1]["type"]

  subexpressions[0]["type"] = tipo

def p_valores(subexpressions):
  '''valores : varYVals
  | varsOps
  '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

  nombreVariable = subexpressions[1]["var"]
  subexpressions[0]["var"] = nombreVariable

  if nombreVariable == "":
    tipo = ""
  else:
    tipo = variables[nombreVariable]["type"]

  subexpressions[0]["type"] = tipo

def p_valores2(subexpressions):
  '''valores : eMat
  | expBool
  | funcReturn
  | reg
  | INT
  | FLOAT
  | STRING
  | BOOL
  | ternario
  | atributos
  | vec
  | RES'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = subexpressions[1]["type"]
  if subexpressions[1]["type"] == "vec":
      subexpressions[0]["elems"] = subexpressions[1].get("elems")

def p_atributos(subexpressions):
  '''atributos : ID '.' valoresCampos
  | reg '.' valoresCampos '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 
  subexpressions[0]["type"] = "falta" 

def p_valoresCampos(subexpressions):
  '''valoresCampos : varYVals
  | END
  | BEGIN'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 


#--------------------------------------------------------------------------------------
# Operadores ternarios
  
def p_ternario(subexpressions):
  '''ternario : ternarioMat
  | ternarioBool
  | '(' ternarioMat ')'
  | '(' ternarioBool ')'
  | ternarioVars 
  | '(' ternarioVars ')'
  '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 
  if len(subexpressions) == 2:
    subexpressions[0]["type"] = subexpressions[1]["type"]
  else:
    subexpressions[0]["type"] = subexpressions[2]["type"]

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
  chequeadorTernario(subexpressions)
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = subexpressions[3]["type"]

def p_valoresTernarioVars1(subexpressions):
  '''valoresTernarioVars : reg
  | vec
  | ternarioVars
  | '(' ternarioVars ')'
  | atributos
  '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 
  if len(subexpressions) == 2:
    subexpressions[0]["type"] = subexpressions[1]["type"]
  else:
    subexpressions[0]["type"] = subexpressions[2]["type"]

def p_valoresTernarioVars2(subexpressions):
  '''valoresTernarioVars : varsOps
  | varYVals
  | res'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  nombreVar = subexpressions[1]["var"]
  subexpressions[0]["var"] = nombreVar
  subexpressions[0]["type"] = variables[nombreVar]["type"]

def p_res(subexpressions):
  '''res : RES'''
  subexpressions[0]["var"] = "res"

def p_ternarioMat(subexpressions):
  '''ternarioMat : valoresBool '?' valoresTernarioMat ':' valoresTernarioMat  
  | expBool '?' valoresTernarioMat ':' valoresTernarioMat
  '''
  chequeadorTernario(subexpressions)
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  if (subexpressions[3], subexpressions[5]) in [("int", "float"), ("float", "int")]:
    subexpressions[0]["type"] = "float"
  else:
    subexpressions[0] = subexpressions[3]

def p_valoresTernarioMat(subexpressions):
  '''valoresTernarioMat : INT
  | FLOAT
  | funcInt
  | STRING
  | eMat
  | ternarioMat
  | '(' ternarioMat ')' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  if len(subexpressions) == 2:
    subexpressions[0]["type"] = subexpressions[1]["type"]
  else:
    subexpressions[0]["type"] = subexpressions[2]["type"]

def p_ternarioBool(subexpressions):
  '''ternarioBool : valoresBool '?' valoresTernarioBool ':' valoresTernarioBool  
  | expBool '?' valoresTernarioBool ':' valoresTernarioBool
  '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = "bool"
  chequeadorTernario(subexpressions)

def p_valoresTernarioBool(subexpressions):
  '''valoresTernarioBool : BOOL
  | funcBool
  | ternarioBool
  | '(' ternarioBool ')'
  | expBool
  '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = "bool"

#-----------------------------------------------------------------------------------------

#VarYVals -> var | VecVal
def p_varYVals1(subexpressions):
  '''varYVals : ID '''
  global variables
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = subexpressions[1]["var"]
  nombreVar = subexpressions[1]["var"]
  variable = variables.get(nombreVar, subexpressions[1])
  subexpressions[0]["type"] = variable["type"]

def p_varYVals2(subexpressions):
  '''varYVals : vecVal
  | vecVal '.' varYVals
  '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  # Falta agregar los registros
  if len(subexpressions) == 4:
    subexpressions[0]["type"] = "falta tipar"
  else:
    subexpressions[0]["type"] = subexpressions[1]["type"]
    subexpressions[0]["elems"] = subexpressions[1]["elems"]

  subexpressions[0]["var"] = subexpressions[1]["var"]

#Registros:
#Reg -> {U}
def p_reg(subexpressions):
  '''reg :  '{' campos '}' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = "reg"

#U -> campo: Valores, U | campof: Valores
#campo no es nada en la gramatica, pero creo que en realidad es cualquier string(!)
#Me parece que mejore el campo es un ID (!)
def p_campos1(subexpressions):
  '''campos : ID ':' valores ',' campos'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
def p_campos2(subexpressions):
  '''campos : ID ':' valores'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

#-----------------------------------------------------------------------------
#Operadores de variables:
#VarsOps -> --SMM | ++SMM | SMM
def p_varsOps1(subexpressions):
  '''varsOps : MENOSMENOS varYVals 
  | MASMAS varYVals '''
  nombreVar = subexpressions[2]["var"]
  if variables[nombreVar]["type"] not in ["int", "float"]:
    raise Exception("El operador ++ tiene que recibir variable de tipo float o int")
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  nombreVar = subexpressions[2]["var"]
  subexpressions[0]["type"] = variables[nombreVar]["type"]
  subexpressions[0]["var"] = subexpressions[2]["var"]

def p_varsOps2(subexpressions):
  '''varsOps : varYVals MASMAS 
  | varYVals MENOSMENOS'''
  nombreVar = subexpressions[1]["var"]
  if variables[nombreVar]["type"] not in ["int", "float"]:
    raise Exception("El operador ++ solo se puede usar con variables de tipo float o int")

  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = subexpressions[1]["type"]
  subexpressions[0]["var"] = subexpressions[1]["var"]
  
#-----------------------------------------------------------------------------
#Asignaciones:

#Dejo las asignaciones no ambiguas como estaban antes
#Aca pongo varYvals por este caso g[a] = b;

def p_varAsig(subexpressions):
  '''varAsig : varYVals MULEQ valores
  | varYVals DIVEQ valores
  | varYVals MASEQ valores
  | varYVals MENOSEQ valores
  | varYVals '=' valores
  | ID '.' ID '=' valores'''
  global variables, vectores

  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = subexpressions[3]["type"] 

  # Si es un vector tengo que obtener el tipo de sus elementos y asignarle a elems de varYVals
  if subexpressions[3]["type"] == "vec":
    nombreVec = subexpressions[1]["var"]
    vectores[nombreVec] = {}
    vectores[nombreVec]["elems"] = subexpressions[3]["elems"]
    subexpressions[0]["elems"] = subexpressions[3]["elems"] 

  nombreVar = subexpressions[1]["var"]
  variables[nombreVar] = {}
  variables[nombreVar]["type"] = subexpressions[3]["type"] 

#-----------------------------------------------------------------------------
#Operaciones binarias enteras

# Coloco string aqui, luego chequeamos tipos para cuando se use
# las operaciones solo para INT

#ACa agrego tambien la funcionString, habria que hacer chequeos despues...

def p_valoresMat1(subexpressions):
  '''valoresMat : INT
  | FLOAT
  | funcInt
  | atributos
  | funcString
  | STRING
  '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = subexpressions[1]["type"]

def p_valoresMat2(subexpressions):
  '''valoresMat : varYVals
  | varsOps
  '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  if subexpressions[1]["type"] in ["var", "vec"]:
    nombreVar = subexpressions[1]["var"]
    subexpressions[0]["type"] = variables[nombreVar]["type"]
  else:
    subexpressions[0]["type"] = subexpressions[1]["type"]

def p_valoresMat3(subexpressions):
  '''valoresMat : '(' ternarioMat ')' ''' 
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = subexpressions[2]["type"]


#EMat -> EMat '+' P | EMat - P | P
def p_eMat1(subexpressions):
    '''eMat : eMat '+' p
    | valoresMat '+' p
    | eMat '+' valoresMat
    | valoresMat '+' valoresMat
    | p'''
    chequeadorSuma(subexpressions)
    chequearUnicoTerminal(subexpressions, ["int", "float"] )
    subexpressions[0] = {}
    subexpressions[0]["value"] = toString(subexpressions)

    if len(subexpressions) == 4:
        if subexpressions[3]["type"] == "string":
          subexpressions[0]["type"] = "string"
        else:
          if (subexpressions[1], subexpressions[3]) == ("int", "int"):
            subexpressions[0]["type"] = "int"
          else:
            subexpressions[0]["type"] = "float"

    if len(subexpressions) == 2:
        subexpressions[0]["type"] = subexpressions[1]["type"]
    

def p_eMat2(subexpressions):
  '''eMat : eMat '-' p
  | valoresMat '-' p
  | eMat '-' valoresMat
  | valoresMat '-' valoresMat
  '''
  chequeadorBinario(subexpressions, ["int", "float"])
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

  if (subexpressions[1], subexpressions[3]) == ("int", "int"):
    subexpressions[0]["type"] = "int"
  else:
    subexpressions[0]["type"] = "float"
    
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
    chequearUnicoTerminal(subexpressions, ["int", "float"] )
    chequeadorBinario(subexpressions, ["int", "float"])
    subexpressions[0] = {}
    subexpressions[0]["value"] = toString(subexpressions)
    subexpressions[0]["type"] = "float"

    if len(subexpressions) == 4:
      if (subexpressions[1], subexpressions[3]) == ("int", "int"):
        subexpressions[0]["type"] = "int"
      else:
        subexpressions[0]["type"] = "float"
    else:
        subexpressions[0]["type"] = subexpressions[1]["type"]

#Exp -> Exp ^ ISing | ISing
def p_exp(subexpressions):
  '''exp : exp '^' iSing
  | valoresMat '^' iSing
  | exp '^' valoresMat
  | valoresMat '^' valoresMat
  | iSing'''
  chequearUnicoTerminal(subexpressions, ["int", "float"] )
  chequeadorBinario(subexpressions, ["int", "float"])
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = "float"

  if len(subexpressions) == 4:
    if (subexpressions[1], subexpressions[3]) == ("int", "int"):
      subexpressions[0]["type"] = "int"
    else:
      subexpressions[0]["type"] = "float"
  else:
    subexpressions[0]["type"] = subexpressions[1]["type"]

#ISing -> -Paren | '+'Paren | Paren
def p_iSing(subexpressions):
  '''iSing : '-' paren
  | '+' paren
  | '-' valoresMat
  | '+' valoresMat
  | paren
  '''
  chequearUnicoTerminal(subexpressions, ["int", "float"] )
  chequeadorUnarioPrefijo(subexpressions, ["int", "float"])
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  if len(subexpressions) == 3:
    subexpressions[0]["type"] = subexpressions[2]["type"]
  else:
    subexpressions[0]["type"] = subexpressions[1]["type"]

#Paren -> (EMat) | int | VarYVals | float | VarsOps| FuncInt
def p_paren1(subexpressions):
  '''paren : '(' eMat ')' 
  | '(' valoresMat ')'
  '''
  chequearTipo([subexpressions[2]], ["int", "float"])
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = subexpressions[2]["type"]

# ---------------------------------------------------------------------------------------
# Expresiones booleanas


def p_valoresBool(subexpressions):
  '''valoresBool : BOOL
  | funcBool
  | varYVals
  | varsOps
  '''
  chequearUnicoTerminal(subexpressions, ["bool"])
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = subexpressions[1]["type"]

def p_valoresBool1(subexpressions):
  '''valoresBool : '('  ternarioBool ')' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = subexpressions[2]["type"]  

def p_valoresBool2(subexpressions):
  '''valoresBool : '''
  subexpressions[0] = {}
  subexpressions[0]["type"] = ""
  subexpressions[0]["value"] = ""

# Or -> Or or And | And
def p_expBool(subexpressions):
  '''expBool : expBool OR and
  | valoresBool OR and
  | expBool OR valoresBool
  | valoresBool OR valoresBool
  | and'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["type"] = "bool"

# And ->  And and Eq | Eq
def p_and(subexpressions):
  '''and : and AND eq
  | valoresBool AND eq
  | and AND valoresBool
  | valoresBool AND valoresBool
  | eq'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

# Eq -> Eq == TBool |  Eq != TBool | Mayor 
def p_eq(subexpressions):
  '''eq : eq EQEQ mayor
  | eq DISTINTO mayor
  | tCompareEQ EQEQ mayor
  | tCompareEQ DISTINTO mayor
  | eq EQEQ tCompareEQ
  | eq DISTINTO tCompareEQ
  | tCompareEQ EQEQ tCompareEQ
  | tCompareEQ DISTINTO tCompareEQ
  | mayor'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

#Aca pongo que se puedan comparar los ternarios.
#Comparar dos booleanos tiene sentido para neq y eq pero no  para menor o mayor. Se podria filtrar chequeando tipos?
# Para comparar booleanos por igualdad
def p_tCompareEQ(subexpressions):
  '''tCompareEQ : BOOL
  | funcBool
  | varYVals
  | varsOps
  | INT
  | FLOAT
  | funcInt
  | eMat
  | '(' ternarioBool ')' 
  | '(' ternarioMat ')'
  '''

def p_tCompare(subexpressions):
  '''tCompare : eMat
  | varsOps
  | varYVals
  | INT
  | funcInt 
  | FLOAT
  | '(' ternarioMat ')' '''
  print subexpressions[1]
  chequearUnicoTerminal(subexpressions, ["int", "float"])
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

# Mayor -> TCompare > TCompare | Menor
def p_mayor(subexpressions):
  '''mayor : tCompare '>' tCompare
  | menor'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = ""
  # if len(subexpressions) > 2:
  #   tokens = [subexpressions[1], subexpressions[3]]
  #   if not chequearTipo(tokens, ["int", "float"]):
  #     raise SemanticException("Se esperaba tipo int o float")


# Menor -> TCompare < TCompare | Not 
def p_menor3(subexpressions):
  '''menor : tCompare '<' tCompare
  | not'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 
  # if len(subexpressions) > 2:
  #   tokens = [subexpressions[1], subexpressions[3]]
  #   if not chequearTipo(tokens, ["int", "float"]):
  #     raise SemanticException("Se esperaba tipo int o float")
# Not ->  not Not | TBool 
def p_not(subexpressions):
  '''not :  NOT not
  | NOT valoresBool
  | parenBool'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 


# TBool -> (ExpBool) | bool | VarYVals | FuncBool
def p_parenBool(subexpressions):
  '''parenBool : '(' expBool ')' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["var"] = "" 

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


def toString(subexpressions):
  res = ""
  for exp in subexpressions[1:]:
    try:
      res += str(exp["value"])
    except TypeError:
      res += str(exp)
  return res

# chequea si todos los elementos de la lista de subexpresiones son de 
# algun tipo de la lista tipos
# Ademas en caso de fallar se levanta una excepcion con el tipo esperado
# Se le puede pasar un mensaje adicional como tercer parametro, esto se usa para los chequeaodores
# de operadores
def chequearTipo(subexps, tipos, aditionalMessage=""):

    for subexp in subexps:
        if subexp["type"] not in tipos:
            message = "Se esperaba tipo "
            message += listTypes(tipos)
            message += aditionalMessage
            raise Exception(message)

    pass

def listTypes(tipos):
    if len(tipos) == 1:
        return tipos[0]

    if len(tipos) == 2:
        return tipos[0] + " o " + tipos[1]

    message = tipos[0]
    for i in range(1, len(tipos)-1):
        message += ", " + tipos[i]

    message += " o " + tipos[len(tipos)-1]
    return message

# Por cada operador (binario, unario, ternario) hay un chequeador de tipos
# Pueden usarlo sin importar si hay otro tipo de operador en la misma regla
# Cada una chequea que sea su tipo de operador el de la expresion,
# comparando la longitud de la lista
# Si hay otro operador con la misma cantidad de elementos y no es de estos tipos hay que tener
# cuidado
# Cada chequeador, en caso de falla, levanta una excepcion con los tipos esperados
# y ademas el tipo que se encontro en los operadores
def chequeadorBinario(subexpressions, tipos):
    if len(subexpressions) == 4:
        subexps = [ subexpressions[1], subexpressions[3] ]
        aditionalMessage = "\n" + subexpressions[1]["value"] + "   " + subexpressions[2] + "   " + subexpressions[3]["value"]
        aditionalMessage += "\n en operador " + subexpressions[2]
        aditionalMessage += "\n se encontro tipos: " + subexpressions[1]["type"] + " y "+ subexpressions[3]["type"]
        chequearTipo(subexps, tipos, aditionalMessage)
    pass

def chequeadorUnarioPrefijo(subexpressions, tipos):
    if len(subexpressions) == 3:
        subexps = [ subexpressions[2] ]
        aditionalMessage = "\n en operador " + subexpressions[1]
        aditionalMessage += "\n se encontro tipo: " + subexpressions[2]["type"]
        chequearTipo(subexps, tipos, aditionalMessage)
    pass

def chequeadorUnarioPostfijo(subexpressions, tipos):
    if len(subexpressions) == 3:
        subexps = [ subexpressions[1] ]
        aditionalMessage = "\n en operador " + subexpressions[2]
        aditionalMessage += "\n se encontro tipo: " + subexpressions[1]["type"]
        chequearTipo(subexps, tipos, aditionalMessage)
    pass

def chequeadorTernario(subexpressions):
    if len(subexpressions) == 6:

        if subexpressions[1]["type"] != "bool":
            message = "La condicion del operador ? tiene que ser de tipo Bool"
            message += "\n se encontro tipo " + subexpressions[1]["type"]
            print message
            #raise Exception(message)

        if (subexpressions[3]["type"], subexpressions[5]["type"]) in [("int", "float"),  ("float", "int")]:
            return

        if subexpressions[3]["type"] != subexpressions[5]["type"]:
            message = "Los valores de retorno del operador ? tiene que ser del mismo tipo"
            message += "\n se encontro tipos " + subexpressions[3]["type"] + " y " + subexpressions[5]["type"]
            print message
            #raise Exception(message)

def chequeadorSuma(subexpressions):
  if len(subexpressions) == 4:
    if subexpressions[1]["type"] == "string" and subexpressions[3]["type"] == "string":
      return

    chequeadorBinario(subexpressions, ["float", "int"])

  pass

def chequearUnicoTerminal(subexpressions, tipos):
    if len(subexpressions) == 2:
        subexps = [ subexpressions[1] ]
        if subexpressions[1]["type"] == "noType":
          message = '''\n variable "''' + subexpressions[1]["var"] + '''" no inicializada'''
          raise Exception(message)

        chequearTipo(subexps, tipos)

def chequearAccesoVector(subexpressions):
  global vectores, variables
  nombreVar1 = subexpressions[1]["var"]
  tipoVariable1 = variables[nombreVar1]["type"]

  if tipoVariable1 != "vec" and tipoVariable1 != "":
    raise Exception("El operador [i] solo se puede usar con variables de tipo vector")

  if subexpressions[3]["type"] == "var":
    nombreVar2 = subexpressions[3]["var"]
    tipoVariable2 = variables[nombreVar2]["type"]
  else:
    tipoVariable2 = subexpressions[3]["type"]

  if tipoVariable2 != "int" and tipoVariable2 != "":
    raise Exception("El indice de un vector solo se puede ser de tipo int") 