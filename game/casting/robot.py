from global_defs import GlobalDefs
from game.casting.cast import Cast
from game.casting.actor import Actor

from game.shared.color import ColorDefs
from game.shared.point import Point

class Robot(Actor):
    """The player character. Moves back and forth and stores the player's score.

    Attributes:
        _money: The money (i.e. score) of the player.
    """
    def __init__(self):
        """Construct a new Robot."""
        super().__init__()
        self._text = "#"
        self._font_size = GlobalDefs.FONT_SIZE * 2
        self._color = ColorDefs.WHITE
        x = int(GlobalDefs.MAX_X / 2)
        y = GlobalDefs.GROUND_Y - GlobalDefs.CELL_SIZE
        self._position = Point(x, y)
        self._money = 0

    def get_money(self):
        """Get the current money of the Robot."""
        return self._money

    def add_money(self, money):
        """Add money to the robot. Can be negative."""
        self._money += money
