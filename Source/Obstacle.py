import pygame
from pg_functions import correctedBlit
from Item import Item

class Obstacle(Item):
  def __init__(self, screen, obstacleName, position, repeats, direction = 'left'):
    Item.__init__(self, screen, obstacleName, "Sprites/Obstacles/Blocks/" + obstacleName + "/" + obstacleName + ".png", position, direction, position)

    self.blockPositions = []
    self.position = [position[0], position[1]]
    for i in range(repeats[0]):
      for j in range(repeats[1]):
        currentBlockPosition = self.image.get_rect()
        currentBlockPosition[0] = self.position[0] + currentBlockPosition[2] * i
        currentBlockPosition[1] = self.position[1] + currentBlockPosition[3] * j
        self.blockPositions.append(currentBlockPosition)
    self.size = [currentBlockPosition[2] * repeats[0], currentBlockPosition[3] * repeats[1]]
    
  
  def Display(self, cameraPosition):
    for currentBlockPosition in self.blockPositions:
      correctedBlit(self.screen,self.image, currentBlockPosition, cameraPosition)

  def GetSize(self):
    return self.size
