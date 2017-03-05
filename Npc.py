import pygame
from Character import Character
from random import random

class Npc(Character):

  'Base class for the playable character'

  def __init__(self, screen, characterName, initialPosition=[0,0]):
 
    Character.__init__(self, screen, characterName, "Sprites/Characters/Npc/" + characterName + "/" + characterName + "_idle.png", initialPosition)
    # General character arguments 
    self.maxHp = 70
    self.currentHp = 70
    self.invulnerabilityFrameDuration = 0
    self.xMaxSpeed = 13
    self.direction = 'left'
    self.spriteDirection = 'right'

  def DeclareCollision(self, directions) :
    
    if (directions['right'] and self.direction == 'right') :
      self.direction = 'left'
    if directions['left'] and self.direction == 'left' :
      self.direction = 'right'
    Character.DeclareCollision(self,directions)
    
  def Move(self):
    if self.direction == 'right':
      if random() < 0.2 :
        Character.Move(self, {'left':0, 'right':1, 'up':1, 'down':0})
      elif random() < 0.4 :
        Character.Move(self, {'left':0, 'right':0, 'up':1, 'down':0})
      else:
        Character.Move(self, {'left':0, 'right':1, 'up':0, 'down':0})
    if self.direction == 'left':
      if random() < 0.2 :
        Character.Move(self, {'left':1, 'right':0, 'up':1, 'down':0})
      elif random() < 0.4 :
        Character.Move(self, {'left':0, 'right':0, 'up':1, 'down':0})
      else:
        Character.Move(self, {'left':1, 'right':0, 'up':0, 'down':0})
  
  def blit(self):
    Character.blit(self)
    self.DisplayHp()

