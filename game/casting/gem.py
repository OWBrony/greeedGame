from game.casting.actor import Actor

from game.shared.color import ColorDefs

class Gem(Actor):
    def __init__(self, name, text, color, value):
        super().__init__()
        self._name = name
        self._value = value
        self._text = text
        self._color = color

    # Stub, can be overridden by subclasses.
    def on_collect(self, cast):
        pass

    # Stub, can be overridden by subclasses.
    def on_update(self, cast):
        pass
    
    def get_name(self):
        return self._name

    def get_value(self):
        return self._value

class GemDefs:
    # Treasure
    SILVER = Gem("Silver", "s", ColorDefs.SILVER, 500)
    GOLD = Gem("Gold", "g", ColorDefs.YELLOW, 1000)
    CORAL = Gem("Coral", "c", ColorDefs.CORAL, 1500)
    ROSEQUARTZ = Gem("Rose Quartz", "r", ColorDefs.ROSEQUARTZ, 2000)
    AQUAMARINE = Gem("Aquamarine", "a", ColorDefs.AQUAMARINE, 2500)
    GARNET = Gem("Garnet", "G", ColorDefs.GARNET, 3000)
    PERIDOT = Gem("Peridot", "P", ColorDefs.PERIDOT, 3750)
    ZIRCON = Gem("Zircon", "Z", ColorDefs.ZIRCON, 4500)
    CITRINE = Gem("Citrine", "C", ColorDefs.ORANGE, 5000)
    AMETHYST = Gem("Amethyst", "A", ColorDefs.AMETHYST, 5750)
    TOPAZ = Gem("Topaz", "T", ColorDefs.TOPAZ, 6250)
    SAPPHIRE = Gem("Sapphire", "S", ColorDefs.BLUE, 7000)
    RUBY = Gem("Ruby", "R", ColorDefs.RED, 7500)
    EMERALD = Gem("Emerald", "E", ColorDefs.LIME, 8250)
    DIAMOND = Gem("Diamond", "D", ColorDefs.WHITE, 10000)
    # TODO Opal - Multicolored supervaluable gem. Needs its own class to override on_update.
    # Hazards
    PEBBLE = Gem("Pebble", "x", ColorDefs.GREY, -2000)
    GRAVEL = Gem("Gravel", "x", ColorDefs.SLATE, -3500)
    ROCK = Gem("Rock", "X", ColorDefs.GREY, -5000)
    BOULDER = Gem("Boulder", "X", ColorDefs.SLATE, -10000)
    # TODO: Powerups?
