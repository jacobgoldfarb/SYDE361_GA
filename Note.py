# This class encapsulates a single note in a composition.
import * from Notes

class Note:
    
    supportedNotes = ['A4', 'A4#', 'B4', 'C4', 'C4#', 'D4', 'D4#', 'E4', 'F4', 'F4#', 'G4', 'G4#'
                     ,'A5', 'A5#', 'B5', 'C5', 'C5#', 'D5', 'D5#', 'E5', 'F5', 'F5#', 'G5', 'G5#']
    supportedFreqs = [440,
    440 * 2 ** (1 / 12),
    440 * 2 ** (2 / 12),
    440 * 2 ** (3 / 12),
    440 * 2 ** (4 / 12),
    440 * 2 ** (5 / 12),
    440 * 2 ** (6 / 12),
    440 * 2 ** (7 / 12),
    440 * 2 ** (8 / 12),
    440 * 2 ** (9 / 12),
    440 * 2 ** (10 / 12),
    440 * 2 ** (11 / 12),
    440 * 2 ** (12 / 12),
    440 * 2 ** ((1 + 12) / 12),
    440 * 2 ** ((2 + 12) / 12),
    440 * 2 ** ((3 + 12) / 12),
    440 * 2 ** ((4 + 12) / 12),
    440 * 2 ** ((5 + 12) / 12),
    440 * 2 ** ((6 + 12) / 12),
    440 * 2 ** ((7 + 12) / 12),
    440 * 2 ** ((8 + 12) / 12),
    440 * 2 ** ((9 + 12) / 12),
    440 * 2 ** ((10 + 12) / 12),
    440 * 2 ** ((11 + 12) / 12)]

    def __init__(self, freq, letter, duration=1):
        if letter not in self.supportedNotes:
            raise Exception("Unsupported letter note")
        self.freq = freq
        self.letter = letter
        self.duration = 1

    @classmethod
    def fromABC(cls, note):
        return {
            'A' : A4,
            '^A' : A4sh,
            'B' : B4,
            'C' : C4,
            '^C' : C4sh,
            'D' : D4,
            '^D' : D4sh,
            'E' : E4,
            'F' : F4,
            '^F' : F4sh,
            'G' : G4,
            '^G' : G4sh,
            'a' : A5,
            '^a' : A5sh,
            'b' : B5,
            'c' : C5,
            '^c' : C5sh,
            'd' : D5,
            '^d' : D5sh,
            'e' : E5,
            'f' : F5,
            '^f' : F5sh,
            'g' : G5,
            '^g' : G5sh,
        }.get(note)

    def __eq__(self, other):
        return abs(self.freq - other.freq) < 100

    def __lt__(self, other):
        return not (self == other) and self.freq < other.freq

    def __add__(self, o): 
        noteIndex = self.supportedNotes.index(self.letter)
        noteIndex += o
        if len(self.supportedNotes) - 1 < noteIndex:
            noteIndex = noteIndex - len(self.supportedNotes)
        newFreq = self.supportedFreqs[noteIndex]
        newNote = self.supportedNotes[noteIndex]
        return Note(newFreq, newNote)
    
    def __sub__(self, o):
        return self.supportedNotes.index(self.letter) - self.supportedNotes.index(o.letter)
 

