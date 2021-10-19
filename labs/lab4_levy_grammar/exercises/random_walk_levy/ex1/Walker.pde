float STEPSCALE=10;

class Walker {
  PVector position;
  PVector prevPosition;
  
  Walker() {
    this.position=CENTER_SCREEN.copy();
    this.prevPosition=this.position.copy();    
  }
  void draw() {    
    stroke(255);
    /* your code */
  }

  void update() {    
    PVector step;
    /* your code */
    
    this.position.add(step);
    this.position.x=constrain(this.position.x, 0, width);    
    this.position.y=constrain(this.position.y, 0, height);
  }
}

float montecarlo() {
  /* your code */
}
