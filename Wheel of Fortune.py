
import random

import string
import time
from unicodedata import category

print("The wheel game category is on colors")
puzzles_and_clues={1:"blue", 2:"green",3:"yellow", 4:"orange"}
def get_puzzle_and_clue(puzzles_and_clues):
    """
    puzzles_and_clues: dictionary of puzzles and clues,
    whose keys are clues and values are puzzles.
    Returns tuple of length two, where first element is
    clue and second element is puzzle.
    """
    print(puzzles_and_clues.keys())
    clue = puzzles_and_clues.keys()
    clue_val=(random.choice(list(puzzles_and_clues.keys())))
    print(clue_val)
    puzzle = puzzles_and_clues.get(clue_val)
    #puzzle([random.randint(0, len(puzzles_and_clues[clue]) - 1)])
    print(puzzle)
    puzzle_and_clue = (clue_val, puzzle)
    print(puzzle_and_clue)

    return puzzle_and_clue


def start():
    """
    Starts game, initializes important variables, and calls function:
    gameSetup(playerNames_hum, playerNames_comp, playerOrder_val, rounds)
    """

    playerNames_hum = ["Player1", "Player2", "Player3"]
    playerNames_comp = ["Player1", "Player2", "Player3"]
    playerOrder_val = [[0, 0], [0, 0], [0, 0]]
    rounds = ["first", "second", "third", "fourth"]
    gameSetup(playerNames_hum, playerNames_comp, playerOrder_val, rounds)


def gameSetup(playerNames_hum, playerNames_comp, playerOrder_val, rounds):
    """
    Calls game setup functions: get_numPlayers() and
    get_playerNames(numPlayers, playerNames_hum, playerNames_comp)
    Also calls function: game(players, playerOrder_val)
    """

    numPlayers = get_numPlayers()
    players = get_playerNames(numPlayers, playerNames_hum, playerNames_comp)
    game(players, playerOrder_val)


def disp_scores(playerOrder_val):
    print("playerOrder_val in disp_scores is:", playerOrder_val)
    playerOrder_val_round = playerOrder_val[:]
    playerOrder_val_round.sort(reverse=True)
    print("playerOrder_val in disp_scores is:", playerOrder_val)

    first = playerOrder_val[0]
    second = playerOrder_val[1]
    third = playerOrder_val[2]

    if first[0] != second[0] and second[0] != third[0]:
        print(first[1], "in first place with $" + str(first[0]) + ".")
        print(second[1], "in second place with $" + str(second[0]) + ".")
        print(third[1], "in third place with $" + str(third[0]) + ".")

    if first[0] > second[0] and second[0] == third[0]:
        print(first[1], "in first place with $" + str(first[0]) + ".")
        print(second[1], "and", third[1], "tied for second with $" + str(third[0]) + " each.")

    if first[0] == second[0] and second[0] > third[0]:
        print(second[1], "and", first[1], "tied for the lead with $" + str(third[0]) + " each .")
        print(third[1], "in second place with $" + str(third[0]) + ".")

    if first[0] == second[0] and second[0] == third[0]:
        print(second[1] + ", " + third[1] + ", and,", first[1], "tied for the lead with $" + str(third[0]) + " each .")
        print("Surely, this is more improbable than the Big Bang (Theory's merciful cancellation.)")


def game(players, playerOrder_val):
    """
    Calls function: get_playerOrder(players, playerOrder_val) and saves
    result to variable: playerOrder
    Calls function: game_round(players, playerOrder_val) and saves
    result to variable: playerOrder_val

    Iterates through function: game_round(playerOrder, playerOrder_val)
    four times, each time returning variable: playerOrder_val
    """

    # sets the number of rounds in the game
    num_rounds = 3
    # tracks the game's round number
    round_num = 1
    # list that tracks the starting order of players throughout game
    playerOrder = get_playerOrder(players, playerOrder_val)

    while round_num <= num_rounds:
     
        playerOrder_val = game_round(playerOrder, playerOrder_val, round_num)
        
        print("")
        print("At the end of ROUND", round_num, "the scores are:")
        disp_scores(playerOrder_val)
        print("")
        round_num += 1

    end_game(players)


