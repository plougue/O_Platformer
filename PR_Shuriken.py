import pygame
from Projectile import *

class PR_Shuriken(Projectile):
  def __init__(self, screen, owner, initialPosition = [0,0], direction = 'right'):
    Projectile.__init__(self, screen, "Shuriken", initialPosition, direction)
    self.xSpeed = 30
    self.damageDealt = 1
    self.ownerName = owner
