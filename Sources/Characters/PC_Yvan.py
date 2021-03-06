import pygame
from Sources.Projectiles.PR_Shuriken import *
from Sources.Pc import Pc

class PC_Yvan(Pc):

  'Base class for Yvan'

  def __init__(self, screen, initialPosition=[0,0]):
    Pc.__init__(self,screen, "Yvan", initialPosition)
    
    # ATTACK RELATED ARGUMENTS
    self.attackRefreshingFrameDuration = 15
    self.attackRefreshingRemainingFrames = 0 

    # X-movement related arguments 
    self.xMaxSpeed = 16.5
    self.xStartAcceleration = 2   # How much speed the first input gives
    self.xSlowDown = self.xMaxSpeed/15.0    # How quickly the character slows down
    self.xAcceleration = self.xMaxSpeed/17.0    # How quickly he accelerates
    
    # Gravity
    self.gravity = 0.55
    
    # Jump related arguments
    self.numberOfJumps = 1
    self.ySpeed = 0
    self.jumpSpeed = 11    # Initial jump speed
    self.jumpAcceleration = 1.3   # How fast the character gains speed until maxJumpSpeed
    self.maxAccelerationFrames = 14
    self.accelerationFramesRemaining = 0
    self.canAccelerateJump = 1   # [BOOL] can the character accelerate his jump ? 
    self.remainingJumps = 0    # [BOOL] can the character jump ?
    self.nextJumpsRatio = 0.7   # How reduced is the speed given by the jumps after the first ?
    self.jumpFreze = 0   # The jump is frozen until the up command is cancelled
    self.direction = 'left'
    self.lookingDirection = 'left'

    # General character arguments
    self.maxHp = 4
    self.currentHp = 4

  def Attack(self, projectileList):
    if self.attackRefreshingRemainingFrames == 0 :
      shurikenPosition = [0,0]
      characterSize = self.GetSize()
      shurikenPosition[1] = self.position[1] + 20
      if self.direction == 'left' :
        shurikenPosition[0] = self.position[0] - characterSize[0] / 2
      else :
        shurikenPosition[0] = self.position[0] + characterSize[0] / 2
      shuriken = PR_Shuriken(self.screen, self.name, self, self.direction)
      projectileList.append(shuriken)
      self.attackRefreshingRemainingFrames = self.attackRefreshingFrameDuration 
  
  def Move(self, movements) :
    if self.attackRefreshingRemainingFrames > 0 :
      self.attackRefreshingRemainingFrames = self.attackRefreshingRemainingFrames - 1
    Pc.Move(self, movements)

    
