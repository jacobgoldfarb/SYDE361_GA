from Note import Note

# This file is used as storage to declare the supported notes for use in the rest of the application.
baseFreq = 440
A4 = Note(baseFreq, "A4")
A4sh = Note(baseFreq * 2 ** (1 / 12), "A4#")
B4 = Note(baseFreq * 2 ** (2 / 12), "B4")
C4 = Note(baseFreq * 2 ** (3 / 12), "C4")
C4sh = Note(baseFreq * 2 ** (4 / 12), "C4#")
D4 = Note(baseFreq * 2 ** (5 / 12), "D4")
D4sh = Note(baseFreq * 2 ** (6 / 12), "D4#")
E4 = Note(baseFreq * 2 ** (7 / 12), "E4")
F4 = Note(baseFreq * 2 ** (8 / 12), "F4")
F4sh = Note(baseFreq * 2 ** (9 / 12), "F4#")
G4 = Note(baseFreq * 2 ** (10 / 12), "G4")
G4sh = Note(baseFreq * 2 ** (11 / 12), "G4#")
A5 = Note(baseFreq * 2 ** ((12) / 12), "A5#")
A5sh = Note(baseFreq * 2 ** ((1 + 12) / 12), "A5#")
B5 = Note(baseFreq * 2 ** ((2 + 12) / 12), "B5")
C5 = Note(baseFreq * 2 ** ((3 + 12) / 12), "C5")
C5sh = Note(baseFreq * 2 ** ((4 + 12) / 12), "C5#")
D5 = Note(baseFreq * 2 ** ((5 + 12) / 12), "D5")
D5sh = Note(baseFreq * 2 ** ((6 + 12) / 12), "D5#")
E5 = Note(baseFreq * 2 ** ((7 + 12) / 12), "E5")
F5 = Note(baseFreq * 2 ** ((8 + 12) / 12), "F5")
F5sh = Note(baseFreq * 2 ** ((9 + 12) / 12), "F5#")
G5 = Note(baseFreq * 2 ** ((10 + 12) / 12), "G5")
G5sh = Note(baseFreq * 2 ** ((11 + 12) / 12), "G5#")

def strListToNoteList(inputComp):
    noteConverter = {'A4': A4, 'A4#': A4sh, 'B4': B4, 'C4': C4, 'C4#': C4sh, 'D4': D4, 'D4#': D4sh, 'E4': E4, 'F4': F4,
                     'F4#': F4sh, 'G4': G4, 'G4#': G4sh, 'A5': A5, 'A5#': A5sh, 'B5': B5, 'C5': C5, 'C5#': C5sh, 'D5': D5,
                     'D5#': D5sh, 'E5': E5, 'F5': F5, 'F5#': F5sh, 'G5': G5, 'G5#': G5sh}
    converted_notes = [noteConverter[note] for note in inputComp]
    return(converted_notes)

def abcStrListToNoteList(inputComp):
    abcConverter =  {
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
        '^g' : G5sh}
    converted_notes = [abcConverter[note] for note in inputComp]
    return (converted_notes)