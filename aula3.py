"""
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / forte
str -> string -> texto
Strings são textos que estão dentro de aspas
"""

print(1234) # aqui ele já detectou que é um numero, sem necessidade de declarar o tipo do dado
print('Bruno') # aqui ele já detectou que o dado é uma string devido as aspas únicas em volta do dado
print("Bruno") # aspas duplas também funciona da mesma forma, até então


# Aspas simples
print('Bruno Landi aspa única')
# Aspas duplas
print("Bruno Landi aspas duplas")

# Escape
print("Bruno \"Landi")

#r
print(r"Bruno \"Landi\"")

# alternativa a Espace / r

print(1, '"Bruno"') # se necessário utilizar algum caracter reservado, utilizar a aspa simples como principal e dupla como secundaria ou vice-versa
print(2, "'Bruno'")