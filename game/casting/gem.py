import random

from global_defs import GlobalDefs
from game.casting.cast import Cast
from game.casting.actor import Actor
from game.shared.point import Point

from game.shared.color import ColorDefs

class Gem(Actor):
    def __init__(self, name, text, color, value):
        super().__init__()
        self._name = name
        self._value = value
        self._text = text
        self._font_size = GlobalDefs.FONT_SIZE
        self._color = color
        self._velocity = Point(0, 5)

    def _gem_collected(self, cast):
        robot = cast.get_first_actor("robot")
        message = cast.get_first_actor("message")
        robot.add_money(self._value)
        if self._value >= 0:
            message.set_color(ColorDefs.WHITE)
            message.set_text(f"Found {self._name}! (${self._value})")
        else:
            message.set_color(ColorDefs.RED)
            message.set_text(f"Hit by {self._name}! Ouch! (${self._value})")

    def on_update(self, cast):
        robot = cast.get_first_actor("robot")
        if self._position.get_y() >= GlobalDefs.GROUND_Y:
            if self._check_robot_touching(robot):
                self._gem_collected(cast)
            cast.remove_actor("gems", self)
    
    def get_name(self):
        return self._name

    def get_value(self):
        return self._value

    def set_fall_speed(self, speed):
        self._velocity = Point(0, abs(speed))

    def _check_robot_touching(self, robot):
        return abs(self._position.get_x() - (robot.get_position().get_x() + GlobalDefs.CELL_SIZE)) <= GlobalDefs.CELL_SIZE * 2

class Opal(Gem):
    COLOR_TIMER = 5
    COLORS =    [ColorDefs.WHITE, ColorDefs.RED, ColorDefs.LIME, ColorDefs.YELLOW, ColorDefs.CYAN, 
                ColorDefs.TEAL, ColorDefs.ORANGE, ColorDefs.CORAL, ColorDefs.PERIDOT, ColorDefs.AQUAMARINE, 
                ColorDefs.MAGENTA, ColorDefs.TOPAZ, ColorDefs.ROSEQUARTZ]

    def __init__(self):
        super().__init__("Opal", "*", ColorDefs.WHITE, 25000)
        self._timer = Opal.COLOR_TIMER

    def on_update(self, cast):
        super().on_update(cast)
        self._timer -= 1
        if self._timer > 0:
            return
        # Change to random color and reset timer
        self._color = random.choice(Opal.COLORS)
        self._timer = Opal.COLOR_TIMER

class Obsidian(Gem):
    COLORS       = [ColorDefs.PURPLE, ColorDefs.GREY, ColorDefs.BLACK]
    COLOR_FRAMES = [20, 10]

    def __init__(self):
        super().__init__("Obsidian", "*", Obsidian.COLORS[0], 50000)
        self._timer = Obsidian.COLOR_FRAMES[0]
        self._timer_stage = 0
    
    def on_update(self, cast):
        super().on_update(cast)
        # If we're already on the last color stage, do nothing
        if self._timer_stage >= len(Obsidian.COLOR_FRAMES):
            return
        self._timer -= 1
        if self._timer > 0:
            return
        # Advance to the next color stage and reset timer if able
        self._timer_stage += 1
        self._color = Obsidian.COLORS[self._timer_stage]
        if self._timer_stage < len(Obsidian.COLOR_FRAMES):
            self._timer = Obsidian.COLOR_FRAMES[self._timer_stage]

class GemDefs:
    # Treasure
    SILVER = Gem("Silver", "*", ColorDefs.SILVER, 500)
    GOLD = Gem("Gold", "*", ColorDefs.YELLOW, 1000)
    CORAL = Gem("Coral", "*", ColorDefs.CORAL, 1500)
    ROSEQUARTZ = Gem("Rose Quartz", "*", ColorDefs.ROSEQUARTZ, 2000)
    AQUAMARINE = Gem("Aquamarine", "*", ColorDefs.AQUAMARINE, 2500)
    GARNET = Gem("Garnet", "*", ColorDefs.GARNET, 3000)
    PERIDOT = Gem("Peridot", "*", ColorDefs.PERIDOT, 3750)
    ZIRCON = Gem("Zircon", "*", ColorDefs.ZIRCON, 4500)
    CITRINE = Gem("Citrine", "*", ColorDefs.ORANGE, 5000)
    AMETHYST = Gem("Amethyst", "*", ColorDefs.AMETHYST, 5750)
    TOPAZ = Gem("Topaz", "*", ColorDefs.TOPAZ, 6250)
    SAPPHIRE = Gem("Sapphire", "*", ColorDefs.BLUE, 7000)
    RUBY = Gem("Ruby", "*", ColorDefs.RED, 7500)
    EMERALD = Gem("Emerald", "*", ColorDefs.LIME, 8250)
    DIAMOND = Gem("Diamond", "*", ColorDefs.WHITE, 10000)
    OPAL = Opal()
    OBSIDIAN = Obsidian()
    # Hazards
    PEBBLE = Gem("Pebble", "o", ColorDefs.GREY, -5000)
    GRAVEL = Gem("Gravel", "o", ColorDefs.SLATE, -10000)
    ROCK = Gem("Rock", "O", ColorDefs.GREY, -20000)
    BOULDER = Gem("Boulder", "O", ColorDefs.SLATE, -50000)
