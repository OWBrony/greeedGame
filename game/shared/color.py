class Color:
    """A color.

    The responsibility of Color is to hold and provide information about itself. Color has a few 
    convenience methods for comparing them and converting to a tuple.

    Attributes:
        _red (int): The red value.
        _green (int): The green value.
        _blue (int): The blue value.
        _alpha (int): The alpha or opacity.
    """
    
    def __init__(self, red, green, blue, alpha = 255):
        """Constructs a new Color using the specified red, green, blue and alpha values. The alpha 
        value is the color's opacity.
        
        Args:
            red (int): A red value.
            green (int): A green value.
            blue (int): A blue value.
            alpha (int): An alpha or opacity.
        """
        self._red = red
        self._green = green
        self._blue = blue 
        self._alpha = alpha

    def to_tuple(self):
        """Gets the color as a tuple of four values (red, green, blue, alpha).

        Returns:
            Tuple(int, int, int, int): The color as a tuple.
        """
        return (self._red, self._green, self._blue, self._alpha)   

class ColorDefs:
    # Basic Colors
    WHITE = Color(255, 255, 255)
    BLACK = Color(0,0,0)
    RED = Color(255,0,0)
    LIME = Color(0,255,0)
    BLUE = Color(0,0,255)
    YELLOW = Color(255,255,0)
    CYAN = Color(0,255,255)
    MAGENTA = Color(255,0,255)
    SILVER = Color(192,192,192)
    GREY = Color(128,128,128)
    MAROON = Color(128,0,0)
    GREEN = Color(0,128,0)
    NAVY = Color(0,0,128)
    OLIVE = Color(128,128,0)
    TEAL = Color(0,128,128)
    PURPLE = Color(128,0,128)
    ORANGE = Color(255,165,0)
    # Gem Colors
    GARNET = Color(220,20,60)
    CORAL = Color(255,127,80)
    PERIDOT = Color(154,205,50)
    AQUAMARINE = Color(127,255,212)
    TOPAZ = Color(244,164,96)
    AMETHYST = Color(75,0,130)
    TURQUOISE = Color(64,224,208)
    ZIRCON = Color(95,158,160)
    ROSEQUARTZ = Color(255,182,193)
