import sys

# Colors will not be diplayed on windows or macOS machines
colors = True
platf = sys.platform
if platf.lower().startswith(("os", "win", "darwin","ios")): 
    colors = False

if not colors:
	green = red = blue = white = reset = ""

else:                                                 
    white = "\033[97m"
    red = "\033[91m"
    blue = "\033[34m"
    green = "\033[92m"
    reset = "\033[0m"
