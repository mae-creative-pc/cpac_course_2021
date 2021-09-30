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
  if (first_frame) {
    old_frame = createImage(img.width, img.height, RGB);
    cur_frame = createImage(img.width, img.height, RGB);
    copy_img(img, old_frame);
    first_frame=false;
    img = createImage(0, 0, RGB);
    
    return; 
  }
  copy2img(cam, cur_frame);
  img.loadPixels();
  float R, G, B;
  for (int i=0; i<cam.width*cam.height; i++) {
    R=abs(red(old_frame.pixels[i])-red(cur_frame.pixels[i])); 
    G=abs(green(old_frame.pixels[i])-green(cur_frame.pixels[i]));    
    B=abs(blue(old_frame.pixels[i])-blue(cur_frame.pixels[i]));
    img.pixels[i]=color(R, G, B);
  }
  img.updatePixels();
  copy_img(cur_frame, old_frame);  
}
void draw() {
  if (! cam.available()) {return;}
  cam.read();
  PImage img=createImage(cam.width,cam.height,RGB);
  
  effectDiffFrames(img);
  
  if(img.width>0){
    image(img, 0, 0);
  }

}
