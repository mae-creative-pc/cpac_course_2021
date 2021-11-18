# %% Import libraries
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from classes import Composer, Grammar_Sequence

# %%
basic_grammar={
    "S":["M", "SM"],
    "M": ["HH"],    
    "H": ["h", "qq"],
}

if __name__=="__main__":
    fn_out="basic_composition.wav"

    NUM_M=8
    START_SEQUENCE="M"*NUM_M
    G=Grammar_Sequence(basic_grammar)        
        
    seqs=G.create_sequence(START_SEQUENCE)
    print("\n".join(seqs), "\nFinal sequence: ", G.sequence)    
    C= Composer("sounds/cymb.wav", BPM=174)
    C.create_sequence(G.sequence)
    C.write("out/"+fn_out)
    