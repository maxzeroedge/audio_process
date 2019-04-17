import numpy as np
import wave
import struct
import matplotlib.pyplot as plt
import collections
 
WaveProps = collections.namedtuple('WaveProps', ['nframes','comptype','compname','nchannels','sampwidth', 'framerate'])

def test_main101():
	# frequency is the number of times a wave repeats a second
	frequency = 1000
	num_samples = 48000
	# The sampling rate of the analog to digital convert
	sampling_rate = 48000.0
	amplitude = 16000
	file = "test.wav"

	sine_wave = [ np.sin( 2 * np.pi * frequency * (x/sampling_rate) ) for x in range(num_samples)]
	wave_props = WaveProps(num_samples, 'NONE', 'not compressed', 1, 2, sampling_rate)
	write_wav_file(file, sine_wave, wave_props, amplitude)

def write_wav_file(file, wave_data, wave_params, amplitude=16000):
	wav_file=wave.open(file, 'w')
	wav_file.setparams((wave_params.nchannels, wave_params.sampwidth, int(wave_params.framerate), wave_params.nframes, wave_params.comptype, wave_params.compname))

	for s in wave_data:
		wav_file.writeframes(struct.pack('l', int(s*amplitude)))
	wav_file.close()

if __name__=="__main__":
	test_main101()