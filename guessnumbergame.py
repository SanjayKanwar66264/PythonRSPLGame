# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

secret_number = 100
x = 7
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0,100)
    print "New Game. Range is from 0 to 100", secret_number
    print "Number of remaining guesses is 7"
    print ""
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    secret_number = random.randrange(0,100)
    print "Secret Number", secret_number
    print ""
# remove this when you add your code   
def range1000():
    # button that changes the range to [0,1000) and starts a new game  
    global secret_number
    secret_number = random.randrange(0,1000)
    print "Secret Number", secret_number
    print ""
    
def input_guess(guess):
    # main game logic goes here
    global x
    value = int(guess)
    x -= 1
    print "Guess was",value
    print "Number of remaining guesses is ", x
    if x == 0:
        print"You ran out of guesses.  The number was", secret_number
        print ""
        return new_game()
    if value == secret_number:
        print "Correct!"
    elif value < secret_number:
        print "Higher!"
    else:
        print "Lower!"       
    print ""
    
# create frame
f = simplegui.create_frame('Guess the number', 200, 200)
f.add_button("Range is [0,1000)", range1000,200)
f.add_button("Range is [0,100)", range100,200)
f.add_input('Enter a guess', input_guess,100)

# register event handlers for control elements and start frame
f.start()

# call new_game 
new_game()


