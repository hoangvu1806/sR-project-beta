import librosa
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def compute_mfcc(file_path, n_mfcc=13, hop_length=512, n_fft=2048):
    # Load âm thanh từ file
    y, sr = librosa.load(file_path)

    # Tính MFCCs với số lượng coefficients là n_mfcc
    mfccs = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_fft=n_fft, n_mfcc=n_mfcc)

    return mfccs

def compute_cosine_similarity(mfccs1, mfccs2):
    # Reshape ma trận MFCC để tránh lỗi
    mfccs1_flat = mfccs1.flatten().reshape(1, -1)
    mfccs2_flat = mfccs2.flatten().reshape(1, -1)

    # Tính cosine similarity
    similarity = cosine_similarity(mfccs1_flat, mfccs2_flat)[0, 0]

    return similarity

# Sử dụng hàm
file_path1 = r"Data/test1.wav"
file_path2 = r"E:\Project Speech recognize\Data\10hzto50hztest.mp3"

# Chọn cùng một số lượng coefficients (n_mfcc) khi tính MFCCs
n_mfcc = 13
mfccs1 = compute_mfcc(file_path1, n_mfcc=n_mfcc)
mfccs2 = compute_mfcc(file_path2, n_mfcc=n_mfcc)

print(mfccs1)
print(mfccs1)

# similarity = compute_cosine_similarity(mfccs1, mfccs2)
# print("Cosine Similarity:", similarity)


