
# Now let's try and bring together what we've learned and have a bit of fun
import pygame as pg
import pymunk  
# We're going to need some random numbers
from random import randrange

# 1. Force the audio driver to do nothing, else game will crash when not using audio .
os.environ["SDL_AUDIODRIVER"] = "dummy"

# 2. Safely initialize everything (including display and freetype for fonts)
pygame.init()

pymunk.pygame_util.positive_y_is_up = False # need to tell Pymunk as Y increases, Pygame moves DOWN (else it assumes UP).

RESOLUTION = W, H = 1280, 1024
FPS = 60

surface = pg.display.set_mode(RESOLUTION)

clock = pg.time.Clock()
pg.display.set_caption('Fun with pygame and pymonk!')

#pymunk
draw_options = pymunk.pygame_util.DrawOptions (surface) # integrate Pymunk with Pygame's "Surface" (Pygame's rectangular area to draw on).                                                          #
space = pymunk.Space() # set up Pymunk's simulation space, and it's gravity.
space.gravity = 0, 2000

# define a Kine to act as our FLOOR for the Ball to bounce off.
# "segment_Shape" is just a line starting at 0, H (0,1024) ending at W, H (1280, 1024) with a thickness of 20.
segment_shape = pymunk.Segment(space.static_body, (0, H), (W, H), 20)

# add to the segment_shape elasticity to make the ball bounce off it.
segment_shape.elasticity = 0.8
segment_shape.friction = 0.5    # surface friction; a value of 0 means, objects will interact without influencing eachother at all
space.add(segment_shape)

# The following Method creates our ball (really just a circle), and with this Meythod we can easily make many more within the game loop by calling this Function.
def create_ball(space, pos, radius=60): # 'space' is our defined surface; 'pos' is (x, y) coordinates of the circle's center as a tuple e.g., (100, 100); then 'radius'.
    ball_mass, ball_radius = radius/5, radius
    ball_momentum = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_momentum)
    ball_body.position = pos
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    ball_shape.elasticity = 0.8
    ball_shape.friction = 0.5
    ball_shape.color = (randrange(0,255), randrange(0,255), randrange(0,255), 255) # random colour range
    space.add(ball_body, ball_shape)

# If width is 0 (default), the circle will be filled solid.
# If width is greater than 0, then its the thickness of the circular line (a hollow circle).

# =================================================================================================================================================================

# MAIN GAME LOOP

never_gonna_give_you_up = True

while never_gonna_give_you_up:
    surface.fill(pg.Color('black'))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            never_gonna_give_you_up = False

        # When user clicks left mouse button, a ball of random size and color is spawned on the location
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1: # button 1?  (left)
                create_ball(space, i.pos, randrange(10, 80)) # call Function "create_ball"; draw at position of the mouse click.

    space.step(1/FPS)               # these 2 lines of code ensures the pymunk engine ticks along nicely with Pymunk;
    space.debug_draw(draw_options) # i.e we “step” the engine forward relative to our frame update speed.;
                                     # . . . and then dump the output to our Pygame "(surface)" that we linked to Pymunk above in . . .
                                     # . . . "draw_options = pymunk.pygame_util.DrawOptions(surface)".

    pg.display.flip()
    clock.tick(FPS)
