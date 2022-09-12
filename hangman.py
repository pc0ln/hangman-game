import random
from wordlist import words, alphabet

used_words = []

# Get's the word to guess
def get_word(words):
    # Picks random word
    word = random.choice(words)
    # Checks to make sure the word hasn't been used if played again
    while word in used_words:
        word = random.choice(words)
    # Adds word to used words list so if played again there will be no repeat of words
    used_words.append(word)
    return word.upper()

def print_char(lives): # Builds the character for the game
    print("     /|")
    print("    / |")
    if lives < 6:
        print("    0 |")
    else:
        print("      |")
    if lives == 4:
        print("    | |")
    if lives ==3:
        print("   /| |")
    if lives < 3:
        print("   /|\|")
        print("    | |")
    else:
        print("      |")
    if lives == 1:
        print("   /  |")
    if lives == 0:
        print("   / \|")
    else:
        print("      |")
    print("      |")
    print("   ___|___")


def print_line(cur_word):
    print("\n" +" ".join(cur_word)+ "\n\n")

def hangman():
    word = get_word(words) #sets the word to guess
    valid_chars = list(alphabet) #sets intial characters able to be guessed
    used_chars = [] #sets the initial characters already guessed
    cur_word = [] #sets how the current word looks
    lives = 6

    #build the intial cur_word
    for c in word:
        if c == " " or c == "-":
            cur_word.append(c)
        else:
            cur_word.append("_")

    #getting user input
    while "".join(cur_word) != word and lives > 0: #compares current word to the word
        print_char(lives)
        print_line(cur_word)
        print(f"You have {lives} lives left.")
        print("You've guessed the letters: " + " ".join(used_chars))
        guess = input("Guess a letter: ").upper()
        if guess in valid_chars: #if guess is able to be guessed
            valid_chars.remove(guess) #removes current guess from valid chars so it cant be repeated
            used_chars.append(guess) #adds the guess to previous guess list
            used_chars.sort()
            if guess in word:
                indicies = [i for i, letter in enumerate(word) if letter == guess] #indicies of every instance of guessed letter in word
                for i in indicies: # goes through the indicies of the word and adds to current word
                    cur_word.pop(i)
                    cur_word.insert(i, guess)
            else:
                lives-=1
    if lives == 0: #Losing
        print_char(lives) #Prints character if lost
        print_line(cur_word)
        print("Sorry you ran out of lives :(\n")
        print(f"The word was {word} but you got to "+"".join(cur_word) +"\n")
    else:
        print_line(cur_word) #Winning
        print("Congrats you got the word "+ word + "\n")
    play_again =input("Press Y if you want play again or any other key to leave\n") #ask if want to play again
    if  play_again.upper() == "Y":   
        hangman() #recurse so game can be played again


hangman()