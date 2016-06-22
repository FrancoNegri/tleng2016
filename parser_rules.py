from lexer_rules import tokens

def p_eMat_plus(subexpressions):
    'eMat : eMat + p'

def p_eMat_plus(subexpressions):
    'eMat : eMat - p'

def p_eMat_plus(subexpressions):
    'eMat : p'

def p_p(subexpressions):
    'p : p * exp'

EMat → EMat + P | EMat - P | P
P → P * Exp | P / Exp | P % Exp | Exp
Exp → Exp ^ ISing | ISing
ISing → -Paren | +Paren | Paren
Paren → (EMat) | int | VarYVals | float | VarsOps | VarYVals | FuncInt