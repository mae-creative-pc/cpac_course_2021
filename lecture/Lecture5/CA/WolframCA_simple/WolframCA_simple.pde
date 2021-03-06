// Wolfram Cellular Automata
// Daniel Shiffman <http://www.shiffman.net>

// Simple demonstration of a Wolfram 1-dimensional cellular automata

CA ca;   // An instance object to describe the Wolfram basic Cellular Automata


void setup() {
  //size(800, 400);
  fullScreen();
  background(255);
  ca = new CA();                 // Initialize CA
}

void draw() {
  ca.display();    // Draw the CA
  if (ca.generation < height/ca.w) {
    ca.generate();
  }
}
