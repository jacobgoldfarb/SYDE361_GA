from Note import Note
from Composition import Composition
from CompositionPlayer import CompositionPlayer
from MetricManager import MetricManager
from GA import GA
from Notes import *

selectedTrack1 = Composition([C4, G4, A5, A5sh, F4, E5, D4, C4])
# selectedTrack2 = [E, D, C, D, E, E, D, D]
# selectedTrack3 = [F, A, D, D, G, E, A, C]
alteredComp = GA().runGA(selectedTrack1, 400)
CompositionPlayer.play(selectedTrack1)
CompositionPlayer.play(alteredComp)