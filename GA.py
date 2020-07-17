from Note import *
from Composition import *
from Fitness import *
from random import randrange, uniform

# This class is the genetic algorithm controller. The only interface function is 'runGA', which inputs
# the initial composition, number of iterations, and outputs the genetically imporved algorithm.
class GA:
    def runGA(self, baseTrack, iterations):
        # inital run
        print("Running the genetic algorithm.")
        firstGeneration = [baseTrack] * 8
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
        mutatedGeneration = []
        for candidate in generation:
            if uniform(0, 1) < mutationProbability: # mutate 80% of this generation
                mutatedGeneration.append(self.mutateCandidate(candidate))
            else: # don't mutate
                mutatedGeneration.append(candidate)
        return mutatedGeneration
        
    def mutateCandidate(self, candidate):
        newNotes = []
        for i, note1 in enumerate(candidate.notes):
            newNote = note1
            for j, note2 in enumerate(candidate.notes):
                if j >= i:
                    continue
                # randomly move consecutive notes:
                if abs(j - i) == 1 and Composition.notesAreConsecutive(note1, note2):
                    newNote = newNote + randrange(3,6)
                elif uniform(0,1) < 0.4: # randomly change 40% of notes.
                    newNote += randrange(1,10)
            newNotes.append(newNote)
        return Composition(newNotes)            

    def sortGenerationByFitness(self, generation):
        return sorted(generation, key=lambda x: x.getFitness(), reverse=True)

