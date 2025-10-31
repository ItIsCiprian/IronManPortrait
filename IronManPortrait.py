import turtle as t
from dataclasses import dataclass
from typing import Tuple

@dataclass
class Colors:
    """Color constants for the Iron Man face"""
    BACKGROUND: str = "black"
    FACE: str = "red"
    EYE: str = "white"
    ARC_REACTOR: str = "blue"

@dataclass
class Config:
    """Configuration settings for the drawing"""
    WINDOW_SIZE: Tuple[int, int] = (800, 600)
    PEN_SIZE: int = 2
    DRAWING_SPEED: int = 0  # Fastest speed

class IronManFaceDrawer:
    def __init__(self):
        """Initialize the drawing environment with optimized settings"""
        self._setup_screen()
        self._setup_turtle()
    
    def _setup_screen(self) -> None:
        """Configure the drawing screen with optimal settings"""
        screen = t.Screen()
        screen.setup(*Config.WINDOW_SIZE)
        screen.bgcolor(Colors.BACKGROUND)
        screen.title("Iron Man Face")
        # Enable fastest drawing mode
        screen.tracer(0)
    
    def _setup_turtle(self) -> None:
        """Configure the turtle with optimal settings"""
        self.pen = t.Turtle()
        self.pen.hideturtle()  # Hide turtle immediately for better performance
        self.pen.speed(Config.DRAWING_SPEED)
        self.pen.pensize(Config.PEN_SIZE)
    
    def _draw_filled_circle(self, color: str, radius: float, x: float, y: float) -> None:
        """Optimized method to draw a filled circle"""
        self.pen.up()
        self.pen.goto(x, y - radius)
        self.pen.down()
        self.pen.fillcolor(color)
        self.pen.begin_fill()
        # Use more efficient circle drawing
        self.pen.circle(radius, steps=36)  # Optimize steps for smoother circles
        self.pen.end_fill()
    
    def draw_face(self) -> None:
        """Draw the complete Iron Man face with optimized ordering"""
        # Draw larger elements first
        self._draw_filled_circle(Colors.FACE, 100, 0, 0)  # Face outline
        
        # Draw eyes
        for x in (-40, 40):
            self._draw_filled_circle(Colors.EYE, 60, x, 60)  # Main eyes
        
        # Draw eye reflections
        for x in (-37, 37):
            self._draw_filled_circle(Colors.EYE, 25, x, 75)
        
        # Draw arc reactor components
        self._draw_filled_circle(Colors.ARC_REACTOR, 15, 0, -35)  # Center
        for x in (-15, 15):
            self._draw_filled_circle(Colors.ARC_REACTOR, 5, x, -35)  # Side pieces
        
        # Update screen once at the end
        t.update()
    
    def display(self) -> None:
        """Display the completed drawing"""
        t.done()

def main() -> None:
    """Entry point with error handling"""
    try:
        drawer = IronManFaceDrawer()
        drawer.draw_face()
        drawer.display()
    except (turtle.Terminator, KeyboardInterrupt):
        print("\nDrawing terminated by user")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()