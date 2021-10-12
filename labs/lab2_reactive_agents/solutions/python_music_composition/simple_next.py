    
import platform
import sys
import time


from constants import ID_START
    
from classes import Agent, Composition

class Simple_Next(Composition):
    def __init__(self, BPM=60):
        Composition.__init__(self,BPM=BPM)
            
    def next(self):
        if self.id ==ID_START: # start
            self.midinote=60
            self.dur =1
            self.amp = 1
            self.id=0
        elif self.id==0:
            self.midinote=self.midinote+1
            if self.midinote==84:
                self.id=1
        elif self.id==1:
            self.midinote -=1
            if self.midinote==60:
                self.id = 0

if __name__=="__main__":
    n_agents=1
    composer=Simple_Next()
    agents=[_ for _ in range(n_agents)]
    agents[0] = Agent(57120, "/note_effect", composer)

    input("Press any key to start \n")
    for agent in agents:
        agent.start()
    try: # USE CTRL+C to exit     
        while True:
            time.sleep(10)
    except:         
        for agent in agents:              
            agent.kill()
            agent.join()
        sys.exit()

# %%