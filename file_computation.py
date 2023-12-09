import file_handling
import numpy as np
from scipy.io import wavfile
import wave
import numpy
import librosa

class File_Comp:
    def __init__(self, file):
        self.file_path = file.wav_filename

    def return_time(self):
        samplerate, data = wavfile.read(self.file_path)
        return data.shape[0] / samplerate

    def high_resonance(self) -> float:
        wav_file = wave.open(self.file_path, rb)
        audio_data = numpy.frombuffer(wav_file.readframes(wav_file.getnframes()), dtype = np.int16)
        freq_spec = np.fft.fft(audio_data)
        sample_rate = wav_file.getframerate()
        freqs = np.fft.fftfreq(len(freq_spec), d = 1/sample_rate)
        peak_index = np.argmax(np.abs(freq_spec))
        return freqs[peak_index]