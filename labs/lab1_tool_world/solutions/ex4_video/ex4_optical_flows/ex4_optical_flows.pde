import gab.opencv.*;
import processing.video.*;

Capture cam;
boolean camera_found=false;

OpenCV opencv=null;


boolean find_camera() {
  /*
  Find a camera,
   return true if it is found (cam is initialized),
   return false otherwise
   */

  // if camera was already found, it returns true
  if (camera_found) {
    return camera_found;
  }

  // else tries to get the list of cameras
  String[] cameras = Capture.list();

  if (cameras.length == 0) { // no camera available THIS TIME
    println("There are no cameras available for capture.");
    //exit();
  } else {   // camera availables, print the list and initialize cam
    println("Available cameras:");
    for (int i = 0; i < cameras.length; i++) {
      println(i, cameras[i]);
    }
    cam = new Capture(this, cameras[0]);
    cam.start();
    camera_found=true;
  }
  return camera_found;
}

void setup() {
  size(640, 480);
}

void copy2img(Capture camera, PImage img) {
  img.loadPixels();
  for (int i=0; i<camera.width*camera.height; i++) {
    img.pixels[i]=camera.pixels[i];
  }
  img.updatePixels();
}


void opticalFlow(PImage img) {
  opencv.loadImage(img);  // load the current image and compute Optical Flow
  opencv.calculateOpticalFlow();

  // we will divide the image in a grid of size:
  int grid_size=10;
  int half_grid=5;

  // center of each cell of the grid
  int c_x=0;
  int c_y=0;
  PVector aveFlow;  // here we will store the optical flow
  //image(img,0,0);   // we plot the image
  //stroke(255,0,0);
  strokeWeight(2);

  for (int w=0; w<img.width; w+=grid_size) {
    for (int h=0; h<img.height; h+=grid_size) {
      // compute the average Flow over the region from w, h to w+grid_size, h+grid_size
      aveFlow = opencv.getAverageFlowInRegion(w, h, grid_size, grid_size);

      // update the center position
      c_x=w+half_grid;
      c_y=h+half_grid;
      int loc = int(c_x+c_y*img.width);

      // say we want the color of the central pixel
      stroke(red(img.pixels[loc]), green(img.pixels[loc]), blue(img.pixels[loc]));
      // draw a line from each center of the cell toward the direction of the average flow
      line(c_x, c_y, c_x+min(aveFlow.x*half_grid, half_grid), c_y+min(aveFlow.y*half_grid, half_grid));
    }
  }
}

void draw() {
  if (! find_camera()) {
    return;
  }
  if (! cam.available()) {
    return;
  }
  cam.read();
  if (opencv ==null) {// not initialized
    opencv = new OpenCV(this, cam.width, cam.height);
  }
  println("opencv", opencv);
  
  PImage img=createImage(cam.width, cam.height, RGB);
  copy2img(cam, img);
  opticalFlow(img);
}
