import pygame
from Character import Character

class Pc(Character):

  'Base class for the playable character'

  def __init__(self, screen, characterName):
 
    Character.__init__(self, screen, characterName, "Sprites/Characters/Pc/" + characterName + "/" + characterName + "_idle.png")
    # General character arguments
    self.image = pygame.image.load("Sprites/Characters/Pc/" + self.name + "/" + self.name + "_idle.png").convert()
    self.image.set_colorkey([34,177,76])
    self.position = self.image.get_rect()
    self.direction = 'left'
  def Move(self,movements,resolution):
    Character.Move(self,movements,resolution)
    if movements['right'] and self.direction == 'left':
      self.image = pygame.transform.flip(self.image, True, False)
      self.direction = 'right'
    if movements['left'] and self.direction == 'right':
      self.image = pygame.transform.flip(self.image, True, False)
      self.direction = 'left'
'''    
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


  ###################################################################################
  ##                       BLITS THE IMAGE TO THE SCREEN                           ##
  ###################################################################################
  def blit(self): 
    self.screen.blit(self.image, self.position)


  ###################################################################################
  ##                       ISSUES THE PLAYER MOVEMENT                              ##
  ###################################################################################
  def Move(self,movementKeys, resolution):
    ### X MOVEMENt MANAGEMENT
    if(movementKeys['left']  and (not(movementKeys['right']))):
      if(self.xSpeed > 0):
        self.xSpeed -= self.xStartAcceleration
      self.xSpeed -= self.xAcceleration
    elif(movementKeys['right'] and (not(movementKeys['left']))):
      if(self.xSpeed < 0):
        self.xSpeed += self.xStartAcceleration
      self.xSpeed += self.xAcceleration 
    elif(self.xSpeed > 0):
      self.xSpeed -= self.xSlowDown
      if(self.xSpeed < 0): # should never slow down as much as to change direction
        self.xSpeed = 0
      #print("lol")
    elif(self.xSpeed < 0):
      self.xSpeed += self.xSlowDown
      if(self.xSpeed > 0): # should never slow down as much as to change direction
        self.xSpeed = 0

    if(self.xSpeed > self.xMaxSpeed):
      self.xSpeed = self.xMaxSpeed
    if(self.xSpeed < -self.xMaxSpeed):
      self.xSpeed = -self.xMaxSpeed 
      
    ### JUMPING MANAGEMENT
    if(movementKeys['up'] and self.ySpeed == 0 and self.canJump):
      self.ySpeed = -self.jumpSpeed
    elif(movementKeys['up'] and self.ySpeed < 0 and not(self.maxJumpSpeedReached)):
      self.ySpeed -= self.jumpAcceleration
      self.canJump = 0

    if(self.ySpeed < -self.maxJumpSpeed):
      self.ySpeed = - self.maxJumpSpeed
      self.maxJumpSpeedReached = 1

    ## GRAVITY
    self.ySpeed += self.gravity
    
    ## MODIFY POSITION
    self.position = self.position.move(self.xSpeed,self.ySpeed) 

    ### COLLISIONNING    
    if(self.position[0] + self.image.get_width() > resolution[0]):
      self.position[0] = resolution[0] - self.image.get_width()
      self.xSpeed = 0
    if(self.position[1] + self.image.get_height() > resolution[1]):
      self.position[1] = resolution[1] - self.image.get_height()
      self.ySpeed = 0
      self.maxJumpSpeedReached = 0
      self.canJump = 1
    if(self.position[0] < 0):
      self.position[0] = 0
      self.xSpeed = 0
    if(self.position[1] < 0):
      self.position[1] = 0
      self.ySpeed = 0 '''
