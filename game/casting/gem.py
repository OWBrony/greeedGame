import random

from global_defs import GlobalDefs
from game.casting.cast import Cast
from game.casting.actor import Actor
from game.shared.point import Point

from game.shared.color import ColorDefs

class Gem(Actor):
    """An Actor that falls from the top of the screen to be collected by the player.

    The Gem types used in-game are defined in the GemDefs class, and creation during gameplay is managed by GemMaker.
    Initialization of a Gem outside of these two contexts is discouraged.

    Attributes:
        _name: User-friendly name representing the name of the created Gem. (e.g. "Diamond")
        _value: Monetary value when the gem is collected by the robot. Can be negative (for stage hazards).
    """    
    def __init__(self, name, text, color, value):
        """Constructs a new Gem."""
        super().__init__()
        self._name = name
        self._value = value
        self._text = text
        self._font_size = GlobalDefs.FONT_SIZE
        self._color = color
        self._velocity = Point(0, 5)

    def _gem_collected(self, cast):
        """Adds the Gem's value to the robot and notifies the player of the Gem's collected via the message actor.

        Called when the Gem hits the ground (in on_update), and is close enough to the robot to be collected.

        Args:
            cast (Cast): The current game's Cast of Actors.
        """        
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
        """Makes the gem fall through the air, destroying itself if it reaches the ground.

        Args:
            cast (Cast): The current game's Cast of Actors.
        """        
        robot = cast.get_first_actor("robot")
        if self._position.get_y() >= GlobalDefs.GROUND_Y:
            if self._check_robot_touching(robot):
                self._gem_collected(cast)
            cast.remove_actor("gems", self)
    
    def get_name(self):
        """Returns the user-friendly name of the Gem."""
        return self._name

    def get_value(self):
        """Returns the monetary value of the Gem."""
        return self._value

    def set_fall_speed(self, speed):
        """Sets the downward velocity of the Gem. Cannot be negative.
        
        Args:
            speed: Speed in pixels to fall each frame.
        """
        self._velocity = Point(0, abs(speed))

    def _check_robot_touching(self, robot):
        """Checks the proximity of the Gem to the robot character and determines whether the Gem can be collected.
        
        Args:
            robot (Robot): Actor representing the robot character.
        """
        return abs(self._position.get_x() - (robot.get_position().get_x() + GlobalDefs.CELL_SIZE)) <= GlobalDefs.CELL_SIZE * 2

class Opal(Gem):
    """A special, supervaluable Gem that flashes many colors while falling.

    Attributes:
        _timer: Frames until the color of the Opal changes. Reset continuously after every color change.
    """    
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
    """A special, supervaluable Gem that flashes purple then turns invisible while falling.

    Attributes:
        _timer: Frames until the color of the Obsidian changes. Advances through the COLOR_FRAMES list.
    """    
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

class Mythril(Gem):
    """A strange blue Gem that falls faster than other gems."""
 
    COLORS       = [ColorDefs.BLUE]
    COLOR_FRAMES = [20, 10]

    def __init__(self):
        super().__init__("Mythril", "*", Mythril.COLORS[0], 59999)
        self._timer = Mythril.COLOR_FRAMES[0]

    def set_fall_speed(self, speed):
        """Sets the downward velocity of the Gem. Cannot be negative.
        
        Args:
            speed: Speed in pixels to fall each frame.
        """
        "Sets speed to 8 regardless of speed passed in"
        self._velocity = Point(0, abs(speed))
        self._velocity = Point(0, 8 )


class GemDefs:
    """Definitions of various gems used by GemMaker."""
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
    MYTHRIL = Mythril()
    # Hazards
    PEBBLE = Gem("Pebble", "o", ColorDefs.GREY, -5000)
    GRAVEL = Gem("Gravel", "o", ColorDefs.SLATE, -10000)
    ROCK = Gem("Rock", "O", ColorDefs.GREY, -20000)
    BOULDER = Gem("Boulder", "O", ColorDefs.SLATE, -50000)