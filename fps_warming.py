import turtle
import random
import time

#screen
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("FPS Warm-Up Game")
turtle_screen.tracer(False)

#turtle
turtle.shape("circle")
turtle.shapesize(3,3,3)
turtle.color("yellow")

#score
score_text = turtle.Turtle()
score_text.hideturtle()
score_text.penup()
score_text.setpos(-67,225)
score_text.color("white")
score_text.write("SCORE :", font=("Comic Sans", 20, "normal"))

score = 0

score_point = turtle.Turtle()
score_point.hideturtle()
score_point.color("deep sky blue")
score_point.penup()
score_point.setpos(53,225)
score_point.write(str(score), font=("Comic Sans", 20, "normal"))

def score_raise(x,y):
    global score
    score += 1
    score_point.clear()
    score_point.write(str(score), font=("Comic Sans", 20, "normal"))

turtle.onrelease(score_raise,1)

#moving the turtle
def chn_loc(x,y):
    a = random.randint(-300, 300)
    b = random.randint(-300, 300)
    turtle.teleport(a,b)

turtle.onclick(chn_loc,1)

#timer
time_text = turtle.Turtle()
time_text.color("white")
time_text.penup()
time_text.hideturtle()
time_text.setpos(-50,265)
time_text.write("TİME: ",font=("Comic Sans", 20, "normal"))

time_number = turtle.Turtle()
time_number.color("red")
time_number.hideturtle()
time_number.setpos(30,265)
start = time.time()
while time.time() - start < 20:
    time_number.clear()
    time_number.write(int(20 - (time.time() - start)), font=("Comic Sans", 20, "normal"))
    turtle_screen.update()
    continue

def game_over():
    game_ovr_text = turtle.Turtle()
    game_ovr_text.hideturtle()
    game_ovr_text.color("red")
    game_ovr_text.penup()
    game_ovr_text.setpos(-125, 263)
    time_number.clear()
    time_text.clear()
    game_ovr_text.write("GAME OVER !", font=("Comic Sans", 30, "bold"))
    turtle.hideturtle()

turtle.ontimer(game_over)

turtle_screen.tracer(True)

turtle.mainloop()