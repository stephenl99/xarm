# The following driver will make the arm move as follows:
# Reset to baseline position
# Rotate 90 degrees and move down to grab ball
# rotate joint six whilst spinning grabber back and forth
# Object should be placed with center 9 cm from base of robot
from reset2 import reset
from grab4 import grab
import time
import xarm
arm = xarm.Controller('USB')
def main():
    reset()
    time.sleep(2.5)
    grab()
    time.sleep(2.5)
    reset()


main()