import turtle as t

# Constants for configuration
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BACKGROUND_COLOR = "black"
FACE_COLOR = "red"
EYE_COLOR = "white"
ARC_REACTOR_COLOR = "blue"
PEN_SIZE = 2

# Setup the turtle window
t.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
t.bgcolor(BACKGROUND_COLOR)
t.title("Iron Man Face")

# Initialize turtle for drawing
pen = t.Turtle()
pen.speed(0)
pen.pensize(PEN_SIZE)

def draw_circle(color, radius, x, y, filled=True):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    if filled:
        pen.fillcolor(color)
        pen.begin_fill()
    pen.circle(radius)
    if filled:
        pen.end_fill()

def draw_eyes():
    # Eyes
    draw_circle(EYE_COLOR, 60, -40, 60)
    draw_circle(EYE_COLOR, 60, 40, 60)
    # Eye reflections
    draw_circle(EYE_COLOR, 25, -37, 75)
    draw_circle(EYE_COLOR, 25, 37, 75)

def draw_arc_reactor():
    draw_circle(ARC_REACTOR_COLOR, 15, 0, -35)
    draw_circle(ARC_REACTOR_COLOR, 5, -15, -35)
    draw_circle(ARC_REACTOR_COLOR, 5, 15, -35)

# Main face outline
draw_circle(FACE_COLOR, 100, 0, 0)
draw_eyes()
draw_arc_reactor()

pen.hideturtle()
t.mainloop()
