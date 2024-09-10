import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
FONT = ("Arial",30,"normal")
screen.title("iko games: HANGMAN")

turtle_1= turtle.Turtle()
turtle_1.color("red")
turtle_2=turtle.Turtle()
turtle_2.color("blue")
def questions_head():
    a = random.randint(10, 10000)
    b = random.randint(10, 10000)
    x = screen.numinput("Poker", f"{a}+{b}:", 1000, minval=10, maxval=100000)
    if x == a+b:
        questions_head()
    else:
        man_head()


def questions_chest():
    a = random.randint(10, 10000)
    b = random.randint(10, 10000)
    x = screen.numinput("Poker", f"{a}+{b}:", 1000, minval=10, maxval=100000)
    if x == a+b:
        questions_chest()
    else:
        man_chest()
def question_left_arm():
    a = random.randint(10, 10000)
    b = random.randint(10, 10000)
    x = screen.numinput("Poker", f"{a}+{b}:", 1000, minval=10, maxval=100000)
    if x == a + b:
        question_left_arm()
    else:
        man_left_arm()
def question_right_arm():
    a = random.randint(10, 10000)
    b = random.randint(10, 10000)
    x = screen.numinput("Poker", f"{a}+{b}:", 1000, minval=10, maxval=100000)
    if x == a + b:
        question_right_arm()
    else:
        man_right_arm()
def question_stomach():
    a = random.randint(10, 10000)
    b = random.randint(10, 10000)
    x = screen.numinput("Poker", f"{a}+{b}:", 1000, minval=10, maxval=100000)
    if x == a + b:
        question_stomach()
    else:
        man_stomach()

def question_right_leg():
    a = random.randint(10, 10000)
    b = random.randint(10, 10000)
    x = screen.numinput("Poker", f"{a}+{b}:", 1000, minval=10, maxval=100000)
    if x == a + b:
        question_right_leg()
    else:
        man_right_leg()
def question_left_leg():
    a = random.randint(10, 10000)
    b = random.randint(10, 10000)
    x = screen.numinput("Poker", f"{a}+{b}:", 1000, minval=10, maxval=100000)
    if x == a + b:
        question_left_leg()
    else:
        man_left_leg()
def execution_board():

    turtle_1.left(180)
    turtle_1.forward(100)
    turtle_1.right(180)

    turtle_1.forward(50)

    turtle_1.left(90)
    turtle_1.forward(150)
    turtle_1.right(90)
    turtle_1.forward(80)
    turtle_1.right(90)
    turtle_1.forward(20)
    questions_head()


def man_head():
    turtle_2.hideturtle()
    turtle_2.penup()
    turtle_2.left(180)
    turtle_2.forward(100)
    turtle_2.right(180)

    turtle_2.forward(50)

    turtle_2.left(90)
    turtle_2.forward(150)
    turtle_2.right(90)
    turtle_2.forward(80)
    turtle_2.right(90)
    turtle_2.forward(20)
    turtle_2.right(90)
    turtle_2.showturtle()
    turtle_2.pendown()
    turtle_2.circle(10)
    questions_chest()
def man_chest():
    turtle_2.hideturtle()


    turtle_2.circle(10, 180)
    turtle_2.showturtle()

    turtle_2.right(90)
    turtle_2.forward(10)
    turtle_2.right(90)

    question_left_arm()
def man_left_arm():
    turtle_2.hideturtle()

    turtle_2.left(45)
    turtle_2.forward(30)
    question_right_arm()

def man_right_arm():
    turtle_2.right(180)
    turtle_2.forward(30)
    turtle_2.right(90)
    turtle_2.forward(30)
    turtle_2.right(180)
    turtle_2.forward(30)
    question_stomach()

def man_stomach():
    turtle_2.right(225)
    turtle_2.forward(40)
    question_right_leg()

def man_right_leg():
    turtle_2.left(45)
    turtle_2.forward(30)
    question_left_leg()

def man_left_leg():
    turtle_2.right(180)
    turtle_2.forward(30)
    turtle_2.left(90)
    turtle_2.forward(30)
    turtle_2.right(180)
    turtle_2.forward(30)





execution_board()

screen.mainloop()