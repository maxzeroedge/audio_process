import numpy as np
import struct, wave

def write_to_wave(wave_data, wave_frames, file='out.wav'):
    wav_file=wave.open(file, 'w')
    wav_file.setparams((wave_data.nchannels, wave_data.sampwidth, wave_data.framerate, wave_data.nframes, wave_data.comptype, wave_data.compname))

    for s in wave_frames:
        wav_file.writeframes(struct.pack('h', int(s)))
    wav_file.close()