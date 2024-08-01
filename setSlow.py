import xarm
import time
import math
delay = .5 # in seconds
degreeOfMovement = 30
degreeOfAngle = 30.0

arm = xarm.Controller('USB')


# The following method simultaneously moves the position of two joints while having custom DOM for both.
def SimultaneousMoveNoAngleCustomDOMs(joint1, degree, joint2, angle, DOM1, DOM2):
    currentDegree = arm.getPosition(joint1)
    currentAngle = arm.getPosition(joint2)
    difference1 = degree - currentDegree
    difference2 = angle - currentAngle
    time1 = difference1 * 1.0 / DOM1
    time2 = difference2 * 1.0 / DOM2
    tempDegreeOfMovement = DOM1
    if currentDegree > degree:
        tempDegreeOfMovement *= -1
    tempDegreeOfAngle = DOM2
    if (currentAngle > angle):
        tempDegreeOfAngle *= -1
    longTime = max(abs(time1), abs(time2))
    for i in range(0, math.ceil(longTime)):
        newPosition = currentDegree + tempDegreeOfMovement
        if (tempDegreeOfMovement > 0 and newPosition > degree):
            newPosition = degree
        if (tempDegreeOfMovement < 0 and newPosition < degree):
            newPosition = degree 
        if (newPosition > 999):
            newPosition = 999
        if (newPosition < 0):
            newPosition = 0
        if (newPosition != currentDegree):
            arm.setPosition(joint1, newPosition)
        currentDegree = newPosition
        newAngle = currentAngle + tempDegreeOfAngle
        if (tempDegreeOfAngle > 0 and newAngle > angle):
            newAngle = angle
        if (tempDegreeOfAngle < 0 and newAngle < angle):
            newAngle = angle
        if (newAngle > 999):
            newAngle = 999
        if (newAngle < -0):
            newAngle = 0
        if (newAngle != currentAngle):
            arm.setPosition(joint2, newAngle)
        currentAngle = newAngle
        time.sleep(delay)

def SimultaneousMoveNoAngle(joint1, degree, joint2, angle):
    SimultaneousMoveNoAngleCustomDOMs(joint1, degree, joint2, angle, degreeOfMovement, degreeOfMovement)

def SimultaneousMoveNoAngleSecondCustomDOM(joint1, degree, joint2, angle, DOM2):
    SimultaneousMoveNoAngleCustomDOMs(joint1, degree, joint2, angle, degreeOfMovement, DOM2)

def SimultaneousMoveNoAngleFirstCustomDOM(joint1, degree, joint2, angle, DOM1):
    SimultaneousMoveNoAngleCustomDOMs(joint1, degree, joint2, angle, DOM1, degreeOfMovement)


def SimultaneousMove(joint1, degree, joint2, angle):
    currentDegree = arm.getPosition(joint1)
    currentAngle = arm.getPosition(joint2, True)
    difference1 = degree - currentDegree
    difference2 = angle - currentAngle
    time1 = abs(difference1 * 1.0 / degreeOfMovement)
    time2 = abs(difference2 / degreeOfAngle)
    tempDegreeOfMovement = degreeOfMovement
    if currentDegree > degree:
        tempDegreeOfMovement *= -1
    tempDegreeOfAngle = degreeOfAngle
    if (currentAngle > angle):
        tempDegreeOfAngle *= -1
    longTime = max(time1, time2)
    for i in range(0, math.ceil(longTime)):
        newPosition = currentDegree + tempDegreeOfMovement
        if (tempDegreeOfMovement > 0 and newPosition > degree):
            newPosition = degree
        if (tempDegreeOfMovement < 0 and newPosition < degree):
            newPosition = degree 
        if (newPosition > 999):
            newPosition = 999
        if (newPosition < 0):
            newPosition = 0
        if (newPosition != currentDegree):
            arm.setPosition(joint1, newPosition)
        currentDegree = newPosition
        newAngle = currentAngle + tempDegreeOfAngle
        if (tempDegreeOfAngle > 0 and newAngle > angle):
            newAngle = angle
        if (tempDegreeOfAngle < 0 and newAngle < angle):
            newAngle = angle
        if (newAngle > 125.0):
            newAngle = 125.0
        if (newAngle < -125.0):
            newAngle = -125.0
        arm.setPosition(joint2, newAngle)
        currentAngle = newAngle
        time.sleep(delay)

def setPositionSlow(joint, degree):
    current = arm.getPosition(joint)
    tempDegreeOfMovement = degreeOfMovement
    if current > degree:
        tempDegreeOfMovement *= -1
    for i in range(current, degree, tempDegreeOfMovement):
        arm.setPosition(joint, max(i + tempDegreeOfMovement, 1))
        time.sleep(delay)
    arm.setPosition(joint, degree)
    
def setPositionSlowCustomDOM(joint, degree, DOM):
    current = arm.getPosition(joint)
    tempDegreeOfMovement = DOM
    if current > degree:
        tempDegreeOfMovement *= -1
    for i in range(current, degree, tempDegreeOfMovement):
        arm.setPosition(joint, max(i + tempDegreeOfMovement, 1))
        time.sleep(delay)
    arm.setPosition(joint, degree)

def setDegreeSlow(joint, angle):
    servo = xarm.Servo(joint)
    current = servo.angle
    if current > angle:
        index = current
        while index > angle:
            arm.setPosition(joint, index - degreeOfAngle)
            time.sleep(delay)
            index -= degreeOfAngle
        arm.setPosition(joint, angle)
    else:
        index = current
        while index < angle:
            arm.setPosition(joint, index + degreeOfAngle)
            time.sleep(delay)
            index += degreeOfAngle
        arm.setPosition(joint, angle)
def getValidAngle(current, target):
    if (current == target):
        return target
    if (current < target):
        if (current + degreeOfAngle > target):
            return target
        else:
            return current + degreeOfAngle
    else:
        if (current - degreeOfAngle < target):
            return target
        else:
            return current - degreeOfAngle

# def setPositionSlowWithRotation(joint, degree, degreeOfRotation):
#     current = arm.getPosition(joint)
#     servo = xarm.Servo(2)
#     currentRotation = servo.angle
#     tempDegreeOfMovement = degreeOfMovement
#     if current > degree:
#         tempDegreeOfMovement *= -1
#     for i in range(current, degree, tempDegreeOfMovement):
#         arm.setPosition(joint, max(i + tempDegreeOfMovement, 1))
#         print(getValidAngle(currentRotation, degreeOfRotation))
#         arm.setPosition(1, getValidAngle(currentRotation, degreeOfRotation))
#         currentRotation = arm.getPosition(2)
#         time.sleep(delay)
#     arm.setPosition(joint, degree)
#     arm.setPosition(2, degreeOfRotation)