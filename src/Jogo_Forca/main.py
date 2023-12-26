import time
import random

name = input("Qual é seu nome ? ")
print ("Olá ", name, " bem vindo ao jogo da forca!")

time.sleep(1)

print("Start quesssing ...")

time.sleep(0.5)

listOfNords = ("devmidea","secret","cat","trash","python")

randomNumber = random.randint(0, len(listOfNords) 1-)

guessWord = listOfNords[randomNumber]

word = guessWord

guesses = ''

turns = 10

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
        
        if failed == 0:
            print("\nYou win")
            break
        print

        guess = input("guess a charecter: ")
        guesses += guess
        
        if guess not in word:
            turns -= 1
            print("Wrong guess \n you have", turns,"tries left\n")
            if turns == 0:
                print("You loose\n")

