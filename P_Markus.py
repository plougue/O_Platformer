import pygame
from Pc import Pc

class P_Markus(Pc):

  'Base class for markus'

  def __init__(self, screen, initialPosition=[0,0]):
    Pc.__init__(self,screen, "Markus", initialPosition)
    # General character arguments
