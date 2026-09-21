#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      badow
#
# Created:     17/07/2025
# Copyright:   (c) badow 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import pathlib
import pygame
import pygame.freetype  # for Fonts
pygame.display.init()
pygame.freetype.init()  # This uses a completely different, safer C path than init.font                                                           than pygame.font.init() 

pygame.display.set_caption("Hello Justin")  # <<-- will go into 'Title' of the PygBag generated .HTML file.

# import traceback   # for use with "Try" exception capture; uncomment if game not working properly

pathlib.Path(__file__).parent.resolve()  # needed for Android to find the .ttf files.
path = pathlib.Path(__file__).parent     # needed for Android to find the .ttf files.
print(f"Script Path: {path}")
# above prints:-
# Script Path: C:\DOWNLOADS\Build Android APK with COLAB\Hello   <<-- .ttf custom font file is within "Hello" directory.

# the following dimensions determine Portrait or landscape
base_width = 1280
base_height = 1280

# the following is the modern way of using the GPU and setting the screen size.
screen = pygame.display.set_mode((base_width, base_height), pygame.FULLSCREEN | pygame.SCALED | pygame.DOUBLEBUF, vsync=1)

GOLD = (255, 215, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


# to capture the Frames Per Second
clock = pygame.time.Clock()

while True:

  # pygame.time.delay(300)

  # try:     # all code in this block will be checked for an exception in processing
             # . . . the exception will be printed below using "except Exception: " at the end of the program
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()

    clock.tick(250)  # set the FPS rate; this must be here within the "while True" loop.

    font = pygame.freetype.Font('Lemon Days.ttf', 85) # freetype does NOT need os.path.abspath for Android.
    # font = pygame.font.Font(os.path.abspath(".")+'/Lemon Days.ttf', 85)   # <<-- for ANDROID & the Python Interpreter.
    #font = pygame.font.Font('C:\PYGAME\My Games\Hello\Lemon Days.ttf', 36)  #  <<-- for Nuitka & Python Interpreter.
    hardware_surface = font.render('Welcome to Pygame, Justin !', True, (GOLD))
    screen.blit(hardware_surface, (10, 100))
    #screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, 100)) # 100 is the Y co-ordinate

    font = pygame.freetype.Font('Skincake.ttf', 85) # freetype does NOT need os.path.abspath for Android.
    #font = pygame.font.Font(os.path.abspath(".")+'/Skincake.ttf', 85)   # <<-- for ANDROID & the Python Interpreter.
    #font = pygame.font.Font('C:\PYGAME\My Games\Hello\Skincake.ttf', 38) #  <<-- for Nuitka & Python Interpreter.
    hardware_surface = font.render(f'FPS =  {round(clock.get_fps(), 1)}', True, (RED)) # "1" means one decimal place
    screen.blit(hardware_surface, (10, 250))  # copies the surface object to the screen.

    # Draws the surface object to the screen.
    pygame.display.update()
    screen.fill((BLACK))    # without fill the screen the FPS display over eachother so looking fuzzy.



  # except Exception:   # exceptions/error messages will be captuted for all code within the Try block and prined here . . .
  #        print(traceback.format_exc())
                                        # . . . the messages are displayed only from the Nuitka .exe (python interpreter does NOT).
  # . . . to stop the messages scrolling, just click & hold the yellow bar of the exxception window display. . .
  # . . . the exception messages are displayed only from the Nuitka .exe (python interpreter does NOT).
