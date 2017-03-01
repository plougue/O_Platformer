import pygame

class Character:
  'Base class for the playable character'
  def __init__(self, screen, characterName, spritePath, initialPosition=[0,0]):
  
    # General character arguments
    self.screen = screen
    self.name = characterName
    self.image = pygame.image.load(spritePath).convert_alpha()
    self.position = self.image.get_rect()
    self.position[0] = initialPosition[0]
    self.position[1] = initialPosition[1]
    self.lastFramePosition = self.position
    
    # X-movement related arguments 
    self.xSpeed = 0
    self.xMaxSpeed = 15
    self.xStartAcceleration = 3   # How much speed the first input gives
    self.xSlowDown = self.xMaxSpeed/25.0    # How quickly the character slows down
    self.xAcceleration = self.xMaxSpeed/20.0    # How quickly he accelerates
    
    # Gravity
    self.gravity = 0.5
    
    # Jump related arguments
    self.numberOfJumps = 2
    self.ySpeed = 0
    self.yMaxSpeed = 10
    self.jumpSpeed = 6    # Initial jump speed
    self.jumpAcceleration = 1/0.7   # How fast the character gains speed until maxJumpSpeed
    self.maxAccelerationFrames = 7
    self.accelerationFramesRemaining = 0
    self.canAccelerateJump = 1   # [BOOL] can the character accelerate his jump ? 
    self.remainingJumps = 0    # [BOOL] can the character jump ?
    self.nextJumpsRatio = 0.8   # How reduced is the speed given by the jumps after the first ?
    self.jumpFreze = 0   # The jump is frozen until the up command is cancelled
    self.direction = 'right'
    self.lookingDirection = 'right'
    
  #############################################################################
  ##    CHANGES THE STATE ACCORDINGLY IF A COLLISION OCCURS                  ##
  #############################################################################
  def DeclareCollision(self, directions):
    # The and . . .  prevents to be stuck
    if (directions['down'] and self.ySpeed > 0) or (directions['up'] and self.ySpeed < 0) :
      self.ySpeed = 0
    if directions['down']:
      self.remainingJumps = self.numberOfJumps
      self.canAccelerateJump = 0 
      self.accelerationFramesRemaining = self.maxAccelerationFrames
      print("touching the floor")


    # The and . . .  prevents to be stuck
    if (directions['left'] and self.xSpeed < 0)  or (directions['right'] and self.xSpeed > 0) : 
      self.xSpeed = 0
    # Basically, if the character falls down he loses a jump
    if self.remainingJumps == self.numberOfJumps and not(directions['down']): 
      self.remainingJumps = self.remainingJumps - 1
      print("falling !!")

  def blit(self): 
    self.screen.blit(self.image, self.position)
  def Move(self,movements, resolution):
    self.lastFramePosition = self.position
    ### X MOVEMENt MANAGEMENT
    if(movements['left']  and (not(movements['right']))):
      if(self.xSpeed >= 0):
        self.xSpeed -= self.xStartAcceleration
      self.xSpeed -= self.xAcceleration
    elif(movements['right'] and (not(movements['left']))):
      if(self.xSpeed <= 0):
        self.xSpeed += self.xStartAcceleration
      self.xSpeed += self.xAcceleration 
    elif(self.xSpeed > 0):
      self.xSpeed -= self.xSlowDown
      if(self.xSpeed < 0): # should never slow down as much as to change direction
        self.xSpeed = 0
    elif(self.xSpeed < 0):
      self.xSpeed += self.xSlowDown
      if(self.xSpeed > 0): # should never slow down as much as to change direction
        self.xSpeed = 0

    if(self.xSpeed > self.xMaxSpeed):
      self.xSpeed = self.xMaxSpeed
    if(self.xSpeed < -self.xMaxSpeed):
      self.xSpeed = -self.xMaxSpeed 
      
    ### JUMPING MANAGEMENT

    # Once you stop accelerating it's too late
    if not(movements['up']):
      self.jumpFreeze = 0
      if self.remainingJumps < self.numberOfJumps :
        self.canAccelerateJump = 0
        self.accelerationFramesRemaining = 0
    if self.accelerationFramesRemaining == 0:
      self.canAccelerateJump = 0
    if(movements['up'] and self.remainingJumps > 0 and not(self.canAccelerateJump) and not(self.jumpFreeze)):
      print("jumping (" + str(self.remainingJumps)+ ")")
      if (self.remainingJumps < self.numberOfJumps) :
        self.ySpeed = -self.nextJumpsRatio * self.jumpSpeed
      else :
        self.ySpeed = -self.jumpSpeed
      self.remainingJumps = self.remainingJumps - 1
      self.canAccelerateJump = 1 
      self.accelerationFramesRemaining = self.maxAccelerationFrames
      self.jumpFreeze = 1
    elif(movements['up'] and self.ySpeed < 0 and self.canAccelerateJump):
      self.ySpeed -= self.jumpAcceleration
      self.accelerationFramesRemaining = self.accelerationFramesRemaining - 1

    ## GRAVITY
    self.ySpeed += self.gravity
    
    ## MODIFY POSITION
    self.position = self.position.move(self.xSpeed,self.ySpeed) 
    if movements['right'] and self.lookingDirection == 'left':
      self.image = pygame.transform.flip(self.image, True, False)
      self.lookingDirection = 'right'
    if movements['left'] and self.lookingDirection == 'right':
      self.image = pygame.transform.flip(self.image, True, False)
      self.lookingDirection = 'left'
 
  
  def GetLastFramePosition(self):
    return self.lastFramePosition

  def GetPosition(self):
    return self.position
  
  def GetSize(self):
    return (self.image.get_width(), self.image.get_height())
  
  def SetPosition(self,newPosition):
    self.position = newPosition
