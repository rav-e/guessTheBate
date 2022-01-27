guess = 'e'
a = 0
while a==0 :
    user_input = input("Guess the Character: ")
    if(user_input == guess):
        print("You Guessed it Right!")
        a=1
        break
    else:
        print("Ops, Try Again")

    play_again = input("Wanna Play Again(Y/N)?")
    if ((play_again == "Y") or (play_again == "y") ):
        a = 0
    else:
        a = 1
        print("Alright, GG")

# to do
# Dynamic guess.
#adding random text to see changes update in git