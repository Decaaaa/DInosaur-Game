import gym
from gym import error, spaces, utils
import gym.spaces
import gym.spaces.space
from gym.utils import seeding

import numpy
import pyautogui
import cv2

import time

class DinoEnv(gym.Env):
  metadata = {'render.modes': ['None']}
  pyautogui.FAILSAFE = False
  speed = 0

  def __init__(self):
    self.observation_space = spaces.Discrete(4)
    self.action_space = spaces.Discrete(2)
    return
  
  def step(self, action):
    #print("action: " + str(action))
    if(action == 1): pyautogui.press("up")

    self.speed += 0.01
    reward = self.speed
    
    obstacleInfo = pyautogui.screenshot(region = [10, 590, 130, 140])
    obstacleInfo = numpy.array(obstacleInfo)
    obstacleInfo = cv2.cvtColor(obstacleInfo, cv2.COLOR_RGB2BGR)
    obstacleInfo = cv2.cvtColor(obstacleInfo, cv2.COLOR_BGR2GRAY)

    jumpOverNothing = 1
    for row in obstacleInfo:
      for pixel in row:
        if pixel < 100:
          jumpOverNothing = 0
          break
    if(jumpOverNothing == 1):
      reward = -100
    else:
      reward += 20

    grayBools = []
    for i in range(3):
      obstacleInfo = pyautogui.screenshot(region = [150, 550 + (80 * i), 300, 1])
      obstacleInfo = numpy.array(obstacleInfo)
      obstacleInfo = cv2.cvtColor(obstacleInfo, cv2.COLOR_RGB2BGR)
      obstacleInfo = cv2.cvtColor(obstacleInfo, cv2.COLOR_BGR2GRAY)
      for pixel in obstacleInfo[0]:
          if(pixel < 100): grayBools.append(1)
          else: grayBools.append(0)
    
    nextObstacle = -1
    highBird = 0
    for i in range(2):
      for j in range(300):
        if(nextObstacle != -1 and j > nextObstacle): break
        if(grayBools[j+(300*(i+1))] == 1): 
          if(nextObstacle == -1): nextObstacle = j
          elif(nextObstacle > j): nextObstacle = j
          break
    for i in range(300):
      if(grayBools[i] == 1): 
        highBird = 1
        break
    stateInfo = [self.speed, nextObstacle, jumpOverNothing, highBird]

    #print("\n" + str(self.speed))
    print("\n" + str(nextObstacle))

    try:
      endGame = pyautogui.locateOnScreen('./end_game.png', grayscale = True) != None
    except:
      endGame = False

    if(endGame): reward = -100

    return (numpy.ndarray(stateInfo), reward, endGame, {})
  
  def reset(self):
    obstacleInfo = pyautogui.screenshot(region = [10, 590, 130, 140])
    obstacleInfo = numpy.array(obstacleInfo)
    obstacleInfo = cv2.cvtColor(obstacleInfo, cv2.COLOR_RGB2BGR)
    obstacleInfo = cv2.cvtColor(obstacleInfo, cv2.COLOR_BGR2GRAY)

    jumpOverNothing = 1
    for row in obstacleInfo:
      for pixel in row:
        if pixel < 100:
          jumpOverNothing = 0
          break

    grayBools = []
    for i in range(3):
      obstacleInfo = pyautogui.screenshot(region = [150, 550 + (80 * i), 300, 1])
      obstacleInfo = numpy.array(obstacleInfo)
      obstacleInfo = cv2.cvtColor(obstacleInfo, cv2.COLOR_RGB2BGR)
      obstacleInfo = cv2.cvtColor(obstacleInfo, cv2.COLOR_BGR2GRAY)
      for pixel in obstacleInfo[0]:
          if(pixel < 100): grayBools.append(1)
          else: grayBools.append(0)
    
    nextObstacle = -1
    highBird = 0
    for i in range(2):
      for j in range(300):
        if(nextObstacle != -1 and j > nextObstacle): break
        if(grayBools[j+(300*(i+1))] == 1): 
          if(nextObstacle == -1): nextObstacle = j
          elif(nextObstacle > j): nextObstacle = j
          break
    for i in range(300):
      if(grayBools[i] == 1): 
        highBird = 1
        break
    stateInfo = [self.speed, nextObstacle, jumpOverNothing, highBird]

    self.speed = 0

    pyautogui.press("space")

    time.sleep(4)

    return numpy.ndarray(stateInfo)
  
  def render(self, mode='None', close=False):
    return