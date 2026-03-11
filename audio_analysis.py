import librosa
import numpy as np

def analyze_voice(file_path):

    y, sr = librosa.load(file_path)

    pitch = librosa.yin(y,
                        fmin=50,
                        fmax=500)

    avg_pitch = np.mean(pitch)

    return {
        "average_pitch": float(avg_pitch)
    }
