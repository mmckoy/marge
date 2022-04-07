s = ['hello'] # word search
#s= 'Mississippi' # letter seach
file =open('C:\\Users\\Marjea\\Downloads\\words.txt')
import random
s=file.readlines()
s=random.choice(s)
letter=set(s)
print(letter)
guess = 7
guessed_letter=set()

while True:  # continuos input

    # get the user input
    c = input('Enter the letter/word to guess: ')
    if len(c) == 1:
        found = False
        new_str = ''
        # iterate user input throuth the given word
        for k in s:
            # if user input letter is found then add it to a set
            if c.lower() == k.lower():
                found =True
                new_str +=''.join(c)
                guessed_letter.add(c)
            else:
                new_str +=''.join('_')
        if found ==False:
            guess -=1
        if guess ==0 and (letter == guessed_letter):
            print('Game Over and Player Won')
            break
        elif guess ==0 and (letter != guessed_letter):
            print('Game Over and Player Lost')
            break
        elif guess ==2 and (letter != guessed_letter) :
             guess -=1
        elif guess ==1 and (letter != guessed_letter) :
            print('Game Over and Player Lost Game')
            break
        print(new_str)
    elif len(c) >1:
        found = False
        new_str = ''
        # iterate user input throuth the given word
        for k in s:
            # if user input letter is found then add it to a set
            if c.lower() == k.lower():
                found =True
                new_str +=''.join(c)
                guessed_letter.add(c)
            else:
                new_str +=''.join('_')
        if found ==False:
            guess -=1
        if guess ==0 and (letter == guessed_letter):
            print('Game Over and Player Won')
            break
        elif guess ==0 and (letter != guessed_letter):
            print('Game Over and Player Lost')
            break
        elif guess ==2 and (letter != guessed_letter) :
             guess -=1
        elif guess ==1 and (letter != guessed_letter) :
            print('Game Over and Player Lost Game')
            break
        print(new_str)