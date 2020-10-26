Assignment 13: 

1. OpenCV Yolo: SOURCE

		Run this above code on your laptop or Colab. 
		
		Take an image of yourself, holding another object which is there in COCO data set (search for COCO classes to learn). 
		
		Run this image through the code above. 
		
		Upload the link to GitHub implementation of this
		
		Upload the annotated image by YOLO. 
		
		
2. Share your NEWLY annotated (same as 12, but annotated using new tool) images with Zoheb by Wednesday at midnight. Take the set back for training on Thursday.


3. Training Custom Dataset on Colab for YoloV3

		Refer to this Colab File: LINK
		
		Refer to this GitHub Repo
		
		Collect a dataset from the last assignment and re-annotate them. Steps are explained in the readme.md file on GitHub.
		
	Once done:
	
		Download a very small (~10-30sec) video from youtube which shows your classes. 
		
		Use ffmpeg to extract frames from the video. 
		
		Upload on your drive (alternatively you could be doing all of this on your drive to save upload time)
		
		Infer on these images using detect.py file. **Modify** detect.py file if your file names do not match the ones mentioned on GitHub. 
		
		python detect.py --conf-thres 0.3 --output output_folder_name
		
		Use ffmpeg  to convert the files in your output folder to video
		
		Upload the video to YouTube. 
		
		Share the link to your GitHub project with the steps as mentioned above
		
		Share the link to your YouTube video
		
		Share the link of your YouTube video on LinkedIn, Instagram, etc! You have no idea how much you'd love people complimenting you! 
		
		
	OPEN CV object detection with coco dataset:
	
	![image](https://github.com/rameshveer/School_of_AI-EVA_5/blob/master/S13/Yolo%20Open%20CV/Annotated_Yolo_Images/me_mobile.jpg)
	
	![image](https://github.com/rameshveer/School_of_AI-EVA_5/blob/master/S13/Yolo%20Open%20CV/Annotated_Yolo_Images/lap_bottle.jpg)
	
	
	PPE object detection after Yolo training with custom dataset:
	
	![image](https://github.com/rameshveer/School_of_AI-EVA_5/blob/master/S13/Yolo%20Open%20CV/Annotated_Yolo_Images/Unknown.jpg)
		
