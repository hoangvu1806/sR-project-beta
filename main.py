import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Đọc âm thanh từ tệp
file_path = r'E:\Project Speech recognize\Data\10hzto50hztest.mp3'
y, sr = librosa.load(file_path)
print(librosa.load(file_path, sr=None))
# Tính toán spectrogram
spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
print("MFCC: ",librosa.feature.chroma_stft(y, sr=22050))
# Hiển thị spectrogram
librosa.display.specshow(librosa.power_to_db(spectrogram, ref=np.max), y_axis='mel', x_axis='time')

# Thêm tiêu đề và màu sắc
plt.title('Spectrogram')
plt.colorbar(format='%+2.0f dB')
plt.show()