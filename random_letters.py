import random
lista_palavras = ["camel", "monkey", "cat"]

chosen_word = random.choice(lista_palavras)
print(chosen_word)

usuario_input = input("escolha uma letra: ").lower()
print(usuario_input)


for letra in chosen_word:
    if letra == usuario_input:
        print("right")
    else:
       