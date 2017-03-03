import pygame
from Character import Character

class Npc(Character):

  'Base class for the playable character'

  def __init__(self, screen, characterName, initialPosition=[0,0]):
 
    Character.__init__(self, screen, characterName, "Sprites/Characters/Npc/" + characterName + "/" + characterName + "_idle.png", initialPosition)
    # General character arguments

    self.direction = 'left'
  def Move(self, resolution):
    if self.direction == 'right':
      Character.Move(self, {'left':0, 'right':1, 'up':1, 'down':0}, resolution)
      if self.position[0] + self.image.get_width() >= resolution[0]:
        self.direction = 'left'
    if self.direction == 'left':
      Character.Move(self, {'left':1, 'right':0, 'up':0, 'down':0}, resolution)
      if self.position[0] <= 0:
        self.direction = 'right'
  
  def blit(self):
    Character.blit(self)
    totalLineLength = 50

    linePosition = [0,0]
    characterPosition =  self.GetPosition()
    characterSize = self.GetSize()
    linePosition[0] = characterPosition[0] + (characterSize[0] - totalLineLength) / 2 
    linePosition[1] = characterPosition[1] - 30
    greenLineLength = 40 * self.currentHp / self.maxHp
    greenLineEndPosition = [0,0]
    lineEndPosition = [0,0]
    greenLineEndPosition[1] = linePosition[1]
    lineEndPosition[1] = linePosition[1]
    greenLineEndPosition[0] = linePosition[0] + greenLineLength
    lineEndPosition[0] = linePosition[0] + totalLineLength
    
    if self.currentHp > 0 :
      greenLine = pygame.draw.line(self.screen, [0,200,0], linePosition, greenLineEndPosition,10)
    if self.currentHp < self.maxHp :
      redLine = pygame.draw.line(self.screen, [200,0,0], greenLineEndPosition, lineEndPosition,10)
    print(50*"-")
    print(linePosition)
    print(greenLineEndPosition)
    print(lineEndPosition)
    print(greenLineLength)

