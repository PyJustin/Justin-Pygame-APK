[app]

# (str) Title of your game; capital letters and spaces are allowed, but no special characters.
title = Fun with Pymunk

# the name of your game; one word only.
# only lowercase ASCII characters (a-z) and numbers (0-9).
package.name = myappfunwithpymunk

# this is to identify you or your company. 
package.domain = com.mycompany

# (str) Source code where the main.py live
source.dir = .

# (str) Icon of the application
icon.filename = Pygame icon.png

# (list) Source files to include (must include 'ttf' for custom fonts)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png,data/*.png, sound

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# Fixed requirements layout ensuring all low-level C wrappers and dependencies compile in correct sequence.
requirements = python3, hostpython3, libffi, cffi, pygame-ce, pyjnius, pymunk

# Keep this line - Buildozer automatically downloads, compiles, and links the CORRECT native C/C++ SDL2 binaries.
p4a.bootstrap = sdl2

# (list) Supported orientations
orientation = landscape

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (list) Android Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 35

# (int) Minimum API your APK / AAB will support.
android.minapi = 31

