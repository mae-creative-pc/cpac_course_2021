import numpy as np
from librosa.beat import beat_track

def compute_beats(y, sr):
    return beat_track(y, sr=sr)

def add_samples(y, sample, sample_beats):
    Ns=sample.size
    y_out=y.copy()
    for beat in sample_beats:
        y_out[beat:beat+Ns]+=sample
    return y_out/np.max(np.abs(y_out))


