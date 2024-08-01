import xarm
import time
from setSlow import setPositionSlow, setDegreeSlow, SimultaneousMove, SimultaneousMoveNoAngle, setPositionSlowCustomDOM
arm = xarm.Controller('USB')
def grab():
    setDegreeSlow(2, 0.0)
    time.sleep(2.5)
    setPositionSlow(3, 900)
    time.sleep(2.5)
    setPositionSlow(4, 70)
    time.sleep(2.5)
    setPositionSlowCustomDOM(1, 550, 10)
    time.sleep(2.5)
    setPositionSlow(4, 150)
    time.sleep(2.5)
    SimultaneousMove(6, 100, 2, 70.0)
    time.sleep(2.5)
    setPositionSlow(6, 500)
    time.sleep(2.5)
    setPositionSlow(4, 70)
    SimultaneousMove(4, 70, 2, 0.0)