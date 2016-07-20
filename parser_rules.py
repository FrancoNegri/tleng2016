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
registros = {}
variablesVector = {}

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
  subexpressions[0]["var"] = "Sentencia" 

def p_g3(subexpressions):
  '''g : empty'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = ""
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
  subexpressions[0]["value"] = toString(subexpressions[:5])
  subexpressions[0]["value"] += toStringLineaAbierta(subexpressions[5])
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------

#AGREGO NUEVA PRODUCCION!! para el caso que faltaba...

#lAbierta -> IF (cosaBooleana) COMMENT com linea
def p_lAbierta1p(subexpressions):
  '''lAbierta : IF '(' cosaBooleana ')' COMMENT com linea '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:5])
  subexpressions[0]["value"] += "\n\ttabing" + subexpressions[5]
  subexpressions[0]["value"] += toString(subexpressions[5:7]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += toStringLineaAbierta(subexpressions[7])
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------
#lAbirta -> IF (cosasBooleana) {g} ELSE lAbierta

def p_lAbierta2(subexpressions):
  '''lAbierta : IF '(' cosaBooleana ')' '{' g '}' ELSE lAbierta''' 
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:5])+ subexpressions[5] 
  subexpressions[0]["value"] += "\n" + toString(subexpressions[5:7]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\ntabing" + toString(subexpressions[6:9])
  subexpressions[0]["value"] += toStringLineaAbierta(subexpressions[9])

def toStringLineaAbierta(subexpression):
  return "\n\ttabing" + subexpression["value"].replace("tabing", "tabing\t")

#-----------------------------------------------------------------------------
#AGREGO NUEVA PRODUCCION!!!
#lAbirta -> IF (cosasBooleana) COMMENT com lCerrada ELSE lAbierta
def p_lAbierta3(subexpressions):
  '''lAbierta : IF '(' cosaBooleana ')' COMMENT com lCerrada ELSE lAbierta '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:5])
  subexpressions[0]["value"] += toStringTerminal(subexpressions[5]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += toString(subexpressions[5:7]).replace("tabing", "tabing\t") + "\n"
  subexpressions[0]["value"] += toStringLineaCerrada(subexpressions[7])
  subexpressions[0]["value"] += toStringTerminal(subexpressions[8]["value"]) + "\n"
  subexpressions[0]["value"] += toStringLineaCerrada(subexpressions[9])

#-----------------------------------------------------------------------------
#AGREGO NUEVA PRODUCCION!!!
#lAbirta -> IF (cosasBooleana) COMMENT com lCerrada ELSE COMMENT com lAbierta
def p_lAbierta4(subexpressions):
  '''lAbierta : IF '(' cosaBooleana ')' COMMENT com lCerrada ELSE COMMENT com lAbierta '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:5])
  subexpressions[0]["value"] += toStringTerminal(subexpressions[5]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += toString(subexpressions[5:7]).replace("tabing", "tabing\t") + "\n"
  subexpressions[0]["value"] += toStringLineaCerrada(subexpressions[7])
  subexpressions[0]["value"] += toStringTerminal(subexpressions[8]["value"])
  subexpressions[0]["value"] += toStringTerminal(subexpressions[9]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += toString(subexpressions[9:11]).replace("tabing", "tabing\t") + "\n"
  subexpressions[0]["value"] += toStringLineaCerrada(subexpressions[11])

#-----------------------------------------------------------------------------

#lAbirta -> IF (cosasBooleana) lCerrada ELSE lAbierta
def p_lAbierta5(subexpressions):
  '''lAbierta : IF '(' cosaBooleana ')' lCerrada ELSE lAbierta '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:5])
  subexpressions[0]["value"] += toStringLineaCerrada(subexpressions[5])
  subexpressions[0]["value"] += "\ntabing" + toString(subexpressions[5:7])
  subexpressions[0]["value"] += toStringLineaAbierta(subexpressions[7])

#-----------------------------------------------------------------------------
#AGREGO NUEVA PRODUCCION!!!
#lAbirta -> IF (cosasBooleana) lCerrada ELSE  COMMENT com  lAbierta
def p_lAbierta6(subexpressions):
  '''lAbierta : IF '(' cosaBooleana ')' lCerrada ELSE COMMENT com lAbierta '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:5]) + "\n"
  subexpressions[0]["value"] += toStringLineaCerrada(subexpressions[5]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += toStringTerminal(subexpressions[6]["value"])
  subexpressions[0]["value"] += toStringTerminal(subexpressions[7]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += toString(subexpressions[7:9]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += toStringLineaAbierta(subexpressions[9])


#-----------------------------------------------------------------------------

#lAbirta -> IF (cosasBooleana) {g} 

def p_lAbierta7(subexpressions):
  '''lAbierta : IF '(' cosaBooleana ')' '{' g '}' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:5]) + subexpressions[5] 
  subexpressions[0]["value"] += "\n" + toString(subexpressions[5:7]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\ntabing" + toString(subexpressions[6:])


#-----------------------------------------------------------------------------
#lAbirta -> loop Labierta

def p_lAbierta8(subexpressions):
  '''lAbierta : loop  lAbierta  '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:2])
  subexpressions[0]["value"] += toStringLineaAbierta(subexpressions[2])
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------
#Linea Cerrada: Cualquier sentencia "comun", if-else completos, loops entre llaves, etc

#lCerrada -> sentencia
def p_lCerrada1(subexpressions):
  '''lCerrada : sentencia'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
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
  subexpressions[0]["value"] = ""
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------
#Las siguientes son las variantes de tener bloques cerrados ELSE bloques cerrados
#Un bloque cerrado puede ser una sentencia unica o un bloque entre llaves
#En cada uno de estos casos puede haber, o no, comentarios. De ahi todas estas combinaciones.

#lCerrada -> IF (cosaBooleana) {g} ELSE {g}

def p_lCerrada3(subexpressions):
  '''lCerrada : IF '(' cosaBooleana ')' '{' g '}' ELSE '{' g '}' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:5]) + subexpressions[5]
  subexpressions[0]["value"] += "\n"
  subexpressions[0]["value"] += toString(subexpressions[5:7]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\ntabing"
  subexpressions[0]["value"] += toString(subexpressions[6:9]) + subexpressions[9]
  subexpressions[0]["value"] += "\n"
  subexpressions[0]["value"] += toString(subexpressions[9:11]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += toStringTerminal(subexpressions[11])
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------

def p_lCerrada12(subexpressions):
  '''lCerrada : IF '(' cosaBooleana ')' lCerrada ELSE '{' g '}' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:5])
  subexpressions[0]["value"] += "\n"
  subexpressions[0]["value"] += toStringLineaCerrada(subexpressions[5])
  subexpressions[0]["value"] += toStringTerminal(subexpressions[6]["value"]) + subexpressions[7] + "\n"
  subexpressions[0]["value"] += toString(subexpressions[7:9]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += toStringTerminal(subexpressions[9])
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------

def p_lCerrada6(subexpressions):
  '''lCerrada : IF '(' cosaBooleana ')' COMMENT com lCerrada ELSE '{' g '}' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:5])
  subexpressions[0]["value"] += "\n\ttabing" + subexpressions[5] + "\n"
  subexpressions[0]["value"] += toString(subexpressions[5:7]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += toStringLineaCerrada(subexpressions[7])
  subexpressions[0]["value"] += "\ntabing" + subexpressions[8] + " " + subexpressions[9]
  subexpressions[0]["value"] += toString(subexpressions[9:11]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\ntabing" + subexpressions[11]

#-----------------------------------------------------------------------------

def p_lCerrada13(subexpressions):
  '''lCerrada : IF '(' cosaBooleana ')' '{' g '}' ELSE lCerrada '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:5]) + subexpressions[5] + "\n"
  subexpressions[0]["value"] += toString(subexpressions[5:7]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\ntabing" + toString(subexpressions[6:9])
  subexpressions[0]["value"] += "\n" + toStringLineaCerrada(subexpressions[9])

#-----------------------------------------------------------------------------

#ESTA FALTABA!!!

#-----------------------------------------------------------------------------

def p_lCerrada13p(subexpressions):
  '''lCerrada : IF '(' cosaBooleana ')' '{' g '}' ELSE COMMENT com lCerrada '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:5]) + subexpressions[5] + "\n"
  subexpressions[0]["value"] += toString(subexpressions[4:6]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\n" + toString(subexpressions[5:7]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\ntabing" + toString(subexpressions[6:9]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\n\ttabing" + toString(subexpressions[8:11]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\n" + toStringLineaCerrada(subexpressions[11])

#-----------------------------------------------------------------------------

def p_lCerrada14(subexpressions):
  '''lCerrada : IF '(' cosaBooleana ')' lCerrada ELSE lCerrada '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:5])
  subexpressions[0]["value"] += "\n" + toStringLineaCerrada(subexpressions[5])
  subexpressions[0]["value"] += "\ntabing"
  subexpressions[0]["value"] += toString(subexpressions[5:7]) + "\n"
  subexpressions[0]["value"] += toStringLineaCerrada(subexpressions[7])
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------

def p_lCerrada15(subexpressions):
  '''lCerrada : IF '(' cosaBooleana ')' COMMENT com lCerrada ELSE lCerrada '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:5])
  subexpressions[0]["value"] += "\n\ttabing" + subexpressions[5]
  subexpressions[0]["value"] += toString(subexpressions[5:7]).replace("tabing", "tabing\t") + "\n"
  subexpressions[0]["value"] += toStringLineaCerrada(subexpressions[7])
  subexpressions[0]["value"] += "\ntabing" + toString(subexpressions[7:9]) + "\n"
  subexpressions[0]["value"] += toStringLineaCerrada(subexpressions[9])
  subexpressions[0]["var"] = "" 

def toStringLineaCerrada(subexpression):
  return "\ttabing" + subexpression["value"].replace("tabing", "tabing\t")
def toStringTerminal(subexpression):
  try:
    return "\ntabing" + subexpression
  except TypeError:
    return "\ntabing" + subexpression["value"]

#-----------------------------------------------------------------------------

def p_lCerrada16(subexpressions):
  '''lCerrada : IF '(' cosaBooleana ')' lCerrada ELSE  COMMENT com lCerrada '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:5])
  subexpressions[0]["value"] += "\n" + toStringLineaCerrada(subexpressions[5])
  subexpressions[0]["value"] += "\ntabing" + subexpressions[6] + "\ntabing" + subexpressions[7]
  subexpressions[0]["value"] += "\ntabing" + toString(subexpressions[6:9]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += toStringLineaCerrada(subexpressions[9])
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------

def p_lCerrada11(subexpressions):
  '''lCerrada : IF '(' cosaBooleana ')' COMMENT com lCerrada ELSE COMMENT com lCerrada '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions[:5])
  subexpressions[0]["value"] += "\n\ttabing" + subexpressions[5]
  subexpressions[0]["value"] += toString(subexpressions[5:7]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += toStringLineaCerrada(subexpressions[7])
  subexpressions[0]["value"] += "\ntabing" + subexpressions[8]["value"] + "\n\ttabing" + subexpressions[9] + "\n"
  subexpressions[0]["value"] += toString(subexpressions[9:11]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += toStringLineaCerrada(subexpressions[11])
  subexpressions[0]["var"] = "" 
#-----------------------------------------------------------------------------

def p_lCerrada4(subexpressions):
  '''lCerrada : loop '{' g '}' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = ""
  subexpressions[0]["value"] += toString(subexpressions[:2]) + subexpressions[2]
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
  subexpressions[0]["value"] += "\n"
  subexpressions[0]["value"] += toStringLineaCerrada(subexpressions[2])
  subexpressions[0]["var"] = "" 

#-----------------------------------------------------------------------------

def p_lCerrada8(subexpressions):
  '''lCerrada : loop COMMENT com lCerrada'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = ""
  subexpressions[0]["value"] += toString(subexpressions[:2])
  #COMMENT es un terminal asi que no tiene el tabbing apropiado segun el sistema este, lo agrego
  subexpressions[0]["value"] += "\n\ttabing" + subexpressions[2] 
  subexpressions[0]["value"] += toString(subexpressions[2:4]).replace("tabing", "tabing\t")+"\n"
  subexpressions[0]["value"] += toStringLineaCerrada(subexpressions[4])
  subexpressions[0]["var"] = ""

#-----------------------------------------------------------------------------

def p_lCerrada5(subexpressions):
  '''lCerrada : DO '{' g '}' WHILE '(' valores ')' ';' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = ""
  subexpressions[0]["value"] += toString(subexpressions[:2])[:-1] + " " + subexpressions[2]
  subexpressions[0]["value"] += "\n"
  subexpressions[0]["value"] += toString(subexpressions[2:4]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\ntabing"
  subexpressions[0]["value"] += toString(subexpressions[3:])
  subexpressions[0]["var"] = "" 
  chequearTipo([subexpressions[7]],["bool"],". La guarda debe ser un booleano")

#-----------------------------------------------------------------------------

def p_lCerrada9(subexpressions):
  '''lCerrada : DO lCerrada WHILE '(' valores ')' ';'  '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = ""
  subexpressions[0]["value"] += toString(subexpressions[:2])
  subexpressions[0]["value"] += "\n"
  subexpressions[0]["value"] += toStringLineaCerrada(subexpressions[2])
  subexpressions[0]["value"] += "\ntabing"
  subexpressions[0]["value"] += toString(subexpressions[2:])
  subexpressions[0]["var"] = "" 
  chequearTipo([subexpressions[5]],["bool"],". La guarda debe ser un booleano")

#----------------------------------------------------------------------------- 

def p_lCerrada10(subexpressions):
  '''lCerrada :  DO COMMENT com lCerrada WHILE '(' valores ')' ';'  '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = ""
  subexpressions[0]["value"] += toString(subexpressions[:2])
  subexpressions[0]["value"] += "\n\ttabing" + subexpressions[2] + "\n"
  subexpressions[0]["value"] += toString(subexpressions[2:4]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += toStringLineaCerrada(subexpressions[4])
  subexpressions[0]["value"] += "\ntabing"
  subexpressions[0]["value"] += toString(subexpressions[4:])
  subexpressions[0]["var"] = "" 
  chequearTipo([subexpressions[7]],["bool"],". La guarda debe ser un booleano")

#-----------------------------------------------------------------------------

#Este tambien faltaba!!

#----------------------------------------------------------------------------- 

def p_lCerrada10p(subexpressions):
  '''lCerrada :  DO  lCerrada COMMENT com WHILE '(' valores ')' ';'  '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = ""
  subexpressions[0]["value"] += toString(subexpressions[:2]) +"\n"
  subexpressions[0]["value"] += toStringLineaCerrada(subexpressions[2])
  subexpressions[0]["value"] += "\n\ttabing" + subexpressions[3]
  subexpressions[0]["value"] += toString(subexpressions[3:5]).replace("tabing", "tabing\t")
  subexpressions[0]["value"] += "\ntabing"
  subexpressions[0]["value"] += toString(subexpressions[4:])
  subexpressions[0]["var"] = "" 
  chequearTipo([subexpressions[7]],["bool"],". La guarda debe ser un booleano")

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
  subexpressions[0]["value"] = toString(subexpressions[:5]) + " "
  subexpressions[0]["value"] += toString(subexpressions[4:7])  + " "
  subexpressions[0]["value"] += toString(subexpressions[6:])
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
  setVariable(subexpressions, None)
  subexpressions[0]["elems"] = subexpressions[1].get("elems")

def p_func2(subexpressions):
  '''func : funcVoid'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  setVariable(subexpressions, None) 

#-----------------------------------------------------------------------------
# funcReturn -> FuncInt | FuncString | FuncBool

def p_funcReturn(subexpressions):
  '''funcReturn : funcInt
  | funcString
  | funcBool'''
  subexpressions[0] = {}
  subexpressions[0]["value"] =  toString(subexpressions)
  setTipo(subexpressions, 1) 
  subexpressions[0]["elems"] = subexpressions[1].get("elems")

#-----------------------------------------------------------------------------
#funcInt -> MULTIESCALAR( valores, valores param)

# NO VA ACA, retorna tipo vector
def p_funcInt1(subexpressions):
  '''funcInt : MULTIESCALAR '(' valores ',' valores   param ')' '''
  global vectores, variables
  subexpressions[0] = {}
  subexpressions[0]["value"] = toStringNoParen(subexpressions[:3])
  subexpressions[0]["value"] += toString(subexpressions[2:])
  setTipo(subexpressions, "vec")
  setVector(subexpressions, 3)

  chequearTipo([subexpressions[3]],["vec"])
  chequearVectorNumerico(subexpressions[3])
  chequearTipo([subexpressions[5]],["int"])

#-----------------------------------------------------------------------------
#funcInt -> LENGTH( valores)

def p_funcInt2(subexpressions):
  '''funcInt : LENGTH '(' valores ')' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toStringNoParen(subexpressions[:3]) 
  subexpressions[0]["value"] += toString(subexpressions[2:])
  setTipo(subexpressions, "int")
  chequearTipo([subexpressions[3]],["string","vec"])
  setVariable(subexpressions, None)

#-----------------------------------------------------------------------------
#funcString -> CAPIALIZAR(valores)

def p_funcString(subexpressions):
  '''funcString : CAPITALIZAR '(' valores ')' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toStringNoParen(subexpressions[:3]) 
  subexpressions[0]["value"] += toString(subexpressions[2:])
  setTipo(subexpressions, "string")
  chequearTipo([subexpressions[3]], ["string"])
  setVariable(subexpressions, None) 

#-----------------------------------------------------------------------------
# FuncBool -> colineales(valores,valores )

def p_funcBool(subexpressions):
  '''funcBool : COLINEALES '(' valores ',' valores ')' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toStringNoParen(subexpressions[:3]) 
  subexpressions[0]["value"] += toString(subexpressions[2:])
  setTipo(subexpressions, "bool")
  setVariable(subexpressions, None) 
  chequearTipo([subexpressions[3],subexpressions[5]], ["vec"])  
  vector1 = subexpressions[3]
  vector2 = subexpressions[5]
  chequearVectorNumerico(vector1)
  chequearVectorNumerico(vector2)


#-----------------------------------------------------------------------------
# FuncVoid -> print(Valores) 

def p_funcVoid(subexpressions):
  '''funcVoid : PRINT '(' valores ')' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toStringNoParen(subexpressions[:3]) 
  subexpressions[0]["value"] += toString(subexpressions[2:])
  setVariable(subexpressions, None) 

#-----------------------------------------------------------------------------
#Parametros de las funciones:
#-----------------------------------------------------------------------------

def p_param1(subexpressions):
  '''param : ',' valores'''
  chequearTipo([subexpressions[2]],["bool"])
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  setVariable(subexpressions, None)
  setTipo(subexpressions, "bool")

def p_param2(subexpressions):
  '''param : empty'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  setVariable(subexpressions, None)
  setTipo(subexpressions, None) 

def p_empty(subexpressions):
  '''empty : '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  setVariable(subexpressions, None)


#-----------------------------------------------------------------------------
#Vectores  y variables
#-----------------------------------------------------------------------------


def p_vec(subexpressions):
  '''vec : '[' elem ']' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  setTipo(subexpressions, "vec") 
  setVector(subexpressions, 2)

#Elem-> Valores, Elem | Valores
def p_elem1(subexpressions):
  '''elem : valores ',' elem'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  setTipo(subexpressions, "vec")
  
  tipoAnteriores = subexpressions[3]["typeVec"]
  tipoActual = getTipoExpresion(subexpressions[1])
  setVector(subexpressions, tipoActual)

  if tipoActual == "Para ejecucion":
    setVector(subexpressions, tipoAnteriores)
    return

  if tipoAnteriores == "Para ejecucion":
    setVector(subexpressions, tipoActual)
    return

  if (tipoActual, tipoAnteriores) in [("float", "int"), ("int", "float")]:
    setVector(subexpressions, "float")
    return

  if tipoAnteriores != tipoActual:
    raise Exception("El vector tiene que ser de un solo tipo")

  

  

def p_elem2(subexpressions):
  '''elem :  valores'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  tipoValor = getTipoExpresion(subexpressions[1])
  setVector(subexpressions, tipoValor)

#VecVal ->  var M

def p_vecVal1(subexpressions):
  '''vecVal : ID '[' valores ']'
  | vec '[' valores ']'
  | vecVal '[' valores ']'
  '''
  chequearAccesoVector(subexpressions)

  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  # Se deja el chequeo de estos atributos para tiempo de ejecucion
  setTipo(subexpressions, "Para ejecucion") 
  setVariable(subexpressions, "Para ejecucion")
  # Para que la asignacion (por ejemplo a[5] = 3) tenga la variable del vector para chequear tipos
  variable = subexpressions[1].get("var")
  if variable != None:
    subexpressions[0]["varAsig"] = variable

def p_vecVal2(subexpressions):
  '''vecVal : atributos '[' valores ']' '''
  chequearAccesoVector(subexpressions)

  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  # Se deja el chequeo de estos atributos para tiempo de ejecucion
  setTipo(subexpressions, "Para ejecucion") 
  setVariable(subexpressions, "Para ejecucion")
  # Se deja el chequeo de k.doublelist[0] para ejecucion
  subexpressions[0]["varAsig"] = "Para ejecucion"

def p_valores(subexpressions):
  '''valores : varYVals
  | varsOps
  | eMat
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
  | RES
  '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  setTipo(subexpressions, 1)
  setVariable(subexpressions, 1)
  setVector(subexpressions, 1)
  tipoValor = subexpressions[1].get("type")

  if subexpressions[1].get("type") == "reg": 
    subexpressions[0]["campos"] = subexpressions[1].get("campos")

#Registros:
#Reg -> {U}
def p_reg(subexpressions):
  '''reg :  '{' campos '}' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  setTipo(subexpressions, "reg") 
  subexpressions[0]["campos"] = subexpressions[2]["campos"]

#U -> campo: Valores, U | campof: Valores
#campo no es nada en la gramatica, pero creo que en realidad es cualquier string(!)
#Me parece que mejore el campo es un ID (!)
def p_campos(subexpressions):
  '''campos : ID ':' valores ',' campos
  | ID ':' valores '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["campos"] = {}
  nombreCampo = subexpressions[1]["var"]
  tipoCampo = subexpressions[3]["type"]

  if len(subexpressions) != 4:
    subexpressions[0]["campos"] = subexpressions[5]["campos"]

  subexpressions[0]["campos"][nombreCampo] = tipoCampo

def p_atributos(subexpressions):
  '''atributos : ID '.' valoresCampos'''
  
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  varReg = subexpressions[1]["var"]
  nombreCampo = subexpressions[3]["campo"]
  tipoRes = registros[varReg]["campos"].get(nombreCampo)
  if tipoRes == None:
    raise Exception("El campo no esta definido para ese registro") 

  setTipo(subexpressions, tipoRes)

def p_atributos2(subexpressions):
  '''atributos : reg '.' valoresCampos '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

  nombreCampo = subexpressions[3]["campo"]
  camposRegistro = subexpressions[1]["campos"]
  tipoCampoReg = camposRegistro.get(nombreCampo)

  if tipoCampoReg == None:
    raise Exception("El campo no esta definido para ese registro")  

  setTipo(subexpressions, tipoCampoReg)

def p_valoresCampos(subexpressions):
  '''valoresCampos : ID
  | end
  | begin'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  subexpressions[0]["campo"] = subexpressions[1]["var"]

def p_end(subexpressions):
  '''end : END'''
  subexpressions[0]["var"] = "end"

def p_begin(subexpressions):
  '''begin : BEGIN'''
  subexpressions[0]["var"] = "begin"

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

  if len(subexpressions) == 2:
    setTipo(subexpressions, 1)
    setVariable(subexpressions, 1)
    setVector(subexpressions, 1)
  else:
    setTipo(subexpressions, 2)
    setVariable(subexpressions, 2)
    setVector(subexpressions, 2)

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
  setTipo(subexpressions, 3)

  # Dejo los atributos de vectores y variables para tiempo de ejecucion
  setVariable(subexpressions, None)
  subexpressions[0]["elems"] = None

def p_valoresTernarioVars1(subexpressions):
  '''valoresTernarioVars : reg
  | vec
  | ternarioVars
  | '(' ternarioVars ')'
  | atributos
  | varsOps
  | varYVals
  | RES
  '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  if len(subexpressions) == 2:
    setTipo(subexpressions, 1)
    setVariable(subexpressions, 1)
    setVector(subexpressions, 1)
  else:
    setTipo(subexpressions, 2)
    setVariable(subexpressions, 2)
    setVector(subexpressions, 2)

def p_ternarioMat(subexpressions):
  '''ternarioMat : valoresBool '?' valoresTernarioMat ':' valoresTernarioMat  
  | expBool '?' valoresTernarioMat ':' valoresTernarioMat
  '''
  chequeadorTernario(subexpressions)
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

  tipo1 = getTipoExpresion(subexpressions[3])
  tipo2 = getTipoExpresion(subexpressions[5])
  if (tipo1, tipo2) in [("int", "float"), ("float", "int")]:
    setTipo(subexpressions, "float")
  else:
    setTipo(subexpressions, tipo1)

  # Dejo los atributos de vectores y variables para tiempo de ejecucion
  setVariable(subexpressions, None)
  subexpressions[0]["elems"] = None

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
    setTipo(subexpressions, 1)
    setVariable(subexpressions, 1)
    setVector(subexpressions, 1)
  else:
    setTipo(subexpressions, 2)
    setVariable(subexpressions, 2)
    setVector(subexpressions, 2)

def p_ternarioBool(subexpressions):
  '''ternarioBool : valoresBool '?' valoresTernarioBool ':' valoresTernarioBool  
  | expBool '?' valoresTernarioBool ':' valoresTernarioBool
  '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  setTipo(subexpressions, "bool")
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
  setTipo(subexpressions, "bool")

#-----------------------------------------------------------------------------------------

#VarYVals -> var | VecVal
def p_varYVals1(subexpressions):
  '''varYVals : ID '''
  global variables
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  setVariable(subexpressions, 1) 
  setTipo(subexpressions, 1)
  setVector(subexpressions, 1) 

def p_varYVals2(subexpressions):
  '''varYVals : vecVal
  | vecVal '.' varYVals
  '''
  global registros, vectores
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  # Pues vecVal se deja para tiempo de ejecucion
  setTipo(subexpressions, "Para ejecucion") 
  setVariable(subexpressions, "Para ejecucion")


  
#-----------------------------------------------------------------------------
#Operadores de variables:
#VarsOps -> --SMM | ++SMM | SMM
def p_varsOps1(subexpressions):
  '''varsOps : MENOSMENOS variable 
  | MASMAS variable '''
  chequearOperadorIncDec(subexpressions, "prefijo")
  subexpressions[0] = {}
  subexpressions[0]["value"] = toStringNoParen(subexpressions)
  setTipo(subexpressions, 2)
  setVariable(subexpressions, 2)
  setVector(subexpressions, 2)


def p_varsOps2(subexpressions):
  '''varsOps : variable MASMAS 
  | variable MENOSMENOS'''
  chequearOperadorIncDec(subexpressions, "postfijo")
  subexpressions[0] = {}
  subexpressions[0]["value"] = subexpressions[1]["value"][:-1] + subexpressions[2]
  setTipo(subexpressions, 1)
  setVariable(subexpressions, 1)
  setVector(subexpressions, 1)
#-----------------------------------------------------------------------------
#Asignaciones:

#Dejo las asignaciones no ambiguas como estaban antes
#Aca pongo varYvals por este caso g[a] = b;
def p_variable(subexpressions):
  '''variable : varYVals'''

  # No hace falta, se pisa el valor de antes pues es una asignacion
  # if nombreVec not in vectores:
  # En caso de que tenga una expresion como indice en un vector (Ver vecVal)

  if subexpressions[1].get("var") == None:
    raise Exception("Solo se puede asignar valores a variables")

  nombreVar = subexpressions[1].get("var")
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  variableVector = subexpressions[1].get("varAsig")

  if variableVector != None:
    setVariable(subexpressions, variableVector)
    subexpressions[0]["esVector"] = True
  else:
    setVariable(subexpressions, nombreVar) 

  setTipo(subexpressions, 1)

  if nombreVar not in vectores:
    vectores[nombreVar] = {}
  if nombreVar not in variables:
    variables[nombreVar] = {}
  if nombreVar not in registros:
    registros[nombreVar] = {}


def p_varAsig(subexpressions):
  '''varAsig : variable MULEQ valores
  | variable DIVEQ valores
  | variable MASEQ valores
  | variable MENOSEQ valores
  | variable '=' valores
  | ID '.' ID '=' valores'''
  global variables, vectores, registros
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

  chequearAsignacion(subexpressions)
  setTipo(subexpressions, 3)
  setVariable(subexpressions, 1)
  setVector(subexpressions, 3)

  nombreVarDestino = subexpressions[1]["var"]
  tipoValorFuente = getTipoExpresion(subexpressions[3])

  if nombreVarDestino == "Para ejecucion":
    return

  if tipoValorFuente == "reg":
    registros[nombreVarDestino]["campos"] = subexpressions[3].get("campos")

  nombreVarFuente = subexpressions[3].get("var")
  # Por si la fuente es una variable
  # a = b
  if nombreVarFuente != None and nombreVarFuente != "Para ejecucion":
    variable = variables[nombreVarFuente]
    tipoVarFuente = variable["type"]
    # Por si la fuente es un vector
    # a = b, b de tipo vector
    if tipoVarFuente == "vec":
      tipoVectorFuente = variable["typeVec"]
      variables[nombreVarDestino]["typeVec"] = tipoVectorFuente
      setTipo(subexpressions, "vec")

    variables[nombreVarDestino]["type"] = tipoValorFuente

  else:
    # Si la fuente no es una variable

    # Si es un vector explicito (no una variable) 
    # a = [3,2,2] (tiene typeVec y type == "vec")
    
    if tipoValorFuente == "vec":
      tipoVectorFuente = subexpressions[3]["typeVec"]
      variables[nombreVarDestino]["typeVec"] = tipoVectorFuente
      variables[nombreVarDestino]["type"] = "vec"
      return

    # Si se tiene a[6] = 5 entonces no se actualiza nada (a ya tiene su informacion de tipos)
    esVector = subexpressions[1].get("esVector")
    if esVector:
      return

    variables[nombreVarDestino]["type"] = tipoValorFuente


  # Si es un vector tengo que obtener el tipo de sus elementos y asignarle a elems de varYVals
  #Aca agrego que solo se haga en caso de hacer la asignacion por primera vez... tal vez haga falta algo mas
  #Uso el get porque si no me tiraba key errors

    
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
  | varYVals
  | varsOps
  '''
  subexpressions[0] = {}
  
  subexpressions[0]["value"] = toString(subexpressions)
  setTipo(subexpressions, 1)
  setVariable(subexpressions, 1)
  setVector(subexpressions, 1)


def p_valoresMat3(subexpressions):
  '''valoresMat : '(' ternarioMat ')' ''' 
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  setTipo(subexpressions, 2)
  setVariable(subexpressions, 2)
  setVector(subexpressions, 2)


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

  setTipoBinarioMat(subexpressions)
    
def p_eMat2(subexpressions):
  '''eMat : eMat '-' p
  | valoresMat '-' p
  | eMat '-' valoresMat
  | valoresMat '-' valoresMat
  '''
  chequeadorBinario(subexpressions, ["int", "float"])
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

  setTipoBinarioMat(subexpressions)
    
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
    setTipoBinarioMat(subexpressions)

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
  setTipo(subexpressions, "float")
  setTipoBinarioMat(subexpressions)

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
  subexpressions[0]["value"] = toStringNoParen(subexpressions)
  if len(subexpressions) == 3:
    setTipo(subexpressions, 2)
  else:
    setTipo(subexpressions, 1)


#Paren -> (EMat) | int | VarYVals | float | VarsOps| FuncInt
def p_paren1(subexpressions):
  '''paren : '(' eMat ')' 
  | '(' valoresMat ')'
  '''
  chequearTipo([subexpressions[2]], ["int", "float"])
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  setTipo(subexpressions, 2)

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
  setTipo(subexpressions, 1)

def p_valoresBool1(subexpressions):
  '''valoresBool : '('  ternarioBool ')' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  setTipo(subexpressions, 2)

def p_valoresBool2(subexpressions):
  '''valoresBool : '''
  subexpressions[0] = {}
  setTipo(subexpressions, None)
  subexpressions[0]["value"] = toString(subexpressions)

# Or -> Or or And | And
def p_expBool(subexpressions):
  '''expBool : expBool OR and
  | valoresBool OR and
  | expBool OR valoresBool
  | valoresBool OR valoresBool
  | and'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  setTipo(subexpressions, "bool")

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
  chequearUnicoTerminal(subexpressions, ["int", "float", "bool"])
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)


def p_tCompare(subexpressions):
  '''tCompare : eMat
  | varsOps
  | varYVals
  | INT
  | funcInt 
  | FLOAT
  | '(' ternarioMat ')' '''
  chequearUnicoTerminal(subexpressions, ["int", "float"])
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)

# Mayor -> TCompare > TCompare | Menor
def p_mayor(subexpressions):
  '''mayor : tCompare '>' tCompare
  | menor'''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  setVariable(subexpressions, None)
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
  setVariable(subexpressions, None) 
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
  setVariable(subexpressions, None) 


# TBool -> (ExpBool) | bool | VarYVals | FuncBool
def p_parenBool(subexpressions):
  '''parenBool : '(' expBool ')' '''
  subexpressions[0] = {}
  subexpressions[0]["value"] = toString(subexpressions)
  setVariable(subexpressions, None) 

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
      if(exp["value"].endswith(' ') or exp["value"].endswith(';')):
        res += str(exp["value"])
      else:
        res += str(exp["value"]) + " "
    except TypeError:
      if(exp == ";" or exp == "[" or exp == "{"or exp == ":" or exp == "." ):
        res = res[:-1]
        res += str(exp)
      else:
        if(exp == "]" or exp == "," or exp == ")"or exp == "}"):
          res = res[:-1]
          res += str(exp) + " "
        else:
          if(exp == "("):
            res += str(exp)
          else:
            res += str(exp) + " "
  return res


def toStringNoParen(subexpressions):
  res = ""
  for exp in subexpressions[1:]:
    try:
      res += str(exp["value"])
    except TypeError:
      res += str(exp)
  return res

# Dado una lista de subexpresiones, asigna los elementos del indice indiceFuente a la produccion
# Si la fuente no tiene elementos, asigna None
def setVector(subexpressions, fuente):
  if fuente == None or isinstance(fuente, str):
    subexpressions[0]["typeVec"] = fuente
    return

  tipoVector = subexpressions[fuente].get("typeVec")
  subexpressions[0]["typeVec"] = tipoVector
  return

# Dado una lista de subexpresiones, asigna la variables del indice indiceFuente a la produccion
# Si la fuente no tiene variable, asigna None
def setVariable(subexpressions, fuente):
  if fuente == None or isinstance(fuente, str):
    subexpressions[0]["var"] = fuente
    return

  variable = subexpressions[fuente].get("var")
  subexpressions[0]["var"] = variable
  return


# retorna el tipo apropiado en las operaciones binarias matematicas
# Se asume que ya paso por el chequeo de tipos
def setTipoBinarioMat(subexpressions):
  if len(subexpressions) == 4:
    tipo1 = getTipoExpresion(subexpressions[1])
    tipo2 = getTipoExpresion(subexpressions[3])
    operador = subexpressions[2]

    if (tipo1, tipo2) in [("Para ejecucion", "Para ejecucion"), ("Para ejecucion", "int"), ("int", "Para ejecucion")]:
      setTipo(subexpressions, "Para ejecucion")
      return

    if operador == "+" and (tipo1 == "string" or tipo2 == "string"):
      setTipo(subexpressions, "string")
      return

    if (tipo1, tipo2) in [("int", "int")]:
      setTipo(subexpressions, "int")
    else:
      setTipo(subexpressions, "float")

  if len(subexpressions) == 2:
      tipo1 = getTipoExpresion(subexpressions[1])
      setTipo(subexpressions, tipo1) 

  return

# Dado una lista de subexpresiones, asigna el tipo del indice indiceFuente a la produccion
# Si el elemento no tiene tipo, asigna None
def setTipo(subexpressions, fuente):
  if fuente == None or isinstance(fuente, str):
    subexpressions[0]["type"] = fuente
    return

  nombreVariable = subexpressions[fuente].get("var")

  if nombreVariable != None and nombreVariable != "Para ejecucion":
    # Si el tipo viene dado por una variable
    if nombreVariable in variables and subexpressions[fuente].get("indice") == None:
      tipo = variables[nombreVariable]["type"]
      subexpressions[0]["type"] = tipo
    else:
      subexpressions[0]["type"] = subexpressions[fuente]["type"]
  else:
    # Si no hay una variable y el tipo viene dado
    subexpressions[0]["type"] = subexpressions[fuente]["type"]
  return

# Obtiene el tipo de una expresion
def getTipoExpresion(subexpression):
  nombreVariable =  subexpression.get("var")
  if nombreVariable != None and nombreVariable != "Para ejecucion" and nombreVariable != "":
    variable = variables.get(nombreVariable)
    if variable == None:
      raise Exception("variable no inicializada")

    tipo = variables[nombreVariable]["type"]
  else:
    tipo = subexpression["type"]

  return tipo

# chequea si todos los elementos de la lista de subexpresiones son de 
# algun tipo de la lista tipos
# Ademas en caso de fallar se levanta una excepcion con el tipo esperado
# Se le puede pasar un mensaje adicional como tercer parametro, esto se usa para los chequeaodores
# de operadores
def chequearTipo(subexps, tipos, aditionalMessage=""):

  for subexp in subexps:
    tipo = getTipoExpresion(subexp)

    if tipo not in tipos:
      if tipo == "Para ejecucion":
        continue
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
    tipoCondicion = subexpressions[1]["type"]
    if tipoCondicion not in ["bool", "Para ejecucion"]:
      message = "La condicion del operador ? tiene que ser de tipo Bool"
      message += "\n se encontro tipo " + subexpressions[1]["type"]
      raise Exception(message)

    tipoRet1 = subexpressions[3]["type"]
    tipoRet2 = subexpressions[5]["type"]

    if (tipoRet1, tipoRet2) in [("int", "float"),  ("float", "int")]:
      return

    if "Para ejecucion" in [tipoRet1, tipoRet2]:
      return

    if tipoRet1 != tipoRet2:
      message = "Los valores de retorno del operador ? tiene que ser del mismo tipo"
      message += "\n se encontro tipos " + tipoRet1 + " y " + tipoRet2
      raise Exception(message)

def chequeadorSuma(subexpressions):
  if len(subexpressions) == 4:

    if subexpressions[1]["type"] == "string" and subexpressions[3]["type"] == "string":
      return

    chequeadorBinario(subexpressions, ["float", "int"])

  pass

def chequearUnicoTerminal(subexpressions, tipos):
    if len(subexpressions) == 2:
        subexps = [ subexpressions[1] ]
        if subexpressions[1]["type"] == "noType" and subexpressions[1]["type"] != "Para ejecucion":
          message = '''\n variable "''' + subexpressions[1]["var"] + '''" no inicializada'''
          raise Exception(message)

        chequearTipo(subexps, tipos)

def chequearAccesoVector(subexpressions):
  global vectores, variables

  tipoVariable1 = getTipoExpresion(subexpressions[1])

  nombreVar1 = subexpressions[1].get("var")
  if tipoVariable1 != "vec" and tipoVariable1 != "Para ejecucion":
    message = "El operador [i] solo se puede usar con variables de tipo vector"
    message += "\n Se encontro "

    if nombreVar1 == None:
      message += "tipo "
      message += tipoVariable1
    else:
      message += nombreVar1
      message += " de tipo "
      message += tipoVariable1

    raise Exception(message)

  nombreVar2 = subexpressions[3].get("var")
  if nombreVar2 == "Para ejecucion":
    return

  if nombreVar2 != None:
    tipoVariable2 = variables[nombreVar2]["type"]
  else:
    tipoVariable2 = subexpressions[3]["type"]

  if tipoVariable2 not in ["int", "Para ejecucion"]:
    raise Exception("El indice de un vector solo se puede ser de tipo int") 

def chequearOperadorIncDec(subexpressions, tipo):
  if tipo == "prefijo":
    variable = subexpressions[2]
    operador = subexpressions[1]
  
  if tipo == "postfijo":
    variable = subexpressions[1]
    operador = subexpressions[2]

  nombreVar = variable["var"]
  
  if nombreVar == None:
    message = "Solo se puede aplicar operador "
    message += operador
    message += " a variables"
    raise Exception(message)

  if nombreVar == "Para ejecucion":
    return

  if nombreVar not in variables:
    raise Exception("Variable no inicializada previamente")

  tipoVariable = variables[nombreVar]["type"]

  if tipoVariable not in ["int", "float", "Para ejecucion"]:
    raise Exception("El operador ++ solo se puede usar con variables de tipo float o int")

def chequearAsignacion(subexpressions):
  global variables

  #Si el lado izquierdo de la asignacion se refiere a una posicion de vector, se chequea estrictamente que se le asigne algo del tipo original.
  #Es decir, si es un vector de ints, solo se puede asignar ints.
  if subexpressions[1].get("indice") != None:
    if subexpressions[3].get("type") != subexpressions[1].get("type"):
      raise Exception ("No coinciden los tipos!")
  #Casos de asignacion a variables,  en asignaciones no se verifica el tipo!
  else:
    if subexpressions[1].get("var") == None:
      raise Exception("Solo se puede asignar valores a variables")

    operador = subexpressions[2]
    if operador not in ["=", "+="]:
      chequearTipo([subexpressions[3]], ["int", "float"])

    if operador == "+=":
      #Asumimos que previamente se inicializo la variable
      if subexpressions[1].get("type") == "string":
        chequearTipo([subexpressions[3]], ["string"])
      else:
        chequearTipo([subexpressions[3]], ["int", "float"])
      
    nombreVar = subexpressions[1].get("var")
      
  # if operador == "=" and variables[nombreVar] != {}:
    # if subexpressions[3].get("indice") == None and subexpressions[1].get("indice") == None:
    #   chequearTipo([subexpressions[3]],[variables[nombreVar].get("type")])
    # else:
 

