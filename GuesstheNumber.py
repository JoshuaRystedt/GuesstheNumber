#   This is a simple yet personal and fun guess the number game is written in Python as a terminal based application
#
#   Copyright (C) 2015 by Joshua Rystedt
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   To read a copy of the GNU General Public License see <http://www.gnu.org/licenses/>.

# Import randint from random
from random import randint, choice

# Random response lists
GoHigher = ["Go HIGHER.",
           "HIGHER.",
           "Guess a HIGHER number.",
           "Guess a HIGHER number... or lose.",
           "May your guesses traverse in an upward trajectory. Go HIGHER.",
           "You have yet to reach the mountaintop. Go HIGHER.",
           "Want to win? Guess a HIGHER number.",
           "Bigger is better. Guess a HIGHER number."]
GoLower = ["Go LOWER.",
           "LOWER.",
           "Guess a LOWER number.",
           "Guess a LOWER number... or lose.",
           "May your guesses traverse in a downward trajectory. Go LOWER.",
           "Keep digging. Go LOWER.",
           "Want to win? Guess a LOWER number.",
           "My number might be small but she sure is cute. Guess a LOWER number."]

# Generate random number between 1 and 100
def thenumber():
    print "I'm thinking of a number between 1 and 100. Can you guess what it is?"
    result = randint(1,100)
    return result

# User guess
def userguess():
    result = raw_input("Guess the number: ")
    try:
        val = int(result)
        result = int(result)
        return result
    except ValueError:
        print "That's not a number!"
        exit()

# Number comparison
def numcomp(number, guess):
    if guess < number:
        if guess == number - 1:
            print "So close! Go HIGHER."
        else:
            print choice(GoHigher)
    elif guess > number:
        if guess == number + 1:
            print "So close! Go LOWER."
        else:
            print choice(GoLower)
    elif guess == number:
        print "You win! That was exactly the number I was thinking of."
        exit()

# While loop
def guessloop(number):
    remainingguess = 5
    while remainingguess > 0:
        guess = userguess()
        numcomp(number,guess)
        remainingguess -= 1
        if remainingguess != 1:
            print "You have " + str(remainingguess) + " guesses remaining"
        else:
            print "You have " + str(remainingguess) + " guess remaining"
        print
    else:
        print "Sorry... you lost."
        print "The number was: " + str(number)
        print "I'm sure you'll do better next time."

# Execute
Number = thenumber()
print
guessloop(Number)