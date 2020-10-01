from pydub import AudioSegment
import random
from scipy.io import wavfile

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

BASE = './wav/'
SONG1 = BASE + 'hikaru.wav'
SONG2 = BASE + 'fiction.wav'

LEFT = BASE + 'left.wav'
RIGHT = BASE + 'right.wav'

FILENAME = 'mixed.wav'

fs, data = wavfile.read(SONG1)
wavfile.write(LEFT, fs, data[:, 0])

fs, data = wavfile.read(SONG2)
wavfile.write(RIGHT, fs, data[:, 1])

sound = AudioSegment.from_file(LEFT, "wav")
normalized_sound = match_target_amplitude(sound, -20.0)
normalized_sound.export(LEFT, format="wav")

sound = AudioSegment.from_file(RIGHT, "wav")
normalized_sound = match_target_amplitude(sound, -20.0)
normalized_sound.export(RIGHT, format="wav")

sound1 = AudioSegment.from_wav(LEFT)
sound2 = AudioSegment.from_wav(RIGHT)

mixed = sound1.overlay(sound2)
mixed.export(FILENAME, format="wav")
