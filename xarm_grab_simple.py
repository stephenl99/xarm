import xarm
import time
from setSlow import setPositionSlow, setDegreeSlow

arm = xarm.Controller('USB')
def grab():
    # for i in range(1, 7):
    #     setPositionSlow(i, 0)
    #     setDegreeSlow(i, 0.0)
    setPositionSlow(4, 420)
    time.sleep(2.5)
    setPositionSlow(4, 500)
    time.sleep(2.5)
    setDegreeSlow(2, 90.0)
    time.sleep(2.5)
    setDegreeSlow(2, 0.0)

grab()