from global_defs import GlobalDefs
from game.casting.cast import Cast
from game.casting.actor import Actor

from game.shared.color import ColorDefs
from game.shared.point import Point

class Robot(Actor):
    def __init__(self):
        super().__init__()
        self._text = "#"
        self._font_size = GlobalDefs.FONT_SIZE * 2
        self._color = ColorDefs.WHITE
        x = int(GlobalDefs.MAX_X / 2)
        y = GlobalDefs.GROUND_Y - GlobalDefs.CELL_SIZE
        self._position = Point(x, y)
        self._money = 0

    def get_money(self):
        return self._money

    def add_money(self, money):
        self._money += money
