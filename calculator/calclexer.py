from ply import lex

# Lista de nomes de tokens
tokens = (
    "NUMBER",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "LPAREN",
    "RPAREN",
)

# Expressões regulares para tokens simples
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_LPAREN = r"\("
t_RPAREN = r"\)"


# Uma expressão regular com regras para números
def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


# Regra para rastrear números de linha
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# Uma string contendo caracteres ignorados (espaços e tabulações)
t_ignore = " \t"


# Regra de manipulação de erros
def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


# Construir o lexer
lexer = lex.lex()
