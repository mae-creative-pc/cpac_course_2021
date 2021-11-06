# %% Import libraries
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from classes import Composer, Grammar_Sequence

# %%

upbeat_grammar={
    "S":["M", "SM"],
    "M": ["HH", "ththth"],    
    "H": ["h", "$h", "QQ", "tqtqtq", "oqo", "$qq", "$oqo",
                           "pqtqtq", "pqpqtq", "pqtqpq"],
    "Q": ["q", "$q", "OO", "tototo","pototo", "popoto", "potopo"],
    "O": ["o", "$o",],
}

upbeat_word_dur={"h":0.5, # half-measure
                 "q":0.25, # quarter-measure
                 "o":1/8,#, your code here: add "o"
                "$h":0.5,
                "$q":0.25,
                "$o":1/8,
                "th": (2/2)/3,                                
                "tq": (2/4)/3,                                
                "to": (2/8)/3,
                "ph": (2/2)/3,                
                "pq": (2/4)/3,                                                
                "po": (2/8)/3,
          }




if __name__=="__main__":
    fn_out="upbeat_composition.wav"

    NUM_M=8
    START_SEQUENCE="M"*NUM_M
    G=Grammar_Sequence(upbeat_grammar)        
        
    seqs=G.create_sequence(START_SEQUENCE)
    print("\n".join(seqs), "\nFinal sequence: ", G.sequence)    
    C= Composer("sounds/imsd.wav", upbeat_word_dur, BPM=160, )
    C.create_sequence(G.sequence)
    C.write("out/"+fn_out)
    