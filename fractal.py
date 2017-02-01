import turtle
import time
from collections import namedtuple

#Basic Defintions
numOfIterations = input("How many iterations: ")
numOfIterations += 0
window = turtle.Screen()
player = turtle.Turtle()
player.speed('fastest')
string = raw_input("What is your starting string: ")
newString = ""
length = 10
iterator = 0

#initializing the L-System
print("The available variables are A, B, [, ], +, -")
print("A and B are draw, [/] is push/pop, and +/- is turn right/left ")
convertions = ["A","B"]
convertions[0] = raw_input("What does A convert to: ")
convertions[1] = raw_input("What does B convert to: ")
lengthA = input("What ratio of length L is A (accepts values greater than 0 and less than 1): ")
lengthA *= length
while(lengthA > 10):
    lengthA = input("Enter a correct ratio for A")
    lengthA *= length
lengthB = input("What ratio of length L is B (accepts values greater than 0 and less than 1): ")
lengthB *= length
while(lengthB > 10):
    lengthB = input("Enter a correct ratio for B")
    lengthB *= length
rightTurnAngle = input("How far do you want to turn on a + (in degrees): ")
rightTurnAngle += 0
while(rightTurnAngle <= 0 or rightTurnAngle >= 360):
    rightTurnAngle = input("Enter a correct number of degrees between 0 and 360: ")
    rightTurnAngle += 0
leftTurnAngle = input("How far do you want to turn on a - (in degrees): ")
leftTurnAngle += 0
while(leftTurnAngle <= 0 and leftTurnAngle >= 360):
    leftTurnAngle = input("Enter a correct number of degrees between 0 and 360: ")
    leftTurnAngle += 0


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

def A():
    if(numOfIterations > 6):
        player.forward(lengthA)
    else:
        player.forward(5)

def B():
    if(numOfIterations > 6):
        player.forward(lengthB)
    else:
        player.forward(5)

def LeftBracket():
    new = Info(player.xcor(), player.ycor(), player.heading() )
    stack.push(new)

def RightBracket():
    old = stack.pop()
    player.penup()
    player.setposition(old.X, old.Y)
    player.setheading(old.Heading)
    player.pendown()

def plus():
    player.right(rightTurnAngle)

def minus():
    player.left(leftTurnAngle)

def convert(char):
    if(char == 'a'):
        return convertions[0]
    elif(char == 'b'):
        return convertions[1]
    else:
        return char

options = {

}


window.screensize(500,500)
player.penup()
player.goto(0,-300)
player.pendown()
player.left(90)
player.hideturtle()

while iterator < numOfIterations:
    for c in string:
        newString += convert(c)
    string = newString
    newString = ""
    iterator += 1

for c in string:
    if(c == 'a'):
        A()
    elif(c == 'b'):
        B()
    elif(c == '+'):
        plus()
    elif(c == '-'):
        minus()
    elif(c == '['):
        LeftBracket()
    else:
        RightBracket()

time.sleep(100)
