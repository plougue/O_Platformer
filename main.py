from W_TrainingGrounds import *
from W_OtherWorld import *
import cProfile  

#gameWorld = W_TrainingGrounds()
gameWorld = W_OtherWorld()

cProfile.run(gameWorld.MainLoop())


