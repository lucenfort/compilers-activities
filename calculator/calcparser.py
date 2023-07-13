from ply import yacc
from calclexer import tokens

# Regras de precedência
precedence = (
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
    ("nonassoc", "UMINUS"),
)


# Definição da gramática
def p_statement_expr(p):
    """
    statement : expression
    """
    print(p[1])


def p_expression_binop(p):
    """
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
    """
    if p[2] == "+":
        p[0] = p[1] + p[3]
    elif p[2] == "-":
        p[0] = p[1] - p[3]
    elif p[2] == "*":
        p[0] = p[1] * p[3]
    elif p[2] == "/":
        p[0] = p[1] / p[3]


def p_expression_uminus(p):
    """
    expression : MINUS expression %prec UMINUS
    """
    p[0] = -p[2]


def p_expression_group(p):
    """
    expression : LPAREN expression RPAREN
    """
    p[0] = p[2]


def p_expression_number(p):
    """
    expression : NUMBER
    """
    p[0] = p[1]


def p_error(p):
    print("Erro de sintaxe na entrada!")


# Construir o parser
parser = yacc.yacc()
