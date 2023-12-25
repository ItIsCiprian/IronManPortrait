import turtle as t  # Import the turtle module and give it an alias 't'

# Set up the drawing window with specific dimensions and background color
t.setup(800, 600)
t.bgcolor("black")
t.title("Iron Man Face")  # Title for the window, which will display at the top

# Initialize a new turtle instance for drawing shapes
pen = t.Turtle()
pen.speed(0)  # Set the drawing speed to the fastest (0 means no animation)
pen.color("red")  # Initial drawing color for the turtle's pen
pen.pensize(2)  # Set the width of the pen to 2 pixels

# Define a function to draw a filled circle with specified parameters
def draw_circle(color, radius, x, y):
    pen.penup()  # Lift the pen to move it without drawing
    pen.fillcolor(color)  # Set the fill color for the next shape
    pen.goto(x, y - radius)  # Move the pen to the starting position of the circle
    pen.pendown()  # Put the pen down to start drawing
    pen.begin_fill()  # Start filling the shape with the set color
    pen.circle(radius)  # Draw the circle with the given radius
    pen.end_fill()  # Complete the filling process for the circle

# Use the draw_circle function to create the components of Iron Man's face
# The parameters specify the color, radius, and central position of each circle

# Main face outline
draw_circle("red", 100, 0, 0)
# Eyes
draw_circle("white", 60, -40, 60)
draw_circle("white", 60, 40, 60)
# Eye reflections
draw_circle("white", 25, -37, 75)
draw_circle("white", 25, 37, 75)
# Arc Reactor and details
draw_circle("blue", 15, 0, -35)
draw_circle("blue", 5, -15, -35)
draw_circle("blue", 5, 15, -35)

# Hide the drawing turtle to give a clean final image
pen.hideturtle()

# Start the event loop for the window to listen for events, like mouse clicks or key presses
# This is necessary to keep the window open; otherwise, it would close immediately after drawing
t.mainloop()
