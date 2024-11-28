import random
lista_palavras = ["camel", "monkey", "cat"]

chosen_word = random.choice(lista_palavras)
print(chosen_word)

#criando string com espaço em branco
placeholder = "_"
word_lenght = len(chosen_word) #criando a váriavel para contar as palavras
for position in range(word_lenght): # loop para adicinar os espaços em brancos em qualquer palavra da lista
    placeholder += "_" 
print(placeholder)

escolha = input("escolha uma letra: ").lower()
print(escolha)



for letra in chosen_word:
    if  letra == escolha:
        print("right")
    else:
        print("wrong")