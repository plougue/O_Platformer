from Sources.Pc import *
from Sources.Npc import *
from Sources.Obstacle import *
from Sources.World import *

class W_TrainingGrounds(World):
  'Base class for the world of the game'
  def __init__(self):
    World.__init__(self, [1200,700], [1400,800], "CalmValley", "Markus", 60)
 
  def InitiateNpcs(self):
    return 1
  def InitiateObstacles(self):
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[600,460], [6,1]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[800,300], [6,2]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[400,300], [2,2]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[0,100], [10,3]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[0,650], [40,2]))
    return 1
    
