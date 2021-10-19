# %% Import libraries
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from classes import Composer, Grammar_Sequence

# %%

upbeat_grammar={ #your code here}


upbeat_word_dur={#your code here}


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
    