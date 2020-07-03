from Note import *
# import numpy as np
from random import randrange, uniform

class GA:

    def runGA(self, baseTrack):
        # inital run
        firstGeneration = [baseTrack] * 5
        mutatedGeneration = self.mutate(firstGeneration, 0.8)
        return mutatedGeneration

    def mutate(self, generation, probability):
        mutatedGeneration = []
        for candidate in generation:
            if uniform(0, 1) < probability: # mutate 80% of the first generation
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


