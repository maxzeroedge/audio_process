import numpy as np
import wave, struct
import matplotlib.pyplot as plt

def get_frequency_test():
    infile = "test.wav"
    num_samples = 48000
    # Open and read the file
    with wave.open(infile, 'r') as wav_file:
        fmt = "{n}h".format(n=num_samples)

        num_samples = struct.calcsize(fmt)
        # Unpack the data
        data = wav_file.readframes(num_samples)
        data = struct.unpack(fmt, data)
        # Convert to array
        data = np.array(data)
        # Get back actual data
        data_fft = np.fft.fft(data)
        # Convert complex numbers to real numbers
        frequencies = np.abs(data_fft)

        print("The frequency is {} Hz".format(np.argmax(frequencies)))

        # Plot the graphs
        plt.subplot(2,1,1)
        plt.plot(data)
        plt.title("Original Wave")
        plt.subplot(2,1,2)
        plt.plot(frequencies)
        plt.title("Frequency wave")
        # plt.xlim(0, 1200)
        plt.show()

def get_frequency(wave_data):
    channels = wave_data[1].nchannels
    num_samples = wave_data[1].framerate
    fmt = "{n}h".format(n=num_samples)
    # Unpack the data
    data = struct.unpack_from(fmt, wave_data[0])

    channel_data = []
    frequency_data = []
    for i in range(channels):
        # Convert to array
        data1 = np.array(data[i::channels])
        # Get back actual data
        data_fft = np.fft.fft(data1)
        # Convert complex numbers to real numbers
        frequencies = np.abs(data_fft)

        print("The frequency is {} Hz".format(np.argmax(frequencies)))
        channel_data.append(data1)
        frequency_data.append(frequencies)
    return {
        'channel_data': channel_data,
        'frequency_data': frequency_data
    }

def plot_graphs(channel_data, frequency_data):
    channels = len(channel_data)
    # Plot the graphs
    for i in range(channels):
        plt.subplot(channels,channels,1)
        plt.plot(channel_data[i])
        plt.title("Original Wave: Channel {}".format(i+1))
        plt.subplot(channels,channels,2)
        plt.plot(frequency_data[i])
        plt.title("Frequency wave: Channel {}".format(i+1))
        # plt.xlim(0, 1200)
    plt.show()

if __name__=="__main__":
    get_frequency_test()