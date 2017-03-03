import pygame
from PR_Shuriken import *

from Pc import Pc

class PC_Yvan(Pc):

  'Base class for Yvan'

  def __init__(self, screen, initialPosition=[0,0]):
    Pc.__init__(self,screen, "Yvan", initialPosition)
    
    # ATTACK RELATED ARGUMENTS
    self.attackRefreshingFrameDuration = 15
    self.attackRefreshingRemainingFrames = 0 

    # X-movement related arguments 
    self.xMaxSpeed = 15
    self.xStartAcceleration = 4   # How much speed the first input gives
    self.xSlowDown = self.xMaxSpeed/15.0    # How quickly the character slows down
    self.xAcceleration = self.xMaxSpeed/15.0    # How quickly he accelerates
    
    # Gravity
    self.gravity = 1.2
    
    # Jump related arguments
    self.numberOfJumps = 1
    self.ySpeed = 0
    self.jumpSpeed = 25    # Initial jump speed
    self.jumpAcceleration = 0.6   # How fast the character gains speed until maxJumpSpeed
    self.maxAccelerationFrames = 10
    self.accelerationFramesRemaining = 0
    self.canAccelerateJump = 1   # [BOOL] can the character accelerate his jump ? 
    self.remainingJumps = 0    # [BOOL] can the character jump ?
    self.nextJumpsRatio = 0.5   # How reduced is the speed given by the jumps after the first ?
    self.jumpFreze = 0   # The jump is frozen until the up command is cancelled
    self.direction = 'left'
    self.lookingDirection = 'left'

    # General character arguments
    self.maxHp = 3
    self.currentHp = 3

  def Attack(self, projectileList):
    if self.attackRefreshingRemainingFrames == 0 :
      shurikenPosition = [0,0]
      characterSize = self.GetSize()
      shurikenPosition[1] = self.position[1] + 20
      if self.direction == 'left' :
        shurikenPosition[0] = self.position[0]
      else :
        shurikenPosition[0] = self.position[0] + characterSize[0]
      shuriken = PR_Shuriken(self.screen, self.name, shurikenPosition, self.direction)
      projectileList.append(shuriken)
      self.attackRefreshingRemainingFrames = self.attackRefreshingFrameDuration 
  
  def Move(self, movements, resolution) :
    if self.attackRefreshingRemainingFrames > 0 :
      self.attackRefreshingRemainingFrames = self.attackRefreshingRemainingFrames - 1
    Pc.Move(self, movements, resolution)
    