def disp_puzzle_init(puzzle_and_clue):
    disp_puzzle = ""

    for i in range(len(puzzle_and_clue[1])):

        if puzzle_and_clue[1][i] in string.punctuation or puzzle_and_clue[1][i] == " ":
            disp_puzzle += puzzle_and_clue[1][i] + " "
        else:
            disp_puzzle += "_ "

    return disp_puzzle


def incom_puzzle_init(puzzle_and_clue):
    incom_puzzle = ""

    for i in range(len(puzzle_and_clue[1])):

        if puzzle_and_clue[1][i] in string.punctuation or puzzle_and_clue[1][i] == " ":
            incom_puzzle += puzzle_and_clue[1][i]
        else:
            incom_puzzle += "_"

    return incom_puzzle


def disp_remaining_letters(alpha):
    vowels = ["A", "E", "I", "O", "U"]
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y',
                  'Z']
    disp_vowels = ""
    disp_consonants = ""

    for i in range(len(vowels)):

        if vowels[i] in alpha:
            disp_vowels += vowels[i] + " "

    for i in range(len(consonants)):

        if consonants[i] in alpha:
            disp_consonants += consonants[i] + " "

    print("")
    print("Remaining letters:")
    print("Vowels: " + disp_vowels)
    print("Consonants: " + disp_consonants)
    print("")


def disp_puzzle_and_clue(puzzle_and_clue, disp_puzzle):
    print("")
    print('Clue: "' + str(puzzle_and_clue[0]) + '"')
    print("Puzzle: " + disp_puzzle)


