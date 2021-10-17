# %% Import libraries
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from classes import Composer, Grammar_Sequence

# %%

clave_grammar={
    "S":["M", "SM"],
    "M": ["R", "T"],    
    "T": ["o$ss$oo$ooq"],
    "R": ["o$ss$o$ss$ooq"], 
    
}


clave_word_dur={
          "q":0.25, # quarter-measure
          "o":1/8, # octave-measure
          "s": 1/16,
          "$q": 0.25,
          "$o": 1/8,
          "$s": 1/16,
}


if __name__=="__main__":
    fn_out="clave_composition.wav"

    NUM_M=8
    START_SEQUENCE="M"*NUM_M
    G=Grammar_Sequence(clave_grammar)        
        
    seqs=G.create_sequence(START_SEQUENCE)
    print("\n".join(seqs), "\nFinal sequence: ", G.sequence)    
    C= Composer("sounds/cymb.wav", clave_word_dur)
    C.create_sequence(G.sequence)
    C.write("out/"+fn_out)
    