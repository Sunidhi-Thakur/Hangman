import random
import string
from words import lst


def hangman():
    word = random.choice(lst).upper()
    lettersInWord = set(word)
    alphabet = set(string.ascii_uppercase)
    lettersGuessed = set() #letters guessed by the user
    lives = 5


    while len(lettersInWord) > 0 and lives > 0:
        
        print("You have selected: ", ' '.join(lettersGuessed))

        wordList = [letter if letter in lettersGuessed else '_' for letter in word]
        print("Current word: ", ' '.join(wordList))



        userLetter = input("Guess a Letter: ").upper()
        if userLetter in alphabet - lettersGuessed:
            lettersGuessed.add(userLetter)
            if userLetter in lettersInWord:
                lettersInWord.remove(userLetter)

            else:
                lives -= 1
                print('Guessed letter not present in Word')
                print('Lives remaining = ', lives)

        elif userLetter in lettersGuessed:
            print('Letter already Guessed. Try another letter')

        else:
            print('invalid character')

    if lives == 0:
        print("Sorry...You Died! The word was ", word)
    else:
        print('You have guessed the word right....Its', word)
c = 'Y'
while(c != 'N'):
    hangman() 
    c = input("Play Again? Y|N: ")
    c = c.upper()
