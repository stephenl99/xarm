import xarm
import time
from setSlow import setDegreeSlow, setPositionSlow, SimultaneousMoveNoAngle, SimultaneousMove
from xarm_reset import reset
arm = xarm.Controller('USB')
def put_down():
    #Old
    # setPositionSlow(3, 540)
    # time.sleep(2.5)
    # setPositionSlow(1, 0)
    time.sleep(2.5)
    SimultaneousMoveNoAngle(4, 750, 3, 999)
    time.sleep(2.5)
    SimultaneousMove(4, 800, 2, 90.0)
    time.sleep(20)
arm.setPosition(3, 30.0, wait=True)
