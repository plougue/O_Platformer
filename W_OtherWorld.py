from Pc import *
from Npc import *
from Obstacle import *
from World import *

class W_OtherWorld(World):
  'Base class for the world of the game'
  def __init__(self):
    World.__init__(self, [1300,700], "DarkGrey", "Markus", 60)
 
  def InitiateNpcs(self):
    self.npcList.append(Npc(self.screen, "Appendix1"))
    self.npcList.append(Npc(self.screen, "SploshyMan",[200,400]))
    self.npcList.append(Npc(self.screen, "Appendix1",[500,500]))
    return 1
  def InitiateObstacles(self):
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[0,460], [4,2]))
    self.obstacleList.append(Obstacle(self.screen,"DarkBricWall",[300,350], [6,2]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[600,300], [2,2]))
    self.obstacleList.append(Obstacle(self.screen,"DarkBricWall",[1000,200], [6,2]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[0,100], [10,3]))
    self.obstacleList.append(Obstacle(self.screen,"DarkBricWall",[0,650], [50,2]))
    return 1
    
