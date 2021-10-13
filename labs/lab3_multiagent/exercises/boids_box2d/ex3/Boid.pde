
float AVOID_DIST=6;
float ALIGN_DIST=25;
class Boid{
    Body body;
    Box2DProcessing  box2d;
    color defColor = color(200, 200, 200);
    color contactColor;
    float time_index, dur_frames;
    int nextPoint;
    SoundFile sample;
    
    Boid(Box2DProcessing  box2d, CircleShape ps, BodyDef bd, Vec2 position,SoundFile sample, int nextPoint){
        this.box2d = box2d;    
        bd.position.set(position);
        this.body = this.box2d.createBody(bd);
        this.body.m_mass=1;
        this.body.createFixture(ps, 1);
        this.body.getFixtureList().setRestitution(0.8);
        this.body.setUserData(this);  
        this.sample=sample;
        
        this.time_index=0;
        this.dur_frames=3*frameRate;
        this.nextPoint=nextPoint;
        colorMode(HSB, 255);
        this.contactColor= color(random(0,255),255,255);
        colorMode(RGB, 255);
    }
    void applyForce(Vec2 force){
      this.body.applyForce(force, this.body.getWorldCenter());      
    }
    void draw(){
        Vec2 posPixel=this.box2d.getBodyPixelCoord(this.body);
        // your code here
        
    }
    void changeColor(){
      // your code here
    }
    void play(){
     // your code here: check if it's already playing, before make it play again
    }
    void update(ArrayList<Boid> boids){
      Vec2 myPosW=this.body.getPosition();
      Vec2 myVel=this.body.getLinearVelocity();
      Vec2 otherPosW;
      Vec2 otherVel;
      Vec2 direction;
      float dist;
      Vec2 align_force=new Vec2(0,0);
      Vec2 avoid_force=new Vec2(0,0);
      
      for(Boid other: boids){        
        if(this.body==other.body){continue;}
        otherPosW=other.body.getPosition();
        direction=otherPosW.sub(myPosW);
        if(direction.length()<AVOID_DIST){
           direction.normalize();
           avoid_force.add(direction.mul(-1));
        }
        else if(direction.length()<ALIGN_DIST){
           otherVel=other.body.getLinearVelocity();
           
           align_force.add(otherVel.sub(myVel));
        }
      }
      if(avoid_force.length()>0){this.applyForce(avoid_force);}
      if(align_force.length()>0){this.applyForce(align_force);}
    }
    
    void kill(){
        this.box2d.destroyBody(this.body);
    }

   
}
