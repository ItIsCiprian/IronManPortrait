dddimport turtle as t
from dataclasses import dataclass
from typing import Tuple


@dataclass
class Point:
    """Represents a 2D coordinate point."""
    x: float
    y: float


@dataclass
class Circle:
    """Represents a circle with color, radius, and center position."""
    color: str
    radius: float
    center: Point


class IronManFaceDrawer:
    """Draws a stylized Iron Man face using turtle graphics."""
    
    # Window configuration
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    BACKGROUND_COLOR = "black"
    WINDOW_TITLE = "Iron Man Face"
    
    # Drawing configuration
    PEN_SIZE = 2
    DRAW_SPEED = 0  # Fastest
    
    # Color palette
    FACE_COLOR = "red"
    EYE_COLOR = "white"
    ARC_REACTOR_COLOR = "blue"
    
    def __init__(self):
        """Initialize the drawing environment and turtle."""
        self._setup_window()
        self.pen = self._create_pen()
    
    def _setup_window(self) -> None:
        """Configure the turtle window."""
        t.setup(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        t.bgcolor(self.BACKGROUND_COLOR)
        t.title(self.WINDOW_TITLE)
    
    def _create_pen(self) -> t.Turtle:
        """Create and configure the turtle pen."""
        pen = t.Turtle()
        pen.speed(self.DRAW_SPEED)
        pen.pensize(self.PEN_SIZE)
        return pen
    
    def _draw_circle(self, circle: Circle) -> None:
        """Draw a filled circle at the specified position."""
        self.pen.penup()
        self.pen.goto(circle.center.x, circle.center.y - circle.radius)
        self.pen.pendown()
        self.pen.fillcolor(circle.color)
        self.pen.begin_fill()
        self.pen.circle(circle.radius)
        self.pen.end_fill()
    
    def _get_face_components(self) -> list[Circle]:
        """Define all circles that compose the Iron Man face."""
        return [
            # Face outline
            Circle(self.FACE_COLOR, 100, Point(0, 0)),
            
            # Main eyes
            Circle(self.EYE_COLOR, 60, Point(-40, 60)),
            Circle(self.EYE_COLOR, 60, Point(40, 60)),
            
            # Eye reflections
            Circle(self.EYE_COLOR, 25, Point(-37, 75)),
            Circle(self.EYE_COLOR, 25, Point(37, 75)),
            
            # Arc reactor
            Circle(self.ARC_REACTOR_COLOR, 15, Point(0, -35)),
            Circle(self.ARC_REACTOR_COLOR, 5, Point(-15, -35)),
            Circle(self.ARC_REACTOR_COLOR, 5, Point(15, -35)),
        ]
    
    def draw(self) -> None:
        """Draw the complete Iron Man face."""
        for circle in self._get_face_components():
            self._draw_circle(circle)
        self.pen.hideturtle()
    
    def display(self) -> None:
        """Keep the window open until closed by user."""
        t.mainloop()


def main() -> None:
    """Entry point for the script."""
    drawer = IronManFaceDrawer()
    drawer.draw()
    drawer.display()


if __name__ == "__main__":
    main()