import pygame
from Sources.Pc import Pc
from Sources.Projectiles.PR_Stick import *

class PC_Luc(Pc):

  'Base class for Luc'

  def __init__(self, screen, initialPosition=[0,0]):
    Pc.__init__(self,screen, "Luc", initialPosition)

    # Attack related arguments
    self.attackFrameDuration = 10
    self.attackRemainingFrames = 0
    self.attackRefreshingFrameDuration = 60
    self.attackRefreshingRemainingFrames = 0

    self.stick = PR_Stick(self.screen, self.name)

    # X-movement related arguments 
    self.xMaxSpeed = 19
    self.xStartAcceleration = 3   # How much speed the first input gives
    self.xSlowDown = self.xMaxSpeed/10.0    # How quickly the character slows down
    self.xAcceleration = self.xMaxSpeed/23.0    # How quickly he accelerates
    
    # Gravity
    self.gravity = 0.55
    
    # Jump related arguments
    self.numberOfJumps = 3
    self.ySpeed = 0
    self.jumpSpeed = 10   # Initial jump speed
    self.jumpAcceleration = 0.6   # How fast the character gains speed until maxJumpSpeed
    self.maxAccelerationFrames = 10
    self.accelerationFramesRemaining = 0
    self.canAccelerateJump = 1   # [BOOL] can the character accelerate his jump ? 
    self.remainingJumps = 0    # [BOOL] can the character jump ?
    self.nextJumpsRatio = 0.9   # How reduced is the speed given by the jumps after the first ?
    self.jumpFreze = 0   # The jump is frozen until the up command is cancelled
    self.direction = 'left'
    self.lookingDirection = 'left'

    # General character arguments
    self.maxHp = 7
    self.currentHp = 7
 
  def Act(self, movements, projectileList):
    Pc.Act(self, movements, projectileList)
    if self.attackRefreshingRemainingFrames > 0 : 
      self.attackRefreshingRemainingFrames = self.attackRefreshingRemainingFrames - 1
    if not (self.stick.IsActive()) and self.stick in projectileList :
      projectileList.remove(self.stick)
      print("removing stick")
    characterSize = self.GetSize()
    stickPosition = [0,0]
    stickSize = self.stick.GetSize()
    if self.direction == 'right' :
      stickPosition[0] = self.position[0] + characterSize[0] 
    else :
      stickPosition[0] = self.position[0] - stickSize[0]
    stickPosition[1] = self.position[1] + 20
    self.stick.SetPosition(stickPosition)

  def Attack(self, projectileList) :
    characterSize = self.GetSize()
    if self.attackRefreshingRemainingFrames == 0:
      self.stick = PR_Stick(self.screen, self.name)
      stickDuration = self.attackFrameDuration
      stickPosition = [0,0]
      stickSize = self.stick.GetSize()
      if self.direction == 'right' :
        stickPosition[0] = self.position[0] + characterSize[0]
      else :
        stickPosition[0] = self.position[0] - stickSize[0]
      stickPosition[1] = self.position[1] + 20
      self.stick.SetPosition(stickPosition)
      self.stick.SetActive(True)
      self.stick.SetDuration(stickDuration)
      self.stick.SetDirection(self.direction)
      projectileList.append(self.stick)
      self.attackRefreshingRemainingFrames = self.attackRefreshingFrameDuration
    return 1

  def Die(self):
    self.stick.SetActive(False) 
    Pc.Die(self)
