import pygame
from pg_functions import correctedBlit

class Projectile:
  'Base class for the playable character'
  def __init__(self, screen, projectileName, initialPosition=[0,0], direction = 'right'):
  
    # General projectile arguments
    self.screen = screen
    self.projectileName = projectileName
    self.image = pygame.image.load("Sprites/Projectiles/" + self.projectileName + "/" + self.projectileName + "_idle.png").convert_alpha()
    self.position = self.image.get_rect()
    self.position[0] = initialPosition[0]
    self.position[1] = initialPosition[1]
    self.lastFramePosition = self.position
    self.toBeDeleted = 0

    self.subjectToCollision = 1
    self.frameDuration = -1 # corresponds to an infinite duration

    self.ownerName = 0     
    self.damageDealt = 10

    # X-movement related arguments 
    self.xSpeed = 15
    self.direction = direction
    
    # Gravity
    self.gravity = 0
    
    self.spriteDirection = 'left'  
  #############################################################################
  ##    CHANGES THE STATE ACCORDINGLY IF A COLLISION OCCURS                  ##
  #############################################################################
  def DeclareCollision(self, directions):
    if (directions['right'] or directions['up'] or directions['down'] or directions['left']) :
      self.toBeDeleted = 1

  def Display(self, cameraPosition):
    if not self.toBeDeleted:
      if self.direction == self.spriteDirection :
        correctedBlit(self.screen, self.image, self.position, cameraPosition)
      else :
        correctedBlit(self.screen,pygame.transform.flip(self.image, True, False), self.position, cameraPosition)
  def Move(self) :
    if self.frameDuration ==  0 :
      self.toBeDeleted = 1
    if not self.toBeDeleted :
      self.lastFramePosition = self.position
      if self.direction == 'right' :
        self.position[0] = self.position[0] + self.xSpeed
      if self.direction == 'left' :
        self.position[0] = self.position[0] - self.xSpeed
    if self.frameDuration > 0 :
      self.frameDuration = self.frameDuration - 1

  def GetLastFramePosition(self):
    return self.lastFramePosition

  def GetPosition(self):
    return self.position
  
  def GetDamageDealt(self):
    return self.damageDealt

  def GetSize(self):
    return (self.image.get_width(), self.image.get_height())

  def GetOwnerName(self):
    return self.ownerName
    
  def CanCollide(self):
    return self.subjectToCollision
  
  def SetPosition(self,newPosition):
    self.position = newPosition

  def SetDirection(self, newDirection):
    self.direction = newDirection

  def SetDuration(self, newDuration) :
    self.duration = newDuration
  
  def IsToBeDeleted(self):
    return self.toBeDeleted
