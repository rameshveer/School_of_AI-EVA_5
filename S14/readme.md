## Dataset creation as part of Assignment 14


### Created the following datasets for the PPE images collected from web scrapping.

1. Images with Bounding box classes using Annotation tool
2. Depth images created with MiDas model
3. Plane images created with plane-rcnn model

Google Drive link - https://drive.google.com/drive/folders/1IhgInibr4296L8YY4pWcD-rOcsAirINv?usp=sharing

### 1. Images with Bounding box classes using Annotation tool
      PPE objects to be detected from the required video/image are,

      hard hat
      vest
      mask
      boots
    
      Bounding Boxes & labels for above classes were done using this annotation tool -  https://github.com/miki998/YoloV3_Annotation_Tool
      
      

### 2. Depth images created with MiDas model

        * MiDaS model was cloned from this repo -  https://github.com/intel-isl/MiDaS
        
        * PPE images were placed in the input folder 
        
        * Pre-trained model was used to compute depth from a single image.
        
        * Depth images were extracted in Grayscale


### 3. Plane images created with plane-rcnn model

        * Plane-RCNN model was cloned from this repo - https://github.com/NVlabs/planercnn
        
        * Above repo was modified to generate only plane segmentation images.
        
        * evaluate.py code was modified to handle .jpeg images as well along with .jpg & .png.
          To handle any no. of. images as input.
          To generate plane images with same name as input image.
        
        * 3590 images were segmented.
 
 
 #### All the images are placed in below Google drive link,          

Google Drive link - https://drive.google.com/drive/folders/1IhgInibr4296L8YY4pWcD-rOcsAirINv?usp=sharing
