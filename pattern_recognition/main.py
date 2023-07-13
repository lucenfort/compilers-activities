from rec import PatternRecognizer

recognizer = PatternRecognizer()

text1 = "CPF: 123.456.789-00, Data de Nascimento: 01/01/1990, CEP: 12345-678, RG: 12.345.678-9, Email: test@example.com"
patterns1 = recognizer.recognize(text1)
print(patterns1)

text2 = "Este é um texto sem nenhum padrão."
patterns2 = recognizer.recognize(text2)
print(patterns2)

text3 = "Meu CPF é 123.456.789-00."
patterns3 = recognizer.recognize(text3)
print(patterns3)

text4 = "CPF: 123.456.789-00, CPF: 987.654.321-00"
patterns4 = recognizer.recognize(text4)
print(patterns4)
