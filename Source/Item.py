import pygame
from pg_functions import correctedBlit

class Item:
  'Base class for the playable character'
  def __init__(self, screen, itemName, spritePath=False, initialPosition=[0,0], direction='left', hitboxSize = False, hitboxPosition = False):
  
    # General character arguments
    self.screen = screen
    self.name = itemName
    self.image = False
    if(spritePath):
      self.image = pygame.image.load(spritePath).convert_alpha()
    self.position = self.image.get_rect()
    self.position[0] = initialPosition[0]
    self.position[1] = initialPosition[1]
    self.lastFramePosition = self.position
    self.spriteDirection = 'left'
    self.direction = direction
    
    if hitboxSize : 
      self.hitboxSize = hitboxSize
    if hitboxPosition : 
      self.hitboxPosition = hitboxPosition
    
  def DeclareCollision(self, directions):
     return 0

  def Display(self,cameraPosition):
    if self.direction != self.spriteDirection :
      correctedBlit(self.screen,pygame.transform.flip(self.image, True, False), self.position, cameraPosition)
    else :
      correctedBlit(self.screen,self.image, self.position, cameraPosition)

  def Move(self,movements) :
    self.lastFramePosition = self.position
    return 0
 
  def Attack(self, projectileList):
    return 0

  def GetLastFramePosition(self):
    return self.lastFramePosition

  def GetHitboxPosition(self):
    if self.hitboxPosition : 
      return self.hitboxPosition
    else :
      return self.position
      
  def GetHitboxSize(self):
    if self.hitboxSize : 
      return self.hitboxSize
    else :
      return self.GetSize()

  def GetPosition(self):
    return self.position
  
  def GetSize(self):
    if self.image:
      return (self.image.get_width(), self.image.get_height())
  
  def GetName(self):
    return self.name

  def SetDirection(self, newDirection):
    self.direction = newDirection

  def SetPosition(self,newPosition):
    self.position[1] = newPosition[1]
    self.position[0] = newPosition[0]
