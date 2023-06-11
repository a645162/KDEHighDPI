import math


def getScreensScale(now, target):
    return round(math.sqrt(now * 1.0 / target), 1)


print(getScreensScale(175, 100))
