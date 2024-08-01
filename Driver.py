from xarm_grab import grab
from xarm_reset import reset
from xarm_put_down import put_down
import xarm
import time
def main():
    reset()
    grab()
    put_down()
    reset()
main()