import pygame
from Pc import Pc

class PC_Markus(Pc):

  'Base class for markus'

  def __init__(self, screen, initialPosition=[0,0]):
    Pc.__init__(self,screen, "Markus", initialPosition)
    self.numberOfJumps = 2
    self.maxHp = 2
    self.currentHp = 2 
    # General character arguments