def game_round(playerOrder, playerOrder_val, round_num):
    
    playerOrder_val_round = [[0, 0], [0, 0], [0, 0]]
    # retrieves and stores tuple, length two, whose first element
    # is round clue and second element is puzzle
    puzzle_and_clue = get_puzzle_and_clue(puzzles_and_clues)
    ##    puzzle_and_clue = ("color")
    # retrieves and stores string of empty puzzle
    disp_puzzle = disp_puzzle_init(puzzle_and_clue)
    # fills out as letters are guessed; not meant to be printed
    incom_puzzle = incom_puzzle_init(puzzle_and_clue)
    # stores uppercase alphabet in variable alpha
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z']

    turn_num = 1
    num_turns = 100
    print("The puzzle and clue for ROUND", round_num, "are:")

    player_turn = (round_num - 1) % 3
    while incom_puzzle != puzzle_and_clue[1]:

        if turn_num == num_turns:
            break
        while num_turns >= turn_num:
            turn_num += 1
            if turn_num == num_turns:
                break
            disp_puzzle_and_clue(puzzle_and_clue, disp_puzzle)
            disp_remaining_letters(alpha)
            player_selection = get_player_selection(playerOrder, player_turn, playerOrder_val_round)
            print("puzzle solved with the selection value: ",player_selection)
            if player_selection == 0:
                print("")
                print("You chose to solve the puzzle.")
                guess = get_guessWord()
                print('solved answer is :',guess,puzzle_and_clue[1])
                if guess == puzzle_and_clue[1]:

                    incom_puzzle = puzzle_and_clue[1]
                else:
                    print("")
                    print("Sorry, " + playerOrder[player_turn] + ", that is not the solution to the puzzle.")
                    print("Possession of the Wheel passes to " + playerOrder[(player_turn + 1) % 3] + ".")
                    time.sleep(1)
                    player_turn = (player_turn + 1) % 3
            if player_selection == 1:
                print("")
                print("You chose to spin The Wheel.")
                prize = get_prize(game_round)
                subPrize = prize
                if prize == "bankrupt":
                    playerOrder_val = bankrupt(player_turn, playerOrder, playerOrder_val_round)
                    player_turn = (player_turn + 1) % 3
                if prize == "loseATurn":
                    lose_a_turn(player_turn, playerOrder)
                    player_turn = (player_turn + 1) % 3
                if prize == "freePlay":
                    freePlay_choice = 0
                    print("")
                    print(playerOrder[player_turn], "spun for a FREE PLAY!")
                    print(playerOrder[
                              player_turn] + ", you may solve or guess a letter (including vowels) without penalty.")
                    print("")
                    selection_freePlay = get_freePlayChoice(playerOrder[player_turn])
                    subPrize = 500
                    if selection_freePlay == 1:
                        guess = get_guessfreePlay()

                        time.sleep(0.7)
                        letter_app = 0
                        print("")
                        print(disp_puzzle)
                        for i in range(len(puzzle_and_clue[1])):
                            if puzzle_and_clue[1][i] == guess:
                                time.sleep(0.7)
                                disp_puzzle = disp_puzzle[0:(i * 2)] + guess + disp_puzzle[((i * 2) + 1):]
                                incom_puzzle = incom_puzzle[0:i] + guess + incom_puzzle[(i + 1):]
                                print("")
                                print(disp_puzzle)
                                letter_app += 1
                        playerOrder_val_round[player_turn][0] = guess_result(player_turn, playerOrder,
                                                                             playerOrder_val_round, guess, subPrize,
                                                                             letter_app)
                        if incom_puzzle == puzzle_and_clue[1]:
                            break
                    if selection_freePlay == 2:
                        guess_word = get_guessWord()
                        if guess_word == puzzle_and_clue[1]:
                            incom_puzzle = guess_word
                            break
                        else:
                            print("")
                            print("Sorry, that is not the solution to the puzzle.")
                            print("Your Free Play spin, however, means that you keep possession of The Wheel.")
                            print("")

                if type(prize) is int:
                    print("")
                    print(playerOrder[player_turn] + " spun for $" + str(prize) + "!")
                    print("")
                    guess = get_guessConsonant()
                    if guess in alpha:
                        alpha = list(map(lambda x: x.replace(guess, ""), alpha))

                        time.sleep(0.7)
                        letter_app = 0
                        print("")
                        print(disp_puzzle)
                        time.sleep(0.7)
                        guess = guess.lower()
                        if guess in puzzle_and_clue[1]:
                            for i in range(len(puzzle_and_clue[1])):
                                if puzzle_and_clue[1][i] == guess:
                                    disp_puzzle = disp_puzzle[0:(i * 2)] + guess + disp_puzzle[((i * 2) + 1):]
                                    incom_puzzle = incom_puzzle[0:i] + guess + incom_puzzle[(i + 1):]
                                    print("")
                                    print(disp_puzzle)
                                    time.sleep(0.7)
                            for i in range(len(puzzle_and_clue[1])):
                                if puzzle_and_clue[1][i] == guess:
                                    letter_app += 1
                            playerOrder_val_round[player_turn][0] = guess_result(player_turn, playerOrder,
                                                                                 playerOrder_val_round, guess, subPrize,
                                                                                 letter_app)
                            if incom_puzzle == puzzle_and_clue[1]:
                                break
                        else:
                            print("")

                            print("")
                            print("I'm sorry",
                                  playerOrder[player_turn] + ", but there are no '" + guess + "'s in the puzzle.")
                            print("")
                            print("Possession of The Wheel passes to " + playerOrder[(player_turn + 1) % 3] + ".")
                            print("")

                            time.sleep(1.5)
                            player_turn = (player_turn + 1) % 3
                    else:
                        guess_previously_called(player_turn, playerOrder, guess)
            if player_selection == 2:
                print("")
                print("You chose to buy a vowel.")
                print("")
                playerOrder_val_round[player_turn][0] = (playerOrder_val_round[player_turn][0] - 250)
                guess = get_guessVowel()
                if guess in alpha:
                    alpha = list(map(lambda x: x.replace(guess, ""), alpha))
                else:
                    guess_previously_called(player_turn, playerOrder, guess)
                    player_turn = (player_turn + 1) % 3
                    break

                time.sleep(0.7)
                print("")
                print(disp_puzzle)
                letter_app = 0
                guess = guess.lower()
                if guess in puzzle_and_clue[1]:
                    for i in range(len(puzzle_and_clue[1])):
                        if puzzle_and_clue[1][i] == guess:
                            time.sleep(0.7)

                            disp_puzzle = disp_puzzle[0:(i * 2)] + guess + disp_puzzle[((i * 2) + 1):]
                            incom_puzzle = incom_puzzle[0:i] + guess + incom_puzzle[(i + 1):]
                            print("")
                            print(disp_puzzle)
                            letter_app += 1
                if letter_app == 0:
                    print("")

                    print("")
                    print("I'm sorry", playerOrder[player_turn] + ", but there are no '" + guess + "'s in the puzzle.")
                    print("")
                    print("Possession of The Wheel passes to " + playerOrder[(player_turn + 1) % 3] + ".")
                    print("")

                    time.sleep(1.5)
                    player_turn = (player_turn + 1) % 3
                    break
                if letter_app == 1:
                    print("")
                    print("Good guess,", playerOrder[player_turn] + "! There is 1", guess, "in the puzzle!")
                    print("")

                    print("")
                if letter_app >= 2:
                    print("")
                    print("Good guess,", playerOrder[player_turn] + "! There are", letter_app,
                          "'" + guess + "'s in the puzzle!")
                    print("")

                    print("")
            if incom_puzzle == puzzle_and_clue[1]:
                playerOrder_val[player_turn][0] = playerOrder_val_round[player_turn][0] + playerOrder_val[player_turn][
                    0]

                time.sleep(2.5)
                print("")
                print("Congratulations,", playerOrder[player_turn] + ". You correctly solved the puzzle:")
                print("")
                break

    print("playerOrder_val right before func return:", playerOrder_val)
    return playerOrder_val


