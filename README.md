# Raspberry Pi Camera
This project uses a raspberry pi to take time lapsed images , which are then uploaded to Google drive for storage and processing into time lapse movies.

## Steps:
* Setup rclone on your raspberry pi

  Rclone helps you connect your Raspberry pi to your google drive through python commands.
  You can follow the instructions [here](https://pimylifeup.com/raspberry-pi-rclone/). I recommend connecting your Raspberry pi to a screen for this step as you might need to log in to your google account on a browser inside your Rpi.

* Install screen on your Raspberry pi

  Screen lets you create multiple terminal instances . We can use that to run 2 or more python scripts parallelly.
  
  You can use the below instructions to work with screen.
  1. Download screen if it does not exist 
        ```$sudo apt-get install screen``` 

	2. Starting a new Screen.
	  ```$screen bash```
	3. Detached a terminal session.
	  CTRL + A  release, and then press D
	4. List all terminal session
	 ``` $ screen -list```
	5. Reconnect screen
	   ``` screen -r```
	
	6. If there are more screens: ```$ screen -r 1245.pts-0.raspberrypi ``` 
	  
	7. Terminate a screen by typing CTRL +D inside a screen.
	
* Create a new screen on your Raspberry pi 

   Run time_lapse.py in the first one. Your Rpi starts to capture images for the allotted time.
   
* Create a second screen and run upload.py

  Now your Rpi begins periodically uploading the images captured from the first script.
* Stop both the scripts once you've captured enough images and wait for all the images on your Rpi to finish uploading.
* Open a new Python3 notebook on Collab and run the "Movie_maker_v1.ipynb" script.
... This connects to your Google drive and converts the images into an mp4 file.

