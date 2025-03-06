import turtle as t

class IronManFaceDrawer:
    # Configuration constants
    WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
    BACKGROUND_COLOR = "black"
    PEN_SIZE = 2
    
    # Color definitions
    FACE_COLOR = "red"
    EYE_COLOR = "white"
    ARC_REACTOR_COLOR = "blue"
    
    def __init__(self):
        """Initialize the drawing environment and turtle."""
        # Setup the turtle window
        t.setup(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        t.bgcolor(self.BACKGROUND_COLOR)
        t.title("Iron Man Face")
        
        # Create and configure the turtle
        self.pen = t.Turtle()
        self.pen.speed(0)  # Fastest drawing speed
        self.pen.pensize(self.PEN_SIZE)
    
    def draw_filled_circle(self, color, radius, x, y):
        """Draws a filled circle with the given color, radius, and center position offset."""
        self.pen.penup()
        self.pen.goto(x, y - radius)
        self.pen.pendown()
        self.pen.fillcolor(color)
        self.pen.begin_fill()
        self.pen.circle(radius)
        self.pen.end_fill()
    
    def draw_eyes(self):
        """Draws the eyes and reflections for the Iron Man face."""
        # Main eyes
        self.draw_filled_circle(self.EYE_COLOR, 60, -40, 60)
        self.draw_filled_circle(self.EYE_COLOR, 60, 40, 60)
        
        # Eye reflections
        self.draw_filled_circle(self.EYE_COLOR, 25, -37, 75)
        self.draw_filled_circle(self.EYE_COLOR, 25, 37, 75)
    
    def draw_arc_reactor(self):
        """Draws the arc reactor on the Iron Man face."""
        self.draw_filled_circle(self.ARC_REACTOR_COLOR, 15, 0, -35)
        self.draw_filled_circle(self.ARC_REACTOR_COLOR, 5, -15, -35)
        self.draw_filled_circle(self.ARC_REACTOR_COLOR, 5, 15, -35)
    
    def draw_face_outline(self):
        """Draws the main face outline for Iron Man."""
        self.draw_filled_circle(self.FACE_COLOR, 100, 0, 0)
    
    def draw(self):
        """Main function to orchestrate the drawing steps."""
        self.draw_face_outline()
        self.draw_eyes()
        self.draw_arc_reactor()
        self.pen.hideturtle()  # Hide the turtle cursor after drawing is complete
    
    def display(self):
        """Keeps the window open until closed."""
        t.mainloop()

def main():
    """Entry point for the script."""
    drawer = IronManFaceDrawer()
    drawer.draw()
    drawer.display()

if __name__ == "__main__":
    main()
