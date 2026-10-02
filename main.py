
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      badow
#
# Created:     20/09/2025
# Copyright:   (c) badow 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import  pygame, random, sys
import pathlib
import os

pygame.init()

pathlib.Path(__file__).parent.resolve()  # needed for Android to find the .ttf files.
path = pathlib.Path(__file__).parent     # needed for Android to find the .ttf files.

GOLD = (255, 215, 0)# the following dimensions determine Portrait or landscape
base_width = 1280
base_height = 1280

# For Android phone use the following for Full Screen:-
screen = pygame.display.set_mode((base_width, base_height), pygame.FULLSCREEN | pygame.SCALED)

RED = (255, 0, 0)
BLACK = (0, 0, 0)

#set up for GPU rendering
# this really works ! On mobile I was getting maximum FPS = 55 but now getting FPS = 89-90 consistently.
screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)
hardware_surface = pygame.Surface(size, pygame.HWSURFACE | pygame.DOUBLEBUF)

win = pygame.display.set_mode(size)
pygame.display.set_caption('StarField')
clock = pygame.time.Clock()

font = pygame.font.Font(os.path.abspath(".")+'/Skincake.ttf', 56)   # <<-- for ANDROID & the Python Interpreter.

MY_TIMER_EVENT = pygame.USEREVENT + 0
pygame.time.set_timer(MY_TIMER_EVENT, 1000)  # triggers every 1000 milliseconds (1 second); this must be outside the game loop.

class Star:
    def __init__(self):
        self.x, self.y, self.z = random.randint(-width, width), random.randint(-height, height), random.randint(-width, width)

    def draw(self, win):
        sx = maps((self.x)/self.z, 0, 1, 0, width)
        sy = maps((self.y)/self.z, 0, 1, 0, height)
        r = maps(self.z, 0, width, 6, 0)
        pygame.draw.circle(win, (255, 255, 255), (int(sx+width/2), int(sy+height/2)), r)

    def update(self, x, y):
        sz = maps((x+y), 0, width+height, 1, 8)
        self.z -= sz
        if self.z < 1:
            self.x, self.y, self.z = random.randint(-width, width), random.randint(-height, height), random.randint(1, width)


def maps(num, in_min, in_max, out_min, out_max):
    return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

stars = []
for i in range(500):
    s = Star()
    stars.append(s)

clock = pygame.time.Clock()

while True:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
        """
        elif event.type == MY_TIMER_EVENT:
             font = pygame.font.Font('C:\PYGAME\My Games\Hello\Skincake.ttf', 38) #  <<-- for Nuitka & Python Interpreter.
             hardware_surface = font.render(f'FPS =  {round(clock.get_fps(), 1)}', True, (RED)) # "1" means one decimal place
             #hardware_surface = font.render(f'ONE second has passed),)', True, (RED)) # "1" means one decimal place
             screen.blit(hardware_surface, (10, 150))  # copies the surface object to the screen.
             pygame.display.update()
             print("1 second has passed!")

        NOTE: *** The above 'elif' works to render the display every second on the screen.
        BUT the trouble is it just flashes on the screen so momentarily you can hardly see it !
        This is because INSIDE the 'elif' the code is NOT executed each game loop but only once a second has passed and then only fleetingly,
        because it then goes round the rest of the Game Loop whereby the screen is cleared.
        So better to display the Frames Per Second within the Game Loop where it gets executed constantly for a steady display !
        """


    win.fill((0, 0, 0))

    for s in stars:
        s.update(*pygame.mouse.get_pos())
        s.draw(win)

    clock.tick(120) # DO NOT SET THE CLOCK TOO FAST else the displayed FPS increments too fast to read the numbers !!!

    # the following is the correct place to display the FPS, as it gets executed every cycle of the Game Loop and so stays on the screen!
    #font = pygame.font.Font('C:\PYGAME\My Games\Hello\Skincake.ttf', 38) #  <<-- for Nuitka & Python Interpreter.
    font = pygame.font.Font(os.path.abspath(".")+'/Skincake.ttf', 56)   # <<-- for ANDROID & the Python Interpreter.
    hardware_surface = font.render(f'FPS =  {round(clock.get_fps(), 1)}', True, (RED)) # "1" means one decimal place
    screen.blit(hardware_surface, (10, 30))  # copies the surface object to the screen.

    pygame.display.flip()



