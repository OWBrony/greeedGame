import pyray
from game.shared.point import Point


class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """

    def __init__(self, cell_size = 1):
        """Constructs a new KeyboardService using the specified cell size.
        
        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        self._cell_size = cell_size

    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1
        
        if pyray.is_key_down(pyray.KEY_UP):
            dy = -1
        
        if pyray.is_key_down(pyray.KEY_DOWN):
            dy = 1

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        return direction

    def get_direction_horizontal(self):
        """Gets the selected direction based on the currently pressed keys, ignoring any vertical input.

        Returns:
            Point: The selected direction.
        """
        direction = self.get_direction()
        return Point(direction.get_x(), 0)

    def get_direction_vertical(self):
        """Gets the selected direction based on the currently pressed keys, ignoring any horizontal input.

        Returns:
            Point: The selected direction.
        """
        direction = self.get_direction()
        return Point(0, direction.get_y())
