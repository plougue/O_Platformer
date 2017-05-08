import pygame
from Sources.Projectile import *

class PR_Fireball(Projectile):
  def __init__(self, screen, owner, itemToStickTo = False, direction = 'right', spriteNumber = 1, framesCharged = 1):
    Projectile.__init__(self, screen, "Fireball", itemToStickTo, direction)
    self.image = pygame.image.load("Sprites/Projectiles/Fireball/Fireball_" + str(spriteNumber + 1) + "_idle.png")
    if itemToStickTo:
      self.StickToItem(itemToStickTo.GetPosition(), itemToStickTo.GetSize())



    spriteToDamage = [1,1,2,2,3,3]
    spriteToSpeed  = [30,20,13,10,9,7]
    self.xSpeed = spriteToSpeed[spriteNumber]
    self.damageDealt = 1 + spriteToDamage[spriteNumber]
    self.ownerName = owner
    self.rotation = 0
    self.rotationSpeed = 25
    self.framesCharged = framesCharged
    self.subjectToCollision = 0
    self.spriteDirection = 'right'
    

    print(self.framesCharged)
    

    self.frameDuration = self.framesCharged
