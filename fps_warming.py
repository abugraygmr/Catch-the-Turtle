import turtle
import random
import time

#screen
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("FPS Warming Game")
turtle_screen.tracer(False)

#score
score_heading = turtle.Turtle()
score_heading.hideturtle()
score_heading.penup()
score_heading.setpos(-67,225)
score_heading.color("white")
score_heading.write("SCORE :", font=("Comic Sans", 20, "normal"))

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

def chn_loc(x,y):
    a = random.randint(-300, 300)
    b = random.randint(-300, 300)
    turtle.teleport(a,b)

turtle.onclick(chn_loc,1)

#turtle
turtle.shape("turtle")
turtle.shapesize(3,3,3)
turtle.color("yellow")

#timer
time_text = turtle.Turtle()
time_text.color("white")
time_text.penup()
time_text.hideturtle()
time_text.setpos(-50,265)
time_text.write("TİME: ",font=("Comic Sans", 20, "normal"))

timer_text = turtle.Turtle()
timer_text.color("red")
timer_text.hideturtle()
timer_text.setpos(30,265)
start = time.time()
while time.time() - start < 20:
    timer_text.clear()
    timer_text.write(int(20 - (time.time() - start)), font=("Comic Sans", 20, "normal"))
    turtle_screen.update()
    continue

def game_over():
    game_ovr_text = turtle.Turtle()
    game_ovr_text.hideturtle()
    game_ovr_text.color("red")
    game_ovr_text.penup()

    game_ovr_text.teleport(-125, 263)

    timer_text.clear()
    time_text.clear()


    game_ovr_text.write("GAME OVER !", font=("Comic Sans", 30, "bold"))

    turtle.hideturtle()

turtle.ontimer(game_over, 20)

turtle_screen.tracer(True)

turtle.mainloop()