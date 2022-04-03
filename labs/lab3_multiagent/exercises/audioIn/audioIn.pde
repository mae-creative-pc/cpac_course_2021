import ddf.minim.*;
import ddf.minim.analysis.*;

int frameLength = 1024; //--> when this is low, it may take more to compute
AudioInput mic;
FFT fft;
Minim minim;
float maxEnergy=0;
   
void setup(){
   size(1280, 720);
   minim= new Minim(this);
   mic = minim.getLineIn(Minim.MONO, frameLength);
   fft = new FFT(mic.bufferSize(), mic.sampleRate());
   fft.window(FFT.HAMMING);
}

void draw(){
  
  background(0);
   fft.forward(this.mic.mix);
   float band_energy;
   float rectWidth=width/fft.specSize();
   fill(255);
   for(int i=0; i<fft.specSize(); i++){
      band_energy=this.fft.getBand(i)/fft.specSize();  
      
      rect(i*rectWidth, height, rectWidth, max(-height, -10*height*band_energy));
      maxEnergy=max(maxEnergy, band_energy);
   }  
}
