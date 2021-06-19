#will take pictures every few minutes (desired time)

import dropbox
import time
import random

start_time= time.time() #returns current time

import cv2

def take_snapshot():
    number= random.randint(0,100) #finding number from 0-100 to have different name of images
    videoCapture_object= cv2.VideoCapture(0) #creates a video recorder object
    result= True

    while(result): #loop unless it becomes false it would runt he loop
        ret, frame= videoCapture_object.read() # ret- dummy variable returns boolean value to tell if something is being returned or not. Like True or false.
        print(ret)
        img_name= "img"+str(number)+".png" #setting different names for the images
        cv2.imwrite(img_name, frame)#name will be different for every image #the image will be saved in frame. imswrite will store img in storage as name NewPicture.jpg
        start_time= time.time #return the current time
        result= False #AS WE HV CAPTURED THE IMG NOW THE RESULT IS FALSE TO BREAK OUT OF LOOP
        videoCapture_object.release() #closes camera with release function
    
    return img_name
    print("Snapshot Taken...")
    videoCapture_object.release() #close camera
    cv2.destroyAllWindows() #close all windows by camera

def upload_file(img_name): #parameter is img_name
    acess_token= "sl.AzD5KYZPAOTP51fAxRadItZR41YpsC3Ahrm6ZZqYrWmHlBH8lS7oIT-gnPmIn1U0cJ0xSYsbnNJqLTPC40BAqmo8083icnAKl0tftEjTpTDuxpNFepJSqQvIkAunhLqEFQzdlflwp1Q"
    file= img_name
    file_from= file #file_from is the file or img
    file_to= "/Security12/"+(img_name)
    dbx= dropbox.Dropbox(acess_token) #uploading file

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode= dropbox.files.WriteMode.overwrite)
        print("file has been uploaded..")

def main():
    while(True):
        if((time.time() - start_time)>=5): #current time- start_time (when picture was taken) if it > then 5 seconds then take snapshot
            name= take_snapshot()
            upload_file(name) #uploads file

main()
