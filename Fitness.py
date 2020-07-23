from random import randrange, uniform
from Notes import *
import numpy as np

# This class encapsualtes functionality to determine the fitness of a composition.
class Fitness:

    @staticmethod
    def determineFitness(composition):
        harmonyWeight = 1
        continuityWeight = 0.0
        harmonyScore = Fitness.getHarmonyScore(composition) * harmonyWeight
        continuityScore = Fitness.getContinuityScore(composition) * continuityWeight
        return harmonyScore + continuityScore

    @staticmethod
    def getHarmonyScore(composition):
         minorPenalty = 0.3
         majorIncrements = [0, 2, 2, 1, 2, 2, 2, 1]
         minorIncrements = [0, 2, 1, 2, 2, 1, 2, 2] # only majors for now [0, 2, 1, 2, 2, 1, 2, 2]
         sortedComp = composition #composition.getSortedComposition()
         compDiffs = [0] + [sortedComp.notes[i + 1] - sortedComp.notes[i] for i in range(len(sortedComp.notes) - 1)]
         diffMaj = list(np.subtract(majorIncrements, compDiffs))
         diffMin = list(np.subtract(minorIncrements, compDiffs))
         scaleScoreMaj = diffMaj.count(0) / len(diffMaj)
         scaleScoreMin = diffMin.count(0) / len(diffMin) - 0.2
         return max(scaleScoreMin, scaleScoreMaj)
    
    @staticmethod
    def getContinuityScore(composition):
        sortedComp = composition.getSortedComposition()
        compDiffs = [0] + [sortedComp.notes[i + 1] - sortedComp.notes[i] for i in range(len(sortedComp.notes) - 1)]
        meanDifference = sum(compDiffs) / len(compDiffs) 
        if meanDifference == 0:
            return 0
        score =  min((len(Note.supportedNotes) / (meanDifference * len(Note.supportedNotes))), 1)
        return score