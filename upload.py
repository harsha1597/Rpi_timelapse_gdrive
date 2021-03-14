import os,sched,time
print("Press ctrl+c to Exit")
while True:

	os.system("rclone move ~/Desktop/bird_time/ rpi_up:Bird")
	time.sleep(30)