def end_game(players):
    print("----------------------")
    print("GAME OVER!")
    print("----------------------")
    print("Would you like to play again? (y/n)")
    selection = input()
    if selection.lower() == "y" or selection.lower() == "yes":
        playerOrder_val = [[0, 0], [0, 0], [0, 0]]
        game(players, playerOrder_val)


def get_numPlayers():
    numPlayers = 0
    while numPlayers <= 0 or numPlayers > 3:
        print("")
        print("How many contestants (max: 3) will be playing today?")
        numPlayers = int(input("Number of players: ", ))
        if numPlayers == "One" or numPlayers == "one" or numPlayers == "ONE" or numPlayers == "1":
            numPlayers = 1
            print("You have selected play for 1 player.")
        if numPlayers == "Two" or numPlayers == "two" or numPlayers == "TWO" or numPlayers == "2":
            numPlayers = 2
            print("You have selected play for 2 players.")
        if numPlayers == "Three" or numPlayers == "three" or numPlayers == "THREE" or numPlayers == "3":
            numPlayers = 3
            print("You have selected play for 3 players.")
        if numPlayers < 1 or numPlayers > 3 or numPlayers == type(int):
            print("")

            print("ERROR: INVALID PLAYER NUMBER")

    return numPlayers


def get_playerNames(numPlayers, playerNames_hum, playerNames_comp):
    players = ["Player1", "Player2", "Player3"]
    print("")
   
    for i in range(numPlayers):
        name = ""
        while name == "":
            name = input(players[i] + ", what is your name? ")
            name = name.title()
            if name == "":
                print("Please try again.")

                print("")
        players[i] = name
    if numPlayers == 3:
        print("")

        print("")
        print("Welcome", players[0] + ",", players[1] + ", and", players[2] + "!")
        print("")
        if numPlayers == 2:
            players[2] = playerNames_comp[0]
        print("")
        
        print("Welcome", players[0] + " and", players[1] + "! Today you will be playing against", players[2] + ".")
        if numPlayers == 1:
            players[1] = playerNames_comp[0]
        players[2] = playerNames_comp[1]
        print("")
        
        print("Welcome", players[0] + "! Today you will be playing against", players[1], "and", players[2] + ".")

    return players


