import pyautogui
import time
import cv2
import numpy

times = 10000
while times > 0:
    obstacleInfo = pyautogui.screenshot(region = [pyautogui.position().x, pyautogui.position().y, 2, 1])
    obstacleInfo = numpy.array(obstacleInfo)
    obstacleInfo = cv2.cvtColor(obstacleInfo, cv2.COLOR_RGB2BGR)

    obstacleInfo1 = pyautogui.screenshot(region = [pyautogui.position().x, pyautogui.position().y, 1, 1])
    obstacleInfo1 = numpy.array(obstacleInfo1)
    obstacleInfo1 = cv2.cvtColor(obstacleInfo1, cv2.COLOR_RGB2BGR)
    print(str(pyautogui.position().x) + ", " + str(pyautogui.position().y))
    #print(str(obstacleInfo[0][0]) + ", " + str(obstacleInfo1[0]))
    time.sleep(1)

    10, 140
    590, 730