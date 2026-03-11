import librosa
import numpy as np

def extract_features(file_path):

    # โหลดไฟล์เสียง
    y, sr = librosa.load(file_path)

    # ตรวจจับ pitch
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

    pitch_values = []

    for i in range(pitches.shape[1]):
        index = magnitudes[:, i].argmax()
        pitch = pitches[index, i]

        if pitch > 0:
            pitch_values.append(pitch)

    if len(pitch_values) == 0:
        return None

    pitch_values = np.array(pitch_values)

    features = {
        "average_pitch": float(np.mean(pitch_values)),
        "min_pitch": float(np.min(pitch_values)),
        "max_pitch": float(np.max(pitch_values)),
        "pitch_std": float(np.std(pitch_values))
    }

    return features
