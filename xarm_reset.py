import xarm
def reset():
    arm = xarm.Controller('USB')
    for i in range (1, 7):
        arm.setPosition(i, 0.0)
    arm.setPosition(i, 500)
    arm.setPosition(6, 0.0)
    arm.setPosition(1, 0)
    arm.setPosition(3, 100)
    arm.setPosition(4, 300)
    arm.setPosition(4, 700)
    arm.setPosition(3, 350)
    #arm.setPosition(2, 90.0)
reset()