import pygame

class Obstacle:
  def __init__(self, screen, obstacleName, position, repeats):
    self.blockPositions = []
    self.image = pygame.image.load("Sprites/Obstacles/Blocks/" + obstacleName+ "/" + obstacleName + ".png").convert_alpha()
    self.screen = screen
    self.position = [position[0], position[1]]
    for i in range(repeats[0]):
      for j in range(repeats[1]):
        currentBlockPosition = self.image.get_rect()
        currentBlockPosition[0] = self.position[0] + currentBlockPosition[2] * i
        currentBlockPosition[1] = self.position[1] + currentBlockPosition[3] * j
        self.blockPositions.append(currentBlockPosition)
    self.size = [currentBlockPosition[2] * repeats[0], currentBlockPosition[3] * repeats[1]]

  def blit(self):
    for currentBlockPosition in self.blockPositions:
      self.screen.blit(self.image, currentBlockPosition)

  def GetPosition(self):
    return self.position

  def GetSize(self):
    return self.size
