import random
from copy import copy

from global_defs import GlobalDefs

from game.casting.gem import Gem, GemDefs
from game.shared.point import Point

class GemMaker:
    GEMS = [GemDefs.SILVER, GemDefs.GOLD, GemDefs.CORAL, GemDefs.ROSEQUARTZ, GemDefs.AQUAMARINE,
            GemDefs.GARNET, GemDefs.PERIDOT, GemDefs.ZIRCON, GemDefs.CITRINE, GemDefs.AMETHYST,
            GemDefs.TOPAZ, GemDefs.SAPPHIRE, GemDefs.RUBY, GemDefs.EMERALD, GemDefs.DIAMOND,
            GemDefs.PEBBLE, GemDefs.GRAVEL, GemDefs.ROCK, GemDefs.BOULDER]

    TIMER_MIN = 2
    TIMER_MAX = 5

    FALL_SPEED_MIN = 3
    FALL_SPEED_MAX = 8

    def __init__(self):
        self._timer = GlobalDefs.FRAME_RATE # Start first drop 1 second after game start

    def on_update(self, cast):
        self._timer -= 1
        if self._timer > 0:
            return
        # Spawn random gem at random column
        gem = copy(random.choice(GemMaker.GEMS))
        gem.set_fall_speed(random.randint(GemMaker.FALL_SPEED_MIN, GemMaker.FALL_SPEED_MAX))
        x = int(random.randint(0, GlobalDefs.COLS) * GlobalDefs.CELL_SIZE)
        gem.set_position(Point(x, 0))
        cast.add_actor("gems", gem)
        # Set timer for next spawn
        self._timer = random.randint(GemMaker.TIMER_MIN, GemMaker.TIMER_MAX)
