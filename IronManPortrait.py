import turtle as t

# Set up the screen
t.setup(800, 600)
t.bgcolor("black")
t.title("Iron Man Face")

# Create a turtle for drawing
pen = t.Turtle()
pen.speed(0)
pen.color("red")
pen.pensize(2)

# Draw a circle with a given color, radius, and position
def draw_circle(color, radius, x, y):
    pen.penup()
    pen.fillcolor(color)
    pen.goto(x, y - radius)
    pen.pendown()
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# Draw Iron Man's face
draw_circle("red", 100, 0, 0)
draw_circle("white", 60, -40, 60)
draw_circle("white", 60, 40, 60)
draw_circle("white", 25, -37, 75)
draw_circle("white", 25, 37, 75)
draw_circle("blue", 15, 0, -35)
draw_circle("blue", 5, -15, -35)
draw_circle("blue", 5, 15, -35)

# Hide the turtle
pen.hideturtle()

# Keep the window open until it's closed by the user
t.mainloop()
