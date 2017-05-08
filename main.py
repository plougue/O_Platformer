from Sources.Worlds.W_TrainingGrounds import *
from Sources.Worlds.W_OtherWorld import *
import cProfile  

print("Quelle difficulte ? 0/1/2")
diff = input()
if diff == 0 :
  gameWorld = W_TrainingGrounds()
elif diff == 1 :
  gameWorld = W_OtherWorld("Easy")
else :
  gameWorld = W_OtherWorld("Hard")

while gameWorld.MainLoop() == 0 :
  if diff == 0 :
    gameWorld = W_TrainingGrounds()
  elif diff == 1 :
    gameWorld = W_OtherWorld("Easy")
  else :
    gameWorld = W_OtherWorld("Hard")

