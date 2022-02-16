from game.casting.actor import Actor
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
SCORE_Y = int((ROWS - 2) * CELL_SIZE)
GROUND_Y = int((ROWS - 4) * CELL_SIZE)
GROUND_CHARS = 106
CAPTION = "Greeed!!"
WHITE = Color(255, 255, 255)


def main():
    
    # create the cast
    cast = Cast()
    
    # create score
    score = Actor()
    score.set_text("")
    score.set_font_size(FONT_SIZE)
    score.set_color(WHITE)
    score.set_position(Point(CELL_SIZE, SCORE_Y))
    cast.add_actor("score", score)

    # create "ground"
    ground = Actor()
    ground.set_text("_" * GROUND_CHARS)
    ground.set_color(WHITE)
    ground.set_position(Point(0, GROUND_Y))
    cast.add_actor("ground", ground)
    
    # create the robot
    x = int(MAX_X / 2)
    y = GROUND_Y
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robot", robot)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()