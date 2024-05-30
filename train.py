import torch
import torch.nn as nn
import torch.optim as optim
import librosa
import numpy as np

# Định nghĩa mô hình
class SpeechClassificationModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(SpeechClassificationModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.fc(out[:, -1, :])
        return out

# Hàm huấn luyện mô hình
def train(model, train_loader, criterion, optimizer, epochs=10):
    model.train()
    for epoch in range(epochs):
        for inputs, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
        print(f'Epoch {epoch + 1}/{epochs}, Loss: {loss.item()}')

# Hàm kiểm thử mô hình
def test(model, test_loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in test_loader:
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    accuracy = correct / total
    print(f'Test Accuracy: {accuracy * 100}%')

# Load dữ liệu và chuyển đổi thành tensor PyTorch
# (Bạn cần thay đổi phần này để phản ánh cách bạn tổ chức dữ liệu)
def load_data(file_paths, labels):
    data = []
    for file_path, label in zip(file_paths, labels):
        y, sr = librosa.load(file_path, sr=None)
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        data.append((torch.tensor(mfccs.T).unsqueeze(0), torch.tensor(label)))
    return data

# Thực hiện các bước trên để huấn luyện và kiểm thử mô hình
if __name__ == "__main__":
    # Thay đổi theo nhu cầu
    input_size = 13
    hidden_size = 128
    num_classes = 3
    learning_rate = 0.001
    batch_size = 32

    # Khởi tạo mô hình, hàm mất mát, và bộ tối ưu
    model = SpeechClassificationModel(input_size, hidden_size, num_classes)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    # Tạo dữ liệu huấn luyện và kiểm thử (thay đổi đường dẫn và nhãn)
    train_file_paths = ["path_to_train_audio_1.wav", "path_to_train_audio_2.wav", ...]
    train_labels = [0, 1, ...]
    train_data = load_data(train_file_paths, train_labels)

    test_file_paths = ["path_to_test_audio_1.wav", "path_to_test_audio_2.wav", ...]
    test_labels = [0, 1, ...]
    test_data = load_data(test_file_paths, test_labels)

    # Chia thành batch và tạo DataLoader
    train_loader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, shuffle=True)
    test_loader = torch.utils.data.DataLoader(test_data, batch_size=batch_size, shuffle=False)

    # Huấn luyện và kiểm thử mô hình
    train(model, train_loader, criterion, optimizer, epochs=10)
    test(model, test_loader)





# import librosa
# import os
# import json

# DATASET_PATH = "dataset"
# JSON_PATH = "data.json"
# SAMPLES_TO_CONSIDER = 22050 # 1 sec. of audio


# def preprocess_dataset(dataset_path, json_path, num_mfcc=13, n_fft=2048, hop_length=512):
#     """Extracts MFCCs from music dataset and saves them into a json file.

#     :param dataset_path (str): Path to dataset
#     :param json_path (str): Path to json file used to save MFCCs
#     :param num_mfcc (int): Number of coefficients to extract
#     :param n_fft (int): Interval we consider to apply FFT. Measured in # of samples
#     :param hop_length (int): Sliding window for FFT. Measured in # of samples
#     :return:
#     """

#     # dictionary where we'll store mapping, labels, MFCCs and filenames
#     data = {
#         "mapping": [],
#         "labels": [],
#         "MFCCs": [],
#         "files": []
#     }

#     # loop through all sub-dirs
#     for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):

#         # ensure we're at sub-folder level
#         if dirpath is not dataset_path:

#             # save label (i.e., sub-folder name) in the mapping
#             label = dirpath.split("/")[-1]
#             data["mapping"].append(label)
#             print("\nProcessing: '{}'".format(label))

#             # process all audio files in sub-dir and store MFCCs
#             for f in filenames:
#                 file_path = os.path.join(dirpath, f)

#                 # load audio file and slice it to ensure length consistency among different files
#                 signal, sample_rate = librosa.load(file_path)

#                 # drop audio files with less than pre-decided number of samples
#                 if len(signal) >= SAMPLES_TO_CONSIDER:

#                     # ensure consistency of the length of the signal
#                     signal = signal[:SAMPLES_TO_CONSIDER]

#                     # extract MFCCs
#                     MFCCs = librosa.feature.mfcc(signal, sample_rate, n_mfcc=num_mfcc, n_fft=n_fft,
#                                                  hop_length=hop_length)

#                     # store data for analysed track
#                     data["MFCCs"].append(MFCCs.T.tolist())
#                     data["labels"].append(i-1)
#                     data["files"].append(file_path)
#                     print("{}: {}".format(file_path, i-1))

#     # save data in json file
#     with open(json_path, "w") as fp:
#         json.dump(data, fp, indent=4)


# if __name__ == "__main__":
#     preprocess_dataset(DATASET_PATH, JSON_PATH)
