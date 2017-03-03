import pygame
from Projectile import *

class PR_Stick(Projectile):
  def __init__(self, screen, owner, initialPosition = [0,0], direction = 'right'):
    Projectile.__init__(self, screen, "Stick", initialPosition, direction)
    self.xSpeed = 0
    self.damageDealt = 3
    self.frameDuration = 15
    self.subjectToCollision = 0
    self.ownerName = owner
    self.active = False
  def Move(self, resolution):
    if self.frameDuration == 0 :
      self.frameDuration = 15
      self.active = False
      print("duration ended")
    Projectile.Move(self, resolution)
  def SetActive(self, active):
    self.active = active  
  def IsActive(self):
    return self.active
