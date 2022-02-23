import random
from copy import copy

from global_defs import GlobalDefs

from game.casting.gem import GemDefs
from game.shared.point import Point

class GemMaker:
    """Class responsible for randomly creating gems and placing them in the game.

    Attributes:
        _timer: The number of frames before the next gem is created. Set at random between TIMER_MIN and TIMER_MAX.
    """
    GEMS    =   [GemDefs.SILVER, GemDefs.GOLD, GemDefs.CORAL, GemDefs.ROSEQUARTZ, GemDefs.AQUAMARINE,
                GemDefs.GARNET, GemDefs.PERIDOT, GemDefs.ZIRCON, GemDefs.CITRINE, GemDefs.AMETHYST,
                GemDefs.TOPAZ, GemDefs.SAPPHIRE, GemDefs.RUBY, GemDefs.EMERALD, GemDefs.DIAMOND,
                GemDefs.OPAL, GemDefs.OBSIDIAN, GemDefs.PEBBLE, GemDefs.GRAVEL, GemDefs.ROCK, GemDefs.BOULDER]
    WEIGHTS =   [10, 7.5, 7.5, 7.5, 5, 
                5, 5, 3.5, 3.5, 3.5,
                3, 3, 3, 3, 2.5,
                2.5, 2, 25, 20, 15, 10]

    TIMER_MIN = 2
    TIMER_MAX = 5

    FALL_SPEED_MIN = 3
    FALL_SPEED_MAX = 8

    def __init__(self):
        """Construct a new GemMaker."""
        self._timer = GlobalDefs.FRAME_RATE # Start first drop 1 second after game start

    def on_update(self, cast):
        """Called every frame by the Director. Updates timer and spawns gem if neccesary.
        
        Args:
            cast (Cast): The current game's Cast of Actors.
        """
        self._timer -= 1
        if self._timer > 0:
            return
        # Spawn random gem at random column
        gem = copy(random.choices(GemMaker.GEMS, weights=GemMaker.WEIGHTS, k=1)[0])
        gem.set_fall_speed(random.randint(GemMaker.FALL_SPEED_MIN, GemMaker.FALL_SPEED_MAX))
        x = int(random.randint(0, GlobalDefs.COLS) * GlobalDefs.CELL_SIZE)
        gem.set_position(Point(x, 0))
        cast.add_actor("gems", gem)
        # Set timer for next spawn
        self._timer = random.randint(GemMaker.TIMER_MIN, GemMaker.TIMER_MAX)
