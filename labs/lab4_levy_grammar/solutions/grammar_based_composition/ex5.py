# %% Import libraries
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from classes import Composer, Grammar_Sequence

# %%

upbeat_grammar={
    "S":["M", "SM"],
    "M": ["HH","VVV", "QHQ"],    
    "H": ["h", "QQ","tqtqtq","$h", "otototoo", "OQO"],
    "V": ["th", "ph"], 
    "Q": ["q", "OO", "oo", "tototo","$q", "potopo", "popoto"],
    "O": ["o", "$o"]
}


upbeat_word_dur={"h":0.5, # half-measure
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


if __name__=="__main__":
    fn_out="upbeat_composition.wav"

    NUM_M=8
    START_SEQUENCE="M"*NUM_M
    G=Grammar_Sequence(upbeat_grammar)        
        
    seqs=G.create_sequence(START_SEQUENCE)
    print("\n".join(seqs), "\nFinal sequence: ", G.sequence)    
    C= Composer("sounds/cymb.wav", upbeat_word_dur)
    C.create_sequence(G.sequence)
    C.write("out/"+fn_out)
    