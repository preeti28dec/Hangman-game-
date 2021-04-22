import string
from word import choose_word
from images import MAGES
# choose_word=['preeti','chnachal','kumkum','bhagwati','karan','rinku','vicky','sunny']
# from images import IMAGES
# def get_hint(secret_word,letters_guessed):
#     import random
#     letters_not_guesses=[]
#     index=0
#     while index<len(secret_word):
#         let=secret_word[index]
#         if let not in letters_guessed:
#             letters_not_guesses.append(let)
#         index += 1
#     return random.choice(letters_not_guesses)
def is_word_guessed(secret_word,letters_guessed):
        # if secret_word==get_guessed_word(secret_word,letters_not_guesses):
        #     return True 
    return False
def get_guessed_word(secret_word,letters_guessed):
    index=0
    guessed_word=" "
    while index <len(secret_word):
        if secret_word[index] in letters_guessed:
            guessed_word+=secret_word[index]
        else:
            guessed_word+=" "
        index+=1
    return guessed_word
def get_available_letters(letters_guessed):
    import string 
    letters_left = string.ascii_lowercase
        # for i in letters_guessed:
        #     letters_left=letters_left.__replace(i,"")
    return letters_left
# def ifvalid(user_input):
#         if len(user_input)!=1:
#             return False 
#         if not user_input.isalpha():
#             return False 
#         return True
def hangman(secret_word):
    print("welcome to the game, Hangman")
    print("I am thinking of a word that is ",+str(len(secret_word),"letters"))
    print(" ")
    letters_guessed=[]
        # user_diffculty_choice=int(input("abhi aap kitni difficulty par hai yhna game me "))
        # total_lives=remaining_lives=8
        # images_selection_list_indices=[0,1,2,3,4,5,6,7]
        # if user_diffculty_choice not in ["a","b","c"]:
        #     print("aapki choice invalid hai\ngame easy mode mei start kar rahe hai ")
        # else:
        #     if user_diffculty_choice=="a":
        #         total_lives=reversed=8
        #         images_selection_list_indices=[0,2,3,4,5,6,7,]
        #     elif user_diffculty_choice=="b":
        #         total_lives=remaining_lives=6
        #         images_selection_list_indices=[0,2,3,5,6,7]
            # letters_guessed=[]
            # letters_not_guesses=[]
            # hit=0
            # while remaining_lives>0:
    available_letters=get_available_letters(letters_guessed)
    print("Availble letters ="+available_letters)
    guess=input("please guess the a letter")
    letter=guess.lower()
                # if not ifvalid(letter) and letter !="hint":
                #     print("invalid input")
                #     continue
                # if hit==0:
                #     if guess=="hint":
                #         p=get_hint(secret_word,letters_guessed)
                #         print("your hint for next character",p)
                #         hit=1
                #         continue
    if letter in secret_word:
        letters_guessed.append (letter)
        print("good guess",get_guessed_word)
        print(" ")
        if is_word_guessed(secret_word,letters_guessed)==True:
            print("** conguratulations you won.")
            print(" ")
                        # break
        else:
            print("Oops !That letter is not in my word:-",get_guessed_word)
                        # remaining_lives=1
            print(" ")
                #         print(remaining_lives)
                # else:
                #     print("sorry you ran out of guess : The word was "+str(secret_word))
secret_word=choose_word()
hangman(secret_word)