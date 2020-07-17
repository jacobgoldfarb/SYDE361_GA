from Note import *
from Composition import *
from Fitness import *
from random import randrange, uniform

class GA:
    def runGA(self, baseTrack, iterations):
        # inital run
        print("Running the genetic algorithm.")
        firstGeneration = [baseTrack] * 8 # copies 8 versions of the Composition object
        mutatedGeneration = self.mutate(firstGeneration, 0.8)
        for _ in range(iterations):
            fitnessedGeneration = list(map(self.addFitnessToComposition, mutatedGeneration))
            sortedFitnessedGeneration = self.sortGenerationByFitness(fitnessedGeneration)
            fittestGeneration = self.eliminateUnfitCandidates(sortedFitnessedGeneration)
            mutatedGeneration = self.mutate(fittestGeneration, 0.8)
        finalGen = self.sortGenerationByFitness(fitnessedGeneration)
        print("Done.")
        return max(finalGen, key=lambda x: x.getFitness())

    def addFitnessToComposition(self, comp):
        compFitness = Fitness.determineFitness(comp)
        comp.setFitness(compFitness)
        return comp

    # Get rid of the bottom half unfit generations.
    def eliminateUnfitCandidates(self, generation):
        return generation[:len(generation)//2] + generation[:len(generation)//2]

    def mutate(self, generation, mutationProbability):
        mutatedGeneration = [] # store the mutated candidates
        for candidate in generation: # go through each of the 8 candidate Composition objects
            if uniform(0, 1) < mutationProbability: # mutate XX% of this generation
                mutatedGeneration.append(self.mutateCandidate(candidate))
            else: # rotate candidate
                mutatedGeneration.append(self.rotateCandidate(candidate)) # rotate candidate
        return mutatedGeneration
        
    def mutateCandidate(self, candidate):
        newNotes = [] # list containing the new notes for the specific composition
        for i, note1 in enumerate(candidate.notes): # each note is a Note object
            newNote = note1
            for j, note2 in enumerate(candidate.notes):
                if j >= i:
                    continue
                # randomly move consecutive notes:
                if abs(j - i) == 1 and Composition.notesAreEqual(note1, note2): # Counterpoint Species 1 does not allow consecutive equal notes
                    newNote = newNote + randrange(3,6)
                elif uniform(0,1) < 0.4: # randomly change 40% of notes.
                    newNote += randrange(1,10)
            newNotes.append(newNote)
        return Composition(newNotes)

    def rotateCandidate(self, candidate):
        oldNotes = candidate.notes
        rotationIndex1 = randrange(0, 8) # rotate once
        tempNotes = oldNotes[rotationIndex1:] + oldNotes[:rotationIndex1]
        rotationIndex2 = randrange(0, 8) # rotate twice
        newNotes = tempNotes[rotationIndex2:] + tempNotes[:rotationIndex2]
        return Composition(newNotes)

    def sortGenerationByFitness(self, generation):
        return sorted(generation, key=lambda x: x.getFitness(), reverse=True)

