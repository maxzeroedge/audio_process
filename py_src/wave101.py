import wave
import get_freq as Get_freq

def process_wave(inFile):
    audio_frames = None
    audio_params = None
    with wave.open(inFile, 'rb') as wave_file:
        # Get file data
        print("channel count:", wave_file.getnchannels())
        print("sample width:", wave_file.getsampwidth())
        print("sampling frequency:", wave_file.getframerate())
        print("number of audio frames:", wave_file.getnframes())
        print("compression type:", wave_file.getcomptype())
        print("compression name:", wave_file.getcompname())
        # print("data:", wave_file.getparams())
        # Read whole audio frames
        audio_frames = wave_file.readframes(wave_file.getnframes())
        audio_params = wave_file.getparams()
    return (audio_frames, audio_params)

def invert_waves(data):
    max_val = max(data)
    return [ max_val - d for d in data ]

if __name__=="__main__":
    out = process_wave("../Tobu-Candyland.wav")
    wave_data = Get_freq.get_frequency(out)
    indx = 0
    for f in wave_data['frequency_data']:
        if(indx % 2 == 0 ):
            continue
        wave_data['frequency_data'][indx] = invert_waves(f)
        indx += 1
    indx = 0
    for f in wave_data['channel_data']:
        if(indx % 2 == 0 ):
            continue
        wave_data['channel_data'][indx] = invert_waves(f)
        indx += 1
    Get_freq.plot_graphs(wave_data['channel_data'], wave_data['frequency_data'])