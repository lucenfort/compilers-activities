from calclexer import lexer
from calcparser import parser


# Função para executar a calculadora
def run_calculator():
    while True:
        try:
            # Solicitar entrada do usuário
            s = input("calc > ")

            # Verificar se o usuário quer sair do programa
            if s.lower() == "sair":
                break

            # Analisar e executar a expressão
            result = parser.parse(s)
            if result is not None:
                print(result)

        except EOFError:
            break


# Executar a calculadora
if __name__ == "__main__":
    run_calculator()
