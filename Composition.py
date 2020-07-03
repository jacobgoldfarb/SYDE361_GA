import simpleaudio as sa
import numpy as np

class Composition:
    
    def __init___(self, notes):
        self.notes = notes

    @staticmethod
    def play(inputNotes):
        # get timesteps for each sample, T is note duration in seconds
        sample_rate = 44100
        T = 0.25
        t = np.linspace(0, T, T * sample_rate, False)
        # generate sine wave notes
        sinNotes = []
        for note in inputNotes:
            sinNotes.append(np.sin(note.freq * t * 2 * np.pi))
        # concatenate notes
        audio = np.hstack(sinNotes)
        # normalize to 16-bit range
        audio *= 32767 / np.max(np.abs(audio))
        # convert to 16-bit data
        audio = audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
        # wait for playback to finish before exiting
        play_obj.wait_done()