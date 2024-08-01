from reset2 import reset
from grab3 import grab
import time
import xarm
arm = xarm.Controller('USB')
def main():
    reset()
    # time.sleep(20)
    # time.sleep(2.5)
    grab()
    # time.sleep(2.5)
    reset()
main()  