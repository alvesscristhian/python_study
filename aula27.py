"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da str
"""

variavel = "Olá mundo"
print(variavel[4:])  # mundo até o fim
print(variavel[0:4])  # Olá
print(len(variavel))  # 9
print(variavel[0 : len(variavel) : 2])  # Pula 2 em 2
print(variavel[::-1])  # Inverte a string
