import turtle
import time
from collections import namedtuple

numOfIterations = input("How many iterations: ")
window = turtle.Screen()
player = turtle.Turtle()
length = 500
newString = ""
string = "b"
iterator = 0
numOfIterations += 0

def A(numOfIterations):
    if(numOfIterations > 8):
        branchLength = 1
    elif(numOfIterations > 6):
        branchLength = 2
    else:
        branchLength = 5
    player.forward(branchLength)

def B(numOfIterations):
    if(numOfIterations > 8):
        branchLength = 1
    elif(numOfIterations > 6):
        branchLength = 2
    else:
        branchLength = 5
    player.forward(branchLength)

def LeftBracket():
    player.left(60)

def RightBracket():
    player.right(60)

def convert(char):
    if(char == 'a'):
        return "b-a-b"
    elif(char == 'b'):
        return "a+b+a"
    else:
        return char

window.screensize(length,length)
player.penup()
if(numOfIterations % 2 == 0):
    player.goto(-550,-430)
else:
    player.goto(-550,430)
player.pendown()
#player.left(90)
player.hideturtle()

while iterator < numOfIterations:
    for c in string:
        newString += convert(c)
        print '', iterator, '', numOfIterations
    string = newString
    newString = ""
    iterator += 1

for c in string:
    if(c == 'a'):
        A(numOfIterations)
    elif(c == 'b'):
        B(numOfIterations)
    elif(c == '-'):
        LeftBracket()
    else:
        RightBracket()

time.sleep(100)
