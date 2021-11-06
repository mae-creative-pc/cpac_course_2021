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
    strokeWeight(3);
    line(this.prevPosition.x, this.prevPosition.y, this.position.x, this.position.y);
    this.prevPosition= this.position.copy();
  }

  void update() {    
    PVector step = new PVector(random(-1,1), random(-1,1));
    step.normalize();
    float stepsize=montecarlo(); 
    step.mult(stepsize*STEPSCALE);
    this.position.add(step);
    this.position.x=constrain(this.position.x, 0, width);    
    this.position.y=constrain(this.position.y, 0, height);
  }
}

float montecarlo() {
  while(true){
    float R1= random(1);
    float p= random(1);
    float R2= random(1);
    if(p>R2){ return R1; }
  }
}
