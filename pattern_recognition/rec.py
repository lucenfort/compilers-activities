import ply.lex as lex
import ply.yacc as yacc
import re


class PatternRecognizer:
    """
    Classe para reconhecimento de padrões usando expressões regulares.
    """

    def __init__(self):
        self.lexer = lex.lex(module=self)
        self.parser = yacc.yacc(module=self)

    def recognize(self, text):
        """
        Reconhece os padrões presentes no texto fornecido.

        Args:
            text (str): O texto a ser analisado.

        Returns:
            dict: Dicionário contendo os padrões reconhecidos.
                  As chaves são os nomes dos padrões e os valores são as correspondências encontradas.
        """
        self.patterns_found = {}
        self.parser.parse(text)
        return self.patterns_found

    # Regras léxicas
    tokens = ["CPF", "DATA", "CEP", "RG", "EMAIL"]

    def t_CPF(self, t):
        r"\d{3}\.\d{3}\.\d{3}-\d{2}"
        self.patterns_found["CPF"] = t.value
        return t

    def t_DATA(self, t):
        r"\d{2}/\d{2}/\d{4}"
        self.patterns_found["DATA"] = t.value
        return t

    def t_CEP(self, t):
        r"\d{5}-\d{3}"
        self.patterns_found["CEP"] = t.value
        return t

    def t_RG(self, t):
        r"\d{2}\.\d{3}\.\d{3}-\d"
        self.patterns_found["RG"] = t.value
        return t

    def t_EMAIL(self, t):
        r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
        self.patterns_found["EMAIL"] = t.value
        return t

    # Regra para lidar com caracteres não reconhecidos
    def t_error(self, t):
        t.lexer.skip(1)

    # Regra de precedência
    precedence = ()

    # Regras gramaticais
    def p_expression(self, p):
        """
        expression : CPF
                   | DATA
                   | CEP
                   | RG
                   | EMAIL
        """
        pass

    def p_error(self, p):
        pass

    def lex(self, text):
        self.lexer.input(text)
        tokens = []
        while True:
            token = self.lexer.token()
            if not token:
                break
            tokens.append(token)
        return tokens
