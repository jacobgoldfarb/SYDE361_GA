from Note import Note
from Composition import Composition
from CompositionPlayer import CompositionPlayer
from MetricManager import MetricManager
from GA import GA
from Notes import *

def run_GA(inputComp):

    converted_notes = strListToNoteList(inputComp)
    # converted_notes = abcStrListToNoteList(inputComp)
    selectedTrack1 = Composition(converted_notes)
    alteredComp = GA().runGA(selectedTrack1, 400)

    outputComp_str = []
    for note in alteredComp.notes:
        outputComp_str.append(str(note.letter))

    return outputComp_str


def main_sandbox():
    selectedTrack1 = Composition([C4, G4, A5, A5sh, F4, E5, D4, C4])
    alteredComp = GA().runGA(selectedTrack1, 400)
    CompositionPlayer.play(selectedTrack1)
    CompositionPlayer.play(alteredComp)

