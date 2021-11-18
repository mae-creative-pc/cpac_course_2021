# %% Import libraries
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from classes import Composer, Grammar_Sequence

# %%

clave_grammar={
    "S":["M","SM"],
    "M":["R", "F"], #"rumba" or "son"
    "R":["o$ss$o$ss$ooq"],
    "F":["o$ss$oo$ooq"],
}


clave_word_dur={
    "h":0.5, # half-measure
    "q":0.25, # quarter-measure
    "o":1/8,#, your code here: add "o"
    "s":1/16,#, your code here: add "o"    
    "$h":0.5,
    "$q":0.25,
    "$o":1/8,    
    "$s":1/16,
    "th": (2/2)/3,                                
    "tq": (2/4)/3,                                
    "to": (2/8)/3,
    "ph": (2/2)/3,                
    "pq": (2/4)/3,                                                
    "po": (2/8)/3,
}


if __name__=="__main__":
    fn_out="clave_composition.wav"

    NUM_M=8
    START_SEQUENCE="M"*NUM_M
    G=Grammar_Sequence(clave_grammar)        
        
    seqs=G.create_sequence(START_SEQUENCE)
    print("\n".join(seqs), "\nFinal sequence: ", G.sequence)    
    C= Composer("sounds/cough.wav", clave_word_dur, BPM=160)
    C.create_sequence(G.sequence)
    C.write("out/"+fn_out)
    