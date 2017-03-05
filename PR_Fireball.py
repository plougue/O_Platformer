import pygame
from Projectile import *

class PR_Fireball(Projectile):
  def __init__(self, screen, owner, initialPosition = [0,0], direction = 'right', spriteNumber = 1, framesCharged = 1):
    Projectile.__init__(self, screen, "Fireball", initialPosition, direction)
    self.image = pygame.image.load("Sprites/Projectiles/Fireball/Fireball_" + str(spriteNumber+1) + "_idle.png")
    print(spriteNumber)
    self.xSpeed = 10

    spriteToDamage = [1,1,2,2,3,3]
    self.damageDealt = 1 + spriteToDamage[spriteNumber]
    self.ownerName = owner
    self.rotation = 0
    self.rotationSpeed = 25
    self.framesCharged = framesCharged
    self.subjectToCollision = 0
    self.spriteDirection = 'right'
