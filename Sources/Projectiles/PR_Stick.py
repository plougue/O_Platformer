import pygame
from Sources.Projectile import *

class PR_Stick(Projectile):
  def __init__(self, screen, owner, itemToStickTo = False, direction = 'right'):
    Projectile.__init__(self, screen, "Stick", itemToStickTo, direction)
    self.xSpeed = 0
    self.damageDealt = 4
    self.frameDuration = 18
    self.subjectToCollision = 0
    self.ownerName = owner

    self.active = False
  def Move(self):
    if self.frameDuration == 0 :
      self.frameDuration = 15
      self.active = False
    Projectile.Move(self)
  def SetActive(self, active):
    self.active = active  
  def IsActive(self):
    return self.active
