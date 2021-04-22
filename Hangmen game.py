import random
word_list = ["insert", "kumkum", "words", "chanchal", "preeti", "python", "bhagwati"]
def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    chance = 6
    print("Let's play Hangman")
    print("show how many chance we have ",display_hangman(chance))
    print('we check word',word_completion)
    print("\n")
    while not guessed and chance > 0:
        guess = input("guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            # The isalpha() function checks whether a character is an alphabet or not.
            if guess in guessed_letters:
                print("you already tried", guess, "!")
            elif guess not in word:
                print(guess, "isn't in the word :")
                chance -= 1
                guessed_letters.append(guess)
            else:
                print("Nice one,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                # The enumerate() function adds a counter as the key of the enumerate object.
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already tried ", guess, "!")
            elif guess != word:
                print(guess, " ist nicht das Wort :(")
                chance -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("invalid input")
        print(display_hangman(chance))
        print(word_completion)
        print("\n")
    if guessed:
        print("Good Job, you guessed the word!")
    else:
        print("I'm sorry, but you ran out of chance. The word was " + word + ". Maybe next time!")

def display_hangman(chance):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[chance]
def main():
    word = get_word(word_list)
    play(word)
    while input("Again? (Y/N) ").upper() == "Y":
        word = get_word(word_list)
        play(word)
if __name__ == "__main__":
    main()

# We can use an if __name__ == "__main__" block to allow or prevent parts of code from being run when the modules are 
# imported. When the Python interpreter readsa file, the __name__ variable is set as __main__ if the module being run,
# or as the module's name if it is imported.
                





        


