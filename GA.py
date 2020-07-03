from Note import *
# import numpy as np
from random import randrange, uniform

class GA:

    def runGA(self, baseTrack, iterations):
        # inital run
        firstGeneration = [baseTrack] * 5
        mutatedGeneration = self.mutate(firstGeneration, 0.8)
        for _ in range(iterations):
            fitnessedGeneration = zip(map(lambda x: self.getFitness(x), mutatedGeneration), mutatedGeneration)
            fitnessedGeneration = self.sortGenerationByFitness(fitnessedGeneration)
            sortedGeneration = map(lambda x: x[1], fitnessedGeneration)
            mutatedGeneration = self.mutate(sortedGeneration, 0.8)
        return mutatedGeneration

    def mutate(self, generation, mutationProbability):
        mutatedGeneration = []
        for candidate in generation:
            if uniform(0, 1) < mutationProbability: # mutate 80% of the first generation
                mutatedGeneration.append(self.mutateCandidate(candidate))
            else: # don't mutate
                print("Skipping mutation")
                mutatedGeneration.append(candidate)
        return mutatedGeneration
        
    def mutateCandidate(self, candidate):
        newCandidate = []
        for i, note1 in enumerate(candidate):
            newNote = note1
            for j, note2 in enumerate(candidate):
                if j >= i:
                    continue
                # randomly move consecutive notes:
                if abs(j - i) == 1 and Note.notesAreConsecutive(note1, note2):
                    print("Mutated consecutive notes")
                    newNote = newNote + randrange(3,6)
            newCandidate.append(newNote)
        return newCandidate            

    def getFitness(self, candidate):
        return uniform(0.5, 1)

    def sortGenerationByFitness(self, generation):
        return sorted(generation, key=lambda x: x[0], reverse=True)

