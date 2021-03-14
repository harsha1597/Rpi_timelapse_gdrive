import os
inp_time = input('Enter length of time lapse in mins : ') 
inp_time=int(float(inp_time)*60*1000) #Convert to milliseconds 
frame_period=2*1000 #Take an image every 2 seconds
total_pics=len(str(int(inp_time//frame_period + 1))) #Number of digits needed when numbering the images 
file_name="~/Desktop/bird_time/image%0"+str(total_pics)+"d.jpg" 
command="raspistill -t "+str(inp_time)+" -tl "+str(frame_period)+" -o "+file_name
print(command)
os.system(command)
