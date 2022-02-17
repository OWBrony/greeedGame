from global_defs import GlobalDefs

from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.robot import Robot

from game.directing.director import Director
from game.directing.gem_maker import GemMaker

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import ColorDefs
from game.shared.point import Point

def main():
    
    # create the cast
    cast = Cast()
    
    # create score
    score = Actor()
    score.set_text("")
    score.set_font_size(GlobalDefs.FONT_SIZE)
    score.set_color(ColorDefs.WHITE)
    score.set_position(Point(GlobalDefs.CELL_SIZE, GlobalDefs.SCORE_Y))
    cast.add_actor("score", score)

    # create message
    message = Actor()
    message.set_text("")
    message.set_font_size(GlobalDefs.FONT_SIZE)
    message.set_color(ColorDefs.WHITE)
    message.set_position(Point(int(GlobalDefs.CELL_SIZE * (GlobalDefs.COLS / 3)), GlobalDefs.SCORE_Y))
    cast.add_actor("message", message)

    # create "ground"
    ground = Actor()
    ground.set_text("_" * (GlobalDefs.COLS + 2))
    ground.set_font_size(GlobalDefs.GROUND_FONT_SIZE)
    ground.set_color(ColorDefs.WHITE)
    ground.set_position(Point(0, GlobalDefs.GROUND_Y))
    cast.add_actor("ground", ground)
    
    # create the robot
    robot = Robot()
    cast.add_actor("robot", robot)
    
    # start the game
    keyboard_service = KeyboardService(GlobalDefs.CELL_SIZE)
    video_service = VideoService(GlobalDefs.CAPTION, GlobalDefs.MAX_X, 
        GlobalDefs.MAX_Y, GlobalDefs.CELL_SIZE, GlobalDefs.FRAME_RATE)
    gem_maker = GemMaker()
    director = Director(keyboard_service, video_service, gem_maker)
    director.start_game(cast)


if __name__ == "__main__":
    main()
