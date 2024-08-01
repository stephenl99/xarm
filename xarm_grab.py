import xarm
import time
from setSlow import setPositionSlow, setDegreeSlow, SimultaneousMove, SimultaneousMoveNoAngle

def grab():
    arm = xarm.Controller('USB')
    # setPositionSlow(4, 450)
    # time.sleep(2.5)
    setDegreeSlow(2, 90.0)
    time.sleep(2.5)
    # setPositionSlow(3, 400)
    # time.sleep(2.5)
    # setDegreeSlow(2, 0.0)
    # time.sleep(2.5)
    # setPositionSlow(3, 540)
    # time.sleep(2.5)
    SimultaneousMoveNoAngle(3,800, 4, 900)
    # SimultaneousMove(3, 640, 2, 0.0)
    time.sleep(2.5)
    
    SimultaneousMove(3, 995, 2, 0.0)
    time.sleep(2.5)
    setPositionSlow(4, 700)
    time.sleep(2.5)
    setPositionSlow(1, 490)
    time.sleep(2.5)
