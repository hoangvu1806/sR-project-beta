import tqdm
import librosa
import os
import numpy as np
import librosa.display
import matplotlib.pyplot as plt
from scipy.fftpack import fft



def plot_audio_waveform(audio_data, sample_rate):
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(audio_data, sr=sample_rate)
    plt.title('Waveform')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()

def read_wav_file(file_path):
    audio_data, sample_rate = librosa.load(file_path)
    return (audio_data, sample_rate)

def plot_spectrogram(file_path):
    # Đọc file âm thanh
    y, sr = librosa.load(file_path)

    # Tính spectrogram
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

    # Vẽ biểu đồ spectrogram
    plt.figure(figsize=(12, 4))
    librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')
    plt.show()

if __name__ == "__main__":
    file_path = r"E:\Project Speech recognize\Data\test1.wav"

    audio_data, sample_rate = read_wav_file(file_path=file_path)
    duration = librosa.get_duration(y=audio_data, sr=sample_rate)
    
    print(np.abs(librosa.stft(audio_data)))
    # plot_audio_waveform(audio_data, sample_rate)
    
    # Tính thời gian tương ứng với mỗi mẫu dữ liệu
    time = np.arange(0, len(audio_data)) / sample_rate

    # Vẽ biểu đồ
    plt.figure(figsize=(10, 4))
    plt.plot(time, audio_data, linewidth=0.1)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Speech Signal')
    plt.show()


    # Giả sử audio_data là mảng numpy chứa dữ liệu âm thanh và sample_rate là tần số lấy mẫu
    # audio_data, sample_rate = ...

    # Tính biến đổi Fourier nhanh (FFT)
    fft_out = fft(audio_data)

    # Tính tần số và độ động
    freqs = np.abs(np.fft.fftfreq(len(fft_out), 1.0/sample_rate))
    magnitude = np.sqrt(fft_out.real**2 + fft_out.imag**2)

    # Chuyển đổi độ động sang dB
    magnitude_db = 20 * np.log10(magnitude)

    # Vẽ biểu đồ
    plt.figure(figsize=(14, 5))
    plt.plot(freqs[1:], magnitude_db[1:], linewidth=0.05) # bỏ qua tần số 0 Hz
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.show()
    # Tính MFCC
    mfccs = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=13)

    # Vẽ biểu đồ
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(mfccs, x_axis='time', sr=sample_rate)
    plt.colorbar()
    plt.title('MFCC')
    plt.tight_layout()
    plt.show()