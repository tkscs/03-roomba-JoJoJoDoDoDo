# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. Ido ---- REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 4 version of the room
window = room.draw_room(level = 4, n_alcoves = 1, radius = 5)

###
# Start your code here

forward(400)
left(180)
forward(40)
left(90)
forward(120)
right(90)
forward(40)
left(90)
forward(40)
right(90)
forward(120)
left(90)
forward(40)
left(180)
forward(40)
left(90)
forward(120)
right(90)
forward(40)
left(90)
forward(40)
right(90)
forward(240)
right(90)
forward(40)
left(90)
forward(40)
right(90)
forward(120)
left(90)
forward(40)
left(180)
forward(40)
left(90)
forward(120)
right(90)
forward(40)
left(90)
forward(40)
right(90)
forward(80)
right(90)
forward(280)
right(90)
forward(40)
right(90)
forward(240)
left(180)
forward(40)
right(90)
forward(40)
left(90)
forward(160)
left(450 + 1080)
forward(160)
right(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
right(90)
forward(40)
left(450)
forward(160)
left(90)
forward(40)
right(90)
forward(40)
left(450)
forward(40)
left(90)
forward(160)
left(90)
forward(40)
left(90)
forward(40)
left(360 * 10)
forward(40)
left(90)
forward(240)
left(90)
forward(40)
right(90)
forward(80)
left(90)
forward(40)
right(90)
forward(40)
left(90)
forward(40)
right(180)
forward(40)
left(90)
forward(40)
right(90)
forward(40)
left(90)
forward(40)
left(180)
forward(40)
left(90)
forward(40)
right(90)
forward(40)
left(90)
forward(40)
left(180)
forward(40)
left(90)
forward(40)
right(90)
forward(40)
right(90 + 360 * 5)
forward(40)
left(360 * 360)









































 
# End your code here
###
 
window.exitonclick()