def get_playerOrder(players, playerOrder_val):
    playerOrder = []
    print("We will now play the Toss-Up Puzzle for possession of The Wheel in the first")
    print("round.")
    print("")
    print(players[0] + " will spin first.")
    print("")

    input("Press 'ENTER' to continue: ")
    for i in (0, 1, 2):
        print("")
        print(players[i] + ", get ready. You're up next!")
        print(players[i] + " prepares to spin The Wheel.")
        print("")
        input("Press 'ENTER' to spin The Wheel. ")
        print("")
        prize = prize = get_prize(0)

        print(players[i] + " received $" + str(prize) + ".")

        for j in (0, 1):
            if j == 0:
                playerOrder_val[i][j] = prize
            else:
                playerOrder_val[i][j] = players[i]
    print(playerOrder_val)
    if playerOrder_val[0][0] =='bankrupt' or playerOrder_val[0][0] =='loseATurn':
        playerOrder_val[0][0]=0
    if playerOrder_val[1][0] =='bankrupt' or playerOrder_val[1][0] =='loseATurn':
        playerOrder_val[1][0]=0
    if playerOrder_val[2][0] =='bankrupt' or playerOrder_val[2][0] =='loseATurn':
        playerOrder_val[2][0]=0
    playerOrder_val.sort(reverse=True)
    for i in range(3):
        if i == 0:
            playerOrder.insert(0, playerOrder_val[i][1])
        else:
            if i == 1:
                if playerOrder_val[i][0] > playerOrder_val[0][0]:
                    playerOrder.insert(0, playerOrder_val[i][1])
                else:
                    playerOrder.insert(1, playerOrder_val[i][1])
            else:
                if playerOrder_val[i][0] > playerOrder_val[0][0] and playerOrder_val[1][0]:
                    playerOrder.insert(0, playerOrder_val[i][1])
                elif playerOrder_val[i][0] < playerOrder_val[0][0] and playerOrder_val[1][0]:
                    playerOrder.insert(2, playerOrder_val[i][1])
                else:
                    playerOrder.insert(1, playerOrder_val[i][1])
    print("")
    print("Congratulations,", playerOrder[0] + "! You have won the Toss-Up Spin and will take possession")
    print("of The Wheel at the beginning of the first round.")
    print("")
    print(playerOrder[1] + " will Take possession of The Wheel after", playerOrder[0] + ", followed by",
          playerOrder[2] + ".")
    print("")

    input("Press 'ENTER' to begin the first round: ")
    print("")

    return playerOrder



def get_guessConsonant():
    check = False
    while check == False:
        guess = input("Please guess a consonant: ", )
        guess=guess.upper()
        if len(guess) == 1 and guess in ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
                                         'V', 'W', 'X', 'Y', 'Z']:
            check = True
        if len(guess) != 1:
            print("")

            print("ERROR: INVALID ENTRY!")
            print("Please enter one letter per guess.")

            print("")
            check = False
        if guess in ["A", "E", "I", "O", "U"]:
            print("")

            print("ERROR: INVALID ENTRY!")
            print("Entry must be a consonant.")

            print("")
            check = False

    return guess


def get_guessfreePlay():
    check = False
    while check == False:

        guess = input("Please guess a letter: ", )
        guess = guess.upper()
        if len(guess) == 1 and guess in string.ascii_uppercase:
            check = True
        if len(guess) != 1:
            print("")

            print("ERROR: INVALID ENTRY!")
            print("Please enter one letter per guess.")

            print("")
            check = False

    return guess


def get_guessVowel():
    check = False
    while check == False:
        guess = input("Please guess a vowel: ", )
        guess = guess.upper()
        if len(guess) == 1 and guess in ["A", "E", "I", "O", "U"]:
            check = True
        if len(guess) != 1:
            print("")

            print("ERROR: INVALID ENTRY!")
            print("Please enter one letter per guess.")

            print("")
            check = False
        if guess in ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y',
                     'Z']:
            print("")

            print("ERROR: INVALID ENTRY!")
            print("Entry must be a vowel.")

            print("")
            check = False

    return guess


