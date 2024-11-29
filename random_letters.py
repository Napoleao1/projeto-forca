import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



lista_palavras = ["camel", "monkey", "cat"]

lives = 6

chosen_word = random.choice(lista_palavras)
print(chosen_word)

# criando string com espaço em branco
placeholder = ""
# criando a váriavel para contar as palavras
word_length = len(chosen_word)
# loop para adicinar os espaços em brancos em qualquer palavra da lista
for position in range(word_length):
    placeholder += "_"
print(placeholder)

lives = 6


#jogador escolhe uma letra
game_over = False
correct_letters = []

while not game_over: #loop de escolha
    escolha = input("escolha uma letra: ").lower()
# criando váriavel que coloca a letra escolhida pelo usuário na posição _
    display = ""
    


    for letra in chosen_word:
        if letra == escolha:
            display += letra
            correct_letters.append(escolha)
        elif letra in correct_letters:
            display += letra
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win")