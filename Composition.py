

# This class encapsulates a composition of notes.
class Composition:
    
    def __init__(self, notes):
        self.notes = notes
    
    def getSortedComposition(self):
        return Composition(sorted(self.notes))

    def setFitness(self, fitness):
        self.fitness = fitness
    
    def getFitness(self):
        return self.fitness

    @staticmethod
    def notesAreConsecutive(note1, note2):
        return note1 == note2 + 1 or note2 == note1 + 1