# Guessing game
import random
jackpot=random.randint(1,100)
guess=int(input("Guess the number "))
counter=1
while guess!=jackpot:
    if guess>jackpot:
        print('Guess Lower')
    else:
        print('Guess Higher')
    
    guess=int(input("Guess the number Again "))
    counter+=1
print('Correct Guess')
print('The jackpot No was ',jackpot)
print('You Took',counter,'Attempts')



