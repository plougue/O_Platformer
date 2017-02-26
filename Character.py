import pygame

class Character:
  'Base class for the playable character'
  def __init__(self, screen, characterName, spritePath):
  
    # General character arguments
    self.screen = screen
    self.name = characterName
    self.image = pygame.image.load(spritePath).convert_alpha()
    self.position = self.image.get_rect()
    
    # X-movement related arguments 
    self.xSpeed = 0
    self.xMaxSpeed = 15
    self.xStartAcceleration = 3   # How much speed the first input gives
    self.xSlowDown = self.xMaxSpeed/25.0    # How quickly the character slows down
    self.xAcceleration = self.xMaxSpeed/20.0    # How quickly he accelerates
    
    # Gravity
    self.gravity = 0.5
    
    # Jump related arguments
    self.ySpeed = 0
    self.yMaxSpeed = 10
    self.jumpSpeed = 6    # Initial jump speed
    self.jumpAcceleration = 2   # How fast the character gains speed until maxJumpSpeed
    self.maxJumpSpeed = 12
    self.maxJumpSpeedReached = 1   # [BOOL] has the character reached his max speed (then he no longers accelerates)
    self.canJump = 0    # [BOOL] can the character jump ?
    self.direction = 'right'
    
  #############################################################################
  ##    CHANGES THE STATE ACCORDINGLY IF A COLLISION OCCURS                  ##
  #############################################################################
  def DeclareCollision(self, directions):
    if directions['down'] or directions['up']:
      self.ySpeed = 0
    if directions['down']:
      self.canJump = 1
      self.maxJumpSpeedReached = 0
    if directions['left'] or directions['right']:
      self.xSpeed = 0

  def blit(self): 
    self.screen.blit(self.image, self.position)
  def Move(self,movements, resolution):
    ### X MOVEMENt MANAGEMENT
    if(movements['left']  and (not(movements['right']))):
      if(self.xSpeed > 0):
        self.xSpeed -= self.xStartAcceleration
      self.xSpeed -= self.xAcceleration
    elif(movements['right'] and (not(movements['left']))):
      if(self.xSpeed < 0):
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
    if(movements['up'] and self.ySpeed == 0 and self.canJump):
      self.ySpeed = -self.jumpSpeed
    elif(movements['up'] and self.ySpeed < 0 and not(self.maxJumpSpeedReached)):
      self.ySpeed -= self.jumpAcceleration
      self.canJump = 0

    if(self.ySpeed < -self.maxJumpSpeed):
      self.ySpeed = - self.maxJumpSpeed
      self.maxJumpSpeedReached = 1

    ## GRAVITY
    self.ySpeed += self.gravity
    
    ## MODIFY POSITION
    self.position = self.position.move(self.xSpeed,self.ySpeed) 
    
  

  def GetPosition(self):
    return self.position
  
  def GetSize(self):
    return (self.image.get_width(), self.image.get_height())
  
  def SetPosition(self,newPosition):
    self.position = newPosition
