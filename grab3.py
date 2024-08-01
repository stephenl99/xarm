import xarm
import time
from setSlow import setPositionSlow, setDegreeSlow, SimultaneousMove, SimultaneousMoveNoAngle, setPositionSlowCustomDOM
arm = xarm.Controller('USB')
def grab():
    setDegreeSlow(2, 0.0)
    # time.sleep(5)
    setPositionSlow(3, 900)
    # time.sleep(5)
    setPositionSlow(4, 70)
    # time.sleep(5)
    setPositionSlow(3, 810)
    # time.sleep(5)
    setPositionSlowCustomDOM(1, 550, 150)

    setPositionSlowCustomDOM(3, 850, 20)
    # setPositionSlow(4, 50)
   
    # time.sleep(5)
    # setPositionSlow(4, 150)
    # time.sleep(5)
    # setDegreeSlow(2, 70.0)
    # time.sleep(2.5)
    # setPositionSlow(6, 100)
    SimultaneousMove(6, 400, 2, 70.0)
    setPositionSlowCustomDOM(6, 100, 100)
    # time.sleep(5)
    setPositionSlowCustomDOM(6, 500, 100)
    # time.sleep(5)
    # setPositionSlow(4, 70)
    # time.sleep(5)
    SimultaneousMove(4, 70, 2, 0.0)

    setPositionSlowCustomDOM(1, 0, 150)
    # time.sleep(5)