def get_prize(game_round):
    prize = 0
    if game_round == 0:
        prizes = ["bankrupt", "bankrupt", "bankrupt", 500, 500, 500, 500, 750, 750,
                  500, 500, 500, 500, 550, 550, 550, 600, 600, 600, 600, 600,
                  600, 650, 650, 650, 650, 650, 650, 700, 700, 700, 700, 700,
                  700, 700, 700, 700, 800, 800, 800, 800, 800, 800, 900, 900,
                  900, "loseATurn", "loseATurn", "loseATurn", "loseATurn", 900, 900, 2500, 2500, 2500, 750, 750]
        prize = prizes[random.randint(0, 24)]
    if game_round == 1:
        prizes = ["bankrupt", "bankrupt", "bankrupt", "bankrupt", "bankrupt",
                  "bankrupt", "bankrupt", "bankrupt", 500, 500, 500, 500, 500, 500, 500, 500,
                  500, 500, 500, 500, 550, 550, 550, 600, 600, 600, 600, 600,
                  600, 650, 650, 650, 650, 650, 650, 700, 700, 700, 700, 700,
                  700, 700, 700, 700, 800, 800, 800, 800, 800, 800, 900, 900,
                  900, 900, 900, 900, 900, 900, 900, 2500, 2500, 2500, "loseATurn",
                  "loseATurn", "loseATurn", "freePlay", "freePlay", "freePlay", 750, 750,
                  750, 750]
        prize = prizes[random.randint(0, 24)]
    if game_round == 2:
        prizes = ["bankrupt", "bankrupt", "bankrupt", "bankrupt", "bankrupt",
                  "bankrupt", "bankrupt", "bankrupt", 500, 500, 500, 500, 500, 500, 500, 500,
                  500, 500, 500, 500, 550, 550, 550, 600, 600, 600, 600, 600,
                  600, 650, 650, 650, 650, 650, 650, 700, 700, 700, 700, 700,
                  700, 700, 700, 700, 800, 800, 800, 800, 800, 800, 900, 900,
                  900, 900, 900, 900, 900, 900, 900, 3500, 3500, 3500, "loseATurn",
                  "loseATurn", "loseATurn", "freePlay", "freePlay", "freePlay", 750, 750,
                  750, 750]
        prize = prizes[random.randint(0, 24)]
    if game_round == 3:
        prizes = ["bankrupt", "bankrupt", "bankrupt", "bankrupt", "bankrupt",
                  "bankrupt", "bankrupt", "bankrupt", 500, 500, 500, 500, 500, 500, 500, 500,
                  500, 500, 500, 500, 550, 550, 550, 600, 600, 600, 600, 600,
                  600, 650, 650, 650, 650, 650, 650, 700, 700, 700, 700, 700,
                  700, 700, 700, 700, 800, 800, 800, 800, 800, 800, 900, 900,
                  900, 900, 900, 900, 900, 900, 900, 3500, 3500, 3500, "loseATurn",
                  "loseATurn", "loseATurn", "freePlay", "freePlay", "freePlay", 750, 750,
                  750, 750]
        prize = prizes[random.randint(0, 24)]

    return prize


def get_guessWord():
    print("")
    guess = input("Input puzzle solution: ", )
    guess = guess.lower()
    print("")

    return guess


def get_freePlayChoice(player):
    selection_freePlay = 0
    choice = False
    while choice is False:
        while selection_freePlay != "letter" or selection_freePlay != "choose" or selection_freePlay != "s" or selection_freePlay != "solve" or selection_freePlay != "choose a letter" or selection_freePlay != "pick" or selection_freePlay != "pick a letter" or selection_freePlay == "solve the puzzle":

            print("")
            print
            player + ", would you like to solve the puzzle or choose a letter?"
            selection_freePlay = input("Selection: ")
            selection_freePlay = selection_freePlay.lower()
            if selection_freePlay == "letter" or selection_freePlay == "choose" or selection_freePlay == "s" or selection_freePlay == "solve the puzzle" or selection_freePlay == "solve" or selection_freePlay == "choose a letter" or selection_freePlay == "pick" or selection_freePlay == "pick a letter":
                break
            else:
                print("")

                print("ERROR: UNRECOGNIZED COMMAND.")
                print("Please select from the following and try again:")
                print("'SOLVE'")
                print("'LETTER'")
                print("'CHOOSE'")
                print("'CHOOSE A LETTER'")
                print("'PICK'")
                print("'PICK A LETTER'")

                print("")

        if selection_freePlay == "pick a letter" or selection_freePlay == "pick" or selection_freePlay == "letter" or selection_freePlay == "choose":
            selection_freePlay = 1
        if selection_freePlay == "solve" or selection_freePlay == "solve the puzzle" or selection_freePlay == "s":
            selection_freePlay = 2

        return selection_freePlay


