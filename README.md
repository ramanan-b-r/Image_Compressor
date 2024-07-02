# Image Compressor
A simple image compressing tool made using Python, OpenCV and CustomTkinter

#How to use
-Store all the images that need to be compressed in a folder. Select this folder while the program asks you to choose the source files.
-Create a destination folder for the compressed images to be stored and choose this when prompted by the program for choosing the save location.
-After choosing the source and the destination folder select the quality by dragging the slider.
-Higher quality --> Bigger file size but image quality is greater.
-Lower quality  --> Smaller file size but image quality is lower.

#Notes
-The images *have* to be stored in a folder
-In my testing anything above 85 for the quality should be good and will allow you 
to preserve the quality ff the image while at the same time not making the file size too big.(your mileage may vary)
#Libraries used
OpenCV
CustomTkinter
