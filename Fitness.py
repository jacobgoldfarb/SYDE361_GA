from random import randrange, uniform
from Notes import *
import numpy as np

# This class encapsualtes functionality to determine the fitness of a composition.
class Fitness:

    @staticmethod
    def determineFitness(composition):
        harmonyScore = Fitness.getHarmonyScore(composition)
        return harmonyScore

    @staticmethod
    def getHarmonyScore(composition):
         majorIncrements = [0, 2, 2, 1, 2, 2, 2, 1]
         minorIncrements = [0, 2, 1, 2, 2, 1, 2, 2]
         sortedComp = composition.getSortedComposition()
         compDiffs = [0] + [sortedComp.notes[i + 1] - sortedComp.notes[i] for i in range(len(sortedComp.notes) - 1)]
         diffMaj = list(np.subtract(majorIncrements, compDiffs))
         diffMin = list(np.subtract(minorIncrements, compDiffs))
         scaleScoreMaj = diffMaj.count(0) / len(diffMaj)
         scaleScoreMin = diffMin.count(0) / len(diffMin)
         return max(scaleScoreMin, scaleScoreMaj)