def get_player_selection(playerOrder, player_turn, playerOrder_val_round):
    selection = 0
    select = 0
    choice = False
    while choice is False:
        while selection != "solve" or selection != "spin" or selection != "s" or selection != "pick" or selection != "solve the puzzle" or selection != "buy" or selection != "buy a vowel" or selection != "vowel" or selection != "v":

            if playerOrder_val_round[player_turn][0] >= 250:
                print("")
                print(playerOrder[player_turn] + ", would you like to SPIN, BUY A VOWEL, or SOLVE THE PUZZLE?")
            else:
                print("")
                print(playerOrder[player_turn] + ", would you like to SPIN or SOLVE THE PUZZLE?")
            selection = input("Selection: ")
            selection = selection.lower()
            if selection == "solve" or selection == "pick" or selection == "spin" or selection == "solve the puzzle" or selection == "buy" or selection == "buy a vowel" or selection == "vowel" or selection == "v":
                break
            else:
                print("")

                print("ERROR: UNRECOGNIZED COMMAND.")
                print("Please select from the following and try again:")
                print("'SOLVE'")
                print("'BUY A VOWEL'")
                print("'SPIN'")
        if selection == "pick a letter" or selection == "pick" or selection == "spin" or selection == "letter":
            select = 1
            return select
        if selection == "buy" or selection == "buy a vowel" or selection == "vowel":
            if playerOrder_val_round[player_turn][0] >= 250:
                select = 2

                return selection

            else:
                print("")
                print("You need a round prize of at least $250 in order to buy a vowel.")
                print("Please try again.")
                print("")
        if selection == "solve" or selection == "solve the puzzle":
            select = 0

            return select


def bankrupt(player_turn, playerOrder, playerOrder_val_round):
    print("")
    print(playerOrder[player_turn], "spun for BANKRUPT, bringing his total prize for this round to $0.")
    playerOrder_val_round[player_turn][0] = 0
    print("Possession of The Wheel passes to", playerOrder[((player_turn + 1) % 3)] + ".")
    print("")

    time.sleep(2.5)

    return playerOrder_val_round


def lose_a_turn(player_turn, playerOrder):
    print("")
    print(playerOrder[player_turn], "spun for LOSE A TURN!")
    print("")
    print("Sorry, " + playerOrder[player_turn] + ". Possession of The Wheel passes to " + playerOrder[
        (player_turn + 1) % 3] + ".")

    time.sleep(2.5)


def letter_app_sing(player_turn, playerOrder, playerOrder_val_round, guess, subPrize, letter_app):
    time.sleep(0.7)
    print("")
    print("Good guess,", playerOrder[player_turn] + "! There is 1", guess, "in the puzzle!")
    print("That adds $" + str(subPrize) + " to your total prize score!")
    print("")
    playerOrder_val_round[player_turn][0] = playerOrder_val_round[player_turn][0] + (subPrize * letter_app)

    print("")
    print(playerOrder[player_turn] + "'s total prize score for this round is now $" + str(
        playerOrder_val_round[player_turn][0]) + "!")
    print("")

    time.sleep(2.5)

    return playerOrder_val_round[player_turn][0]


def letter_app_plur(player_turn, playerOrder, playerOrder_val_round, guess, subPrize, letter_app):
    time.sleep(0.7)
    print("")
    print("Good guess,", playerOrder[player_turn] + "! There are", letter_app, "'" + guess + "'s in the puzzle!")
    print("That adds $" + str(subPrize * letter_app) + " to your total prize score!")
    print("")
    playerOrder_val_round[player_turn][0] = playerOrder_val_round[player_turn][0] + (subPrize * letter_app)

    print("")
    print(playerOrder[player_turn] + "'s total prize score is now $" + str(playerOrder_val_round[player_turn][0]) + "!")
    print("")

    time.sleep(2.5)

    return playerOrder_val_round[player_turn][0]


def guess_result(player_turn, playerOrder, playerOrder_val_round, guess, subPrize, letter_app):
    if letter_app == 0:
        print("")
        print("I'm sorry", playerOrder[player_turn] + ", but there are no '" + guess + "s in the puzzle.")
        print("Your Free Play, however, means that you keep possession of The Wheel.")
        print("")

    if letter_app == 1:
        playerOrder_val_round[player_turn][0] = letter_app_sing(player_turn, playerOrder, playerOrder_val_round, guess,
                                                                subPrize, letter_app)
    if letter_app >= 2:
        playerOrder_val_round[player_turn][0] = letter_app_plur(player_turn, playerOrder, playerOrder_val_round, guess,
                                                                subPrize, letter_app)

    return playerOrder_val_round[player_turn][0]


def guess_previously_called(player_turn, playerOrder, guess):
    print("")
    print("Sorry, '" + guess + "' has already been called in this round.")
    print( playerOrder[(player_turn + 1) % 3] + " now takes possession of The Wheel.")
    print("")

    time.sleep(1.5)

    return playerOrder


start()