
from random import choice
from time import sleep
Words = ['TERNO', 'PRETO', 'BOIAS', 'CAGAR', 'FUNDO', 'BANDA', 'QUERO', 'TERMO', ]

def runGame():
    tries = 0
    word_Choosed = choice(Words)
    def checking_word(wordie):
        
        position = 0
        mark = ''
        right_letters = ''
        global guessed_it
        guessed_it = False
        for letra in wordie:
            if letra == word_Choosed[position]:
                mark +=  '&  '
                
            elif letra in word_Choosed and letra != word_Choosed[position]:
                mark += '/  '
                
            else:
                mark += '-  '
            position += 1
            right_letters += letra + '  '
            if mark == '&  &  &  &  &  ':
                guessed_it = True

            else:
                guessed_it = False
                    
            
        print(right_letters)
        print(mark)
        return guessed_it
    
    
    while True:
        word_try = input().upper()
        guess = checking_word(word_try)
        if guess == False:
            tries += 1
            continue
        elif guess == True:
            break
    print("Você adivinhou! \nDeseja jogar denovo? S/N")
    WantToPlayAgain = input().upper()
    if WantToPlayAgain == 'S':
        print('Palavra nova escolhida! Qual será?')
        print('_  _  _  _  _')
        runGame()
    elif WantToPlayAgain == 'N':
        print('ok, até mais')
    
print("Bem vindo ao termon! Você quer jogar? S/N")
while True:
    WantToPlay = input().upper()
    if WantToPlay == "S":
        print("O jogo funciona da seguinte maneira:\n")
        sleep(1)
        print("O símbolo (&) indica que aquela letra está na palavra e na posição certa.\n")
        sleep(0.7)
        print("O símbolo (/) mostra que a letra existe, mas na está na posição errada.\n")
        sleep(0.7)
        print("O símbolo (-) indica que aquela letra não existe na palavra.\n")
        sleep(0.7)
        print("Bom jogo e boa sorte!\n")
        print("\n_  _  _  _  _  ")
    
        runGame()
        break
    elif WantToPlay == "N":
        print("Ok, até mais!")
        break
    elif WantToPlay == "add_word":
        print('Adicione a nova palavra:')
        new_word = input()
        Words.append(new_word)
        break
    else:
        print('Forma inválida, tente novamente.')

        
          