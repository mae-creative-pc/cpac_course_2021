

import re
import random
import soundfile as sf
import librosa
import numpy as np

default_word_dur={"h":0.5, # half-measure
          "q":0.25, # quarter-measure
}


def random_elem_in_list(list_of_elems):
    return list_of_elems[random.randint(0,len(list_of_elems)-1)]

# %% Grammar Sequence
class Grammar_Sequence:
    def __init__(self, grammar):
        self.grammar=grammar
        self.grammar_keys=list(grammar.keys())
        self.N=len(self.grammar_keys)
        self.sequence=""
       
    def find_symbol(self, symbol):
        return [m.start() for m in re.finditer(symbol, self.sequence)]
    def replace(self, index, symbol, convert_to):
        len_symbol=len(symbol)
        self.sequence=self.sequence[:index]+convert_to+self.sequence[index+len_symbol:]
    def convert_sequence(self):        
        symbol=random_elem_in_list(self.grammar_keys)
        while symbol not in self.sequence:
            symbol=random_elem_in_list(self.grammar_keys)
            
        index=random_elem_in_list(self.find_symbol(symbol))
        convert_to= random_elem_in_list(self.grammar[symbol])
        self.replace(index, symbol, convert_to)
        
    def create_sequence(self, start_sequence):
        self.sequence=start_sequence
        sequence_transformation=[start_sequence]
        while (self.sequence!=self.sequence.lower()):
            self.convert_sequence()
            sequence_transformation.append(self.sequence)
        return sequence_transformation
# %% Composer
class Composer():
    def __init__(self, fn, word_dur=default_word_dur, sr=-1, BPM=120):
        if sr==-1:
            self.sample, self.sr =  librosa.load(fn)     
        else:
            self.sample, self.sr =  librosa.load(fn,sr=sr)         
        self.sampleN=self.sample.size
        self.BPM=BPM
        self.q_bpm=60/self.BPM
        self.m_bpm=4*self.q_bpm
        self.sequence=[]
        self.word_dur=word_dur
    def split_sequence(self, sequence):
        k=0
        sym_seq=[]
        dur_seq=[]
        while k<len(sequence):
            if sequence[k] in "$tp":
                sym=sequence[k]+sequence[k+1]
                k+=2
            else:
                sym=sequence[k]
                k+=1
            sym_seq.append(sym)
            
            dur_seq.append(self.word_dur[sym])
        return dur_seq, sym_seq
    def compute_duration(self, dur_seq):
        duration_in_notes=0
        for dur in dur_seq:
            duration_in_notes+=dur
        return duration_in_notes        
    def create_sequence(self, sequence):
        dur_seq, sym_seq=self.split_sequence(sequence)
        duration_in_notes=self.compute_duration(dur_seq)
        
        duration_in_seconds=duration_in_notes*self.m_bpm
        self.sequence=np.zeros((int(duration_in_seconds*self.sr),))
        idx=0
        for note, symbol in zip(dur_seq, sym_seq):
            if not (symbol.startswith("$") or symbol.startswith("p")):
                if self.sequence.size > idx+self.sampleN: 
                    self.sequence[idx:idx+self.sampleN]+=self.sample
                else:
                    K=self.sequence.size-idx
                    self.sequence[idx:]+=self.sample[:K]
                    self.sequence[:self.sampleN-K]+=self.sample[K:]
            idx+=int(note*self.sr*self.m_bpm)
    def write(self, fn_out="out.wav", repeat=1, write=True):
        sequence_to_write=np.repeat(self.sequence, (repeat,))
        if write:
            sf.write(fn_out, sequence_to_write, self.sr)
        else:
            return sequence_to_write