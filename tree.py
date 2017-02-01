import turtle
import time
from collections import namedtuple

#Basic Defintions
numOfIterations = input("How many iterations: ")
window = turtle.Screen()
player = turtle.Turtle()
player.speed('fastest')

Info = namedtuple('Info', ['X', 'Y', 'Heading'])

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

stack = Stack()
length = 500
newString = ""
string = "b"
iterator = 0
numOfIterations += 0

def A(numOfIterations):
    if(numOfIterations > 6):
        branchLength = 2
    else:
        branchLength = 5
    player.forward(branchLength)

def B(numOfIterations):
    if(numOfIterations > 6):
        branchLength = 5
    else:
        branchLength = 5
    player.forward(branchLength)

def LeftBracket():
    new = Info(player.xcor(), player.ycor(), player.heading() )
    stack.push(new)
    player.left(45)

def RightBracket():
    old = stack.pop()
    player.penup()
    player.setposition(old.X, old.Y)
    player.setheading(old.Heading)
    player.right(45)
    player.pendown()


def convert(char):
    if(char == 'a'):
        return "aa"
    elif(char == 'b'):
        return "a[b]b"
    else:
        return char

options = {

}


window.screensize(length,length)
player.penup()
player.goto(0,-300)
player.pendown()
player.left(90)
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
    elif(c == '['):
        LeftBracket()
    else:
        RightBracket()

time.sleep(100)
