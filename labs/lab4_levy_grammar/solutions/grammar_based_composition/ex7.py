# %% Import libraries
import numpy as np
import os
import soundfile as sf
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from classes import Composer, Grammar_Sequence

# ==== GRAMMARS
basic_grammar={
    "S":["M", "SM"],
    "M": ["HH"],    
    "H": ["h", "qq"],
}

slow_grammar={
    "S":["M", "SM"],
    "M": ["HH","w", "$w"],    
    "H": ["h", "$h"],
}

octave_grammar={
    "S":["M", "SM"],
    "M": ["HH"],    
    "H": ["h", "QQ"],
    "Q": ["q", "oo"],
}

triplet_grammar={
    "S":["M", "SM"],
    "M": ["HH", "ththth"],    
    "H": ["h", "QQ","tqtqtq","$h"],
    "Q": ["q", "OO", "oo", "tototo","$q"],
    "O": ["o", "$o"]
}
upbeat_grammar={
    "S":["M", "SM"],
    "M": ["HH", "ththth","VVV", "QHQ"],    
    "H": ["h", "QQ","tqtqtq","$h", "otototoo", "OQO"],
    "V": ["th", "ph"], 
    "Q": ["q", "OO", "oo", "tototo","$q", "potopo", "popoto"],
    "O": ["o", "$o"]
}

word_dur={"h":0.5, # half-measure
          "q":0.25, # quarter-measure
          "o":1/8, # octave-measure
          "$h": 0.5,
          "$q": 0.25,
          "$o": 1/8,
          "th": 1/3,
          "tq": 1/6,
          "to": 1/12,
          "ph": 1/3,
          "pq": 1/6,
          "po": 1/12,
          "w": 1,
          "$w": 1,          
}

class Track:
    def __init__(self, composer, grammar, gain, sr):
        self.composer=composer
        self.grammar=grammar
        self.gain=gain
        self.sr=sr
    def create_sequence(self, start_sequence):
        self.grammar.create_sequence(start_sequence)                    
        self.composer.create_sequence(self.grammar.sequence)
    
# write_mix
def write_mix(tracks, fn_out="out.wav"):
    max_size=0
    for track in tracks:
        max_size=max(max_size, track.composer.sequence.size)
    total_track=np.zeros((len(tracks), max_size))
    for i, track in enumerate(tracks):
        total_track[i, 0:track.composer.sequence.size]=track.gain*track.composer.sequence
    total_track = np.sum(total_track, axis=0)                            
    total_track=0.707*total_track/np.max(np.abs(total_track))
    sf.write(fn_out, total_track, track.sr)


# %% main script
if __name__=="__main__":
    
    NUM_M = 8
    START_SEQUENCE = "M"*NUM_M
    SR=44100
    BPM=120
    samples=[#your code here
             ]
    grammars=[# your grammars
               ]
    gains = [ #your gains
                 ]
    
    tracks=[]
    
    for i in range(len(samples)):
        track=Track(Composer("sounds/"+samples[i], word_dur, BPM=BPM, sr=SR),
                    Grammar_Sequence(grammars[i]), gains[i], SR)
        track.create_sequence(START_SEQUENCE)
        tracks.append(track)
        
    fn_out="multitrack.wav"
    write_mix(tracks, fn_out="out/multitrack.wav")