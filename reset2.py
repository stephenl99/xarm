import xarm
def reset():
    arm = xarm.Controller('USB')
    for i in range (1, 7):
        arm.setPosition(i, 0.0)
    arm.setPosition(5, 150)
    arm.setPosition(4, 150)
    arm.setPosition(3, 930)
    arm.setPosition(1, 0)

reset()