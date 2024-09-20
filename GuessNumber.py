# This game implements the random module, functions, user input and conditional statement.

# This game is easy to userstand and if you are not able to understand this code then focus on the basic of python.

# Share this game with your friends and don't forget to follow https://github.com/anmolvermaa

import random as rum

# Reset the game 
def resetGame():
    print("Do you want to play again ? enter 'y' to play again or 'e' to exit from the game  \n")
    play = str(input())

    if play == 'y' or play == 'Y':
        home()
    
    elif play == 'e' or play == 'E':
        print("Thanks for playing this game\n")
    
    else:
        print("Wrong key pressed")
        resetGame()


# Heart of the game
def gameLogic(string, computer):

    guess = 1
    print(string)
    user = int(input())
    
    while user != computer:
        
        if user > computer :
            print("\nLower number please")
            user = int(input())

        elif user < computer:
            print("\nHigher number please")
            user = int(input())
        
        guess += 1

        if guess == 20:
            print("To many guesses")

            resetGame()
            break
    
    if user == computer:
        print("You guessed the number in ",guess,"attempts\n")

        resetGame()
        
            
# Generate the random number 
def randomNumber(choice):
    if choice == 1:
        s = "Guess the number between 1 to 10 "
        computer = rum.randrange(1,11)
        
    elif choice == 2:
        s = "Guess the number between 1 to 100 "
        computer = rum.randrange(1, 101)

    elif choice == 3:
        s= "Guess the number between 1 to 500 "
        computer = rum.randrange(1, 501)
    
    elif choice == 4:
        s = "Guess the number between 1 to 5000 (Its your choice play if you can ) = "
        computer = rum.randrange(1, 5001)
        
    else:
        print("Wrong key pressed\n")
        home()
    
    gameLogic(s, computer)


# Home function 
def home():
    print("\nChoose the difficulty level of the game ")
    print("Enter 1 for Basic level")
    print("Enter 2 for medium level")
    print("Enter 3 for hard level")
    print("Enter 4 for crazyyyyy level")
    choice = int(input()) 
  
    randomNumber(choice)
    

# calling function
home()














