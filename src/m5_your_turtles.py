"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Emily Dougherty.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

Elle = rg.SimpleTurtle('turtle')
Elle.pen = rg.Pen('pink', 2)
Elle.speed = 20

size1 = 300

Emmett = rg.SimpleTurtle('turtle')
Emmett.speed = 15

size2 = 15

for k in range(8):
    Elle.draw_square(size1)

    Elle.pen_up()
    Elle.right(45)
    Elle.forward(15)
    Elle.left(45)

    Elle.pen_down()
    size1 = (size1 - 15)

for a in range(8):
    Emmett.draw_circle(size2)

    Emmett.pen_up()
    Emmett.left(60)
    Emmett.forward(15)
    Emmett.right(60)

    Emmett.pen_down()
    size2 = (size2 + 15)

window.close_on_mouse_click()
