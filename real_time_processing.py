import pyaudio
import numpy as np
import time

def audio_callback(in_data, frame_count, time_info, status):
    # Xử lý âm thanh ở đây (ví dụ: thêm hiệu ứng biến đổi tần số)
    audio_data = np.frombuffer(in_data, dtype=np.int16)
    
    # Nâng tần số (ví dụ: tăng 1.5 lần)
    increased_amplitude_data = (audio_data * 1.5).clip(-100000, 100000).astype(np.int16)

    return increased_amplitude_data.tobytes(), pyaudio.paContinue

def main():
    p = pyaudio.PyAudio()

    # Thiết lập thông số thu âm
    FORMAT = pyaudio.paInt16
    CHANNELS = 4
    RATE = 44100
    CHUNK_SIZE = 1024

    # Mở stream thu âm
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    output=True,
                    frames_per_buffer=CHUNK_SIZE,
                    stream_callback=audio_callback)

    print("Bắt đầu thu âm và xử lý giọng nói...")

    # Bắt đầu stream
    stream.start_stream()

    try:
            time.sleep(0.0)
    except KeyboardInterrupt:
        pass

    print("Dừng thu âm và kết thúc chương trình.")

    # Dừng stream và đóng PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    main()
