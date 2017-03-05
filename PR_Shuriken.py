import pygame
from Projectile import *

class PR_Shuriken(Projectile):
  def __init__(self, screen, owner, initialPosition = [0,0], direction = 'right'):
    Projectile.__init__(self, screen, "Shuriken", initialPosition, direction)
    self.xSpeed = 15
    self.damageDealt = 1
    self.ownerName = owner
    self.rotation = 0
    self.rotationSpeed = 25

  def blit(self):
    if self.direction == 'right' :
      self.rotation = self.rotation + self.rotationSpeed
    if self.direction == 'left' :
      self.rotation = self.rotation - self.rotationSpeed
    
    self.screen.blit(pygame.transform.rotate(self.image, self.rotation), self.position)

