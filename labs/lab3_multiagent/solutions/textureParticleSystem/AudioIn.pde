import ddf.minim.*;
import ddf.minim.analysis.*;

int frameLength = 1024; //--> when this is low, it may take more to compute


class AudioIn{
   AudioInput mic;
   AudioPlayer song;  

   FFT fft;
   Minim minim;
   float maxEnergy=1;
   float energy=1;
   AudioIn(textureParticleSystem app){
     this.minim= new Minim(app);
     this.mic = minim.getLineIn(Minim.MONO, frameLength);
     this.fft = new FFT(mic.bufferSize(), mic.sampleRate());
     this.fft.window(FFT.HAMMING);
     this.energy=0;
   }
   float getEnergy(){    
    this.fft.forward(this.mic.mix);
    float energy = 0;
    for(int i=0; i<this.fft.specSize(); i++){
      float band_energy=this.fft.getBand(i);
      energy+=band_energy;
    }
    energy=map(energy,0, this.fft.specSize(), 0, 1);
    this.energy= this.energy*0.1+energy*0.9;    
    return this.energy;
  }
}
