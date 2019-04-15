import numpy as np
import struct, wave

def write_to_wave(wave_data, file='out.wav'):
    wav_file=wave.open(file, 'w')
    wav_file.setparams((wave_data.nchannels, wave_data.sampwidth, wave_data.sampling_rate, wave_data.nframes, wave_data.comptype, wave_data.compname))

    for s in sine_wave:
        wav_file.writeframes(struct.pack('h', int(s*amplitude)))
    wav_file.close()