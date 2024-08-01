import xarm
import time
from setSlow import *
arm = xarm.Controller('USB')
def grab():
    SimultaneousMoveNoAngle(3, 840, 4, 90)
    SimultaneousMoveNoAngleCustomDOMs(1, 490, 2, 0, 100, 70)
    SimultaneousMoveNoAngleCustomDOMs(6, 300, 2, 500, 50, 100)
    SimultaneousMoveNoAngleCustomDOMs(6, 100, 2, 100, 50, 100)
    SimultaneousMoveNoAngleCustomDOMs(6, 300, 3, 900, 50, 15)
    SimultaneousMoveNoAngleCustomDOMs(6, 500, 3, 840, 50, 15)
    SimultaneousMoveNoAngleCustomDOMs(1, 0, 2, 500, 70, 70)


