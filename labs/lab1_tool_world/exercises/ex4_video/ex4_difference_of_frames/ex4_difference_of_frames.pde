import processing.video.*;

Capture cam;
PImage old_frame;
PImage cur_frame;
boolean first_frame=true;

void setup() {
  size(640, 480);

  String[] cameras = Capture.list();

  if (cameras.length == 0) {
    println("There are no cameras available for capture.");
    exit();
  } else {
    println("Available cameras:");
    for (int i = 0; i < cameras.length; i++) {
      println(i, cameras[i]);
    }
    
    cam = new Capture(this, cameras[0]);
    cam.start();
    
  }
  
}

void copy2img(Capture camera, PImage img) {
  img.loadPixels();
  for (int i=0; i<camera.width*camera.height; i++) {
    img.pixels[i]=camera.pixels[i];
  }
  img.updatePixels();
}

void copy_img(PImage src, PImage dst) {
  dst.set(0,0,src);
}
void effectDiffFrames(PImage img){
  copy2img(cam, cur_frame);
  if(first_frame){
    copy2img(cam, old_frame);
    first_frame=false;
    return; 
  }
  img.loadPixels(); // creates the pixels[] array
  old_frame.loadPixels();
  float r, oldr, g, oldg, b, oldb;
  colorMode(RGB, 255);
  for (int loc=0; loc<img.width*img.height; loc++){
    r= red(cur_frame.pixels[loc]);
    oldr= red(old_frame.pixels[loc]);
    g= green(cur_frame.pixels[loc]);
    oldg= green(old_frame.pixels[loc]);
    b= blue(cur_frame.pixels[loc]);
    oldb= blue(old_frame.pixels[loc]);
    img.pixels[loc]=color(Math.abs(r-oldr), Math.abs(g-oldg), Math.abs(b-oldb));
  }
  img.updatePixels();
  copy_img(cur_frame, old_frame);
}
void draw() {
  if (! cam.available()) {return;}
  cam.read();
  if(first_frame){
    cur_frame=createImage(cam.width,cam.height,RGB);
    old_frame=createImage(cam.width,cam.height,RGB);  
  }
  PImage img=createImage(cam.width,cam.height,RGB);
  
  effectDiffFrames(img);
  
  if(img.width>0){
    image(img, 0, 0);
  }

}
