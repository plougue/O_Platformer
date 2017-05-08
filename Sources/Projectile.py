import pygame
from Item import Item
from pg_functions import correctedBlit, screenPrint

class Projectile(Item):
  'Base class for the playable character'
  def __init__(self, screen, projectileName, itemToStickTo = False, direction = 'right'):
    
    Item.__init__(self, screen, projectileName, "Sprites/Projectiles/" + projectileName + "/" + projectileName + "_idle.png", [0,0])

    if itemToStickTo :
      self.StickToItem(itemToStickTo.GetPosition(), itemToStickTo.GetSize())

    # General projectile arguments
    self.toBeDeleted = 0
    self.deletedWhenCollision = {'left': True, 'right': True, 'up' : False, 'down' : False}
    self.subjectToCollision = 0
    self.frameDuration = -1 # corresponds to an infinite duration
    self.ownerName = 0     
    self.damageDealt = 10

    # X-movement related arguments 
    self.xSpeed = 15
    self.direction = direction
    
    # Gravity
    self.gravity = 0
    self.spriteDirection = 'left'  

  def DeclareCollision(self, directions):
    if (directions['right'] and self.deletedWhenCollision['right']) or (directions['up'] and self.deletedWhenCollision['up']) \
       or (directions['down'] and self.deletedWhenCollision['down']) or (directions['left'] and self.deletedWhenCollision['left']) :
      self.toBeDeleted = 1

  def Move(self) :
    if self.frameDuration ==  0 :
      self.toBeDeleted = 1
    if not self.toBeDeleted :
      Item.Move(self, 0)
      if self.direction == 'right' :
        self.position[0] = self.position[0] + self.xSpeed
      if self.direction == 'left' :
        self.position[0] = self.position[0] - self.xSpeed
    if self.frameDuration > 0 :
      self.frameDuration = self.frameDuration - 1

  def StickToItem(self, position, size):
    projectilePosition = self.GetPosition()
    projectileSize = self.GetSize()
    projectilePosition[1] = min(position[1] + (size[1] - projectileSize[1]) / 2, position[1] + size[1] - projectileSize[1])
    if self.direction == 'left':
      projectilePosition[0] = position[0] - projectileSize[0]
    if self.direction == 'right' :
      projectilePosition[0] = position[0] + size[0]
    self.SetPosition(projectilePosition)


  def GetDamageDealt(self):
    return self.damageDealt

  def GetOwnerName(self):
    return self.ownerName
    
  def CanCollide(self):
    return self.subjectToCollision

  def SetDuration(self, newDuration) :
    self.duration = newDuration
  
  def IsToBeDeleted(self):
    return self.toBeDeleted
