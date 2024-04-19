import turtle as t

# Configuration constants for window and drawing
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BACKGROUND_COLOR = "black"
PEN_SIZE = 2
t.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
t.bgcolor(BACKGROUND_COLOR)
t.title("Iron Man Face")

# Turtle for drawing setup
pen = t.Turtle()
pen.speed(0)  # Fastest drawing speed
pen.pensize(PEN_SIZE)

# Color definitions
FACE_COLOR = "red"
EYE_COLOR = "white"
ARC_REACTOR_COLOR = "blue"

def draw_filled_circle(pen, color, radius, x, y):
    """Draws a filled circle with the given color, radius, and center position offset."""
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def draw_eyes():
    """Draws the eyes and reflections for the Iron Man face."""
    # Main eyes
    draw_filled_circle(pen, EYE_COLOR, 60, -40, 60)
    draw_filled_circle(pen, EYE_COLOR, 60, 40, 60)
    # Eye reflections
    draw_filled_circle(pen, EYE_COLOR, 25, -37, 75)
    draw_filled_circle(pen, EYE_COLOR, 25, 37, 75)

def draw_arc_reactor():
    """Draws the arc reactor on the Iron Man face."""
    draw_filled_circle(pen, ARC_REACTOR_COLOR, 15, 0, -35)
    draw_filled_circle(pen, ARC_REACTOR_COLOR, 5, -15, -35)
    draw_filled_circle(pen, ARC_REACTOR_COLOR, 5, 15, -35)

def draw_face_outline():
    """Draws the main face outline for Iron Man."""
    draw_filled_circle(pen, FACE_COLOR, 100, 0, 0)

def main():
    """Main function to orchestrate the drawing steps."""
    draw_face_outline()
    draw_eyes()
    draw_arc_reactor()
    pen.hideturtle()
    t.mainloop()

if __name__ == "__main__":
    main()
