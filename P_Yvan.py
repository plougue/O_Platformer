import pygame
from Pc import Pc

class P_Yvan(Pc):

  'Base class for Yvan'

  def __init__(self, screen, initialPosition=[0,0]):
    Pc.__init__(self,screen, "Yvan", initialPosition)
    # X-movement related arguments 
    self.xMaxSpeed = 15
    self.xStartAcceleration = 4   # How much speed the first input gives
    self.xSlowDown = self.xMaxSpeed/30.0    # How quickly the character slows down
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