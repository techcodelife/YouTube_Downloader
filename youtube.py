import pytube
from tkinter import *

def download():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video   = youtube.streams.get_highest_resolution()
        video.download("C:/Users/asus/Desktop/videosD")
        notif.config(fg="green",text="Download complete")
    except Exception as e:
        print(e)
        notif.config(fg="red",text="Video could not be downloaded")

master = Tk()
master.title("YouTube Downloader")
master.configure(bg='black')


Label(master, text="YouTube Video Downloader", bg = "black", fg="red", font=("Roboto",30, "bold")).grid(sticky=N,padx=100,row=0) #title
Label(master, text="Enter the video link here:", bg = "black", fg="white", font=("Roboto",20)).grid(sticky=N,pady=30,row=1)    #subtitle


notif = Label(master,bg = "black", font=("Roboto",15)) #message that will show succesful or not
notif.grid(sticky=N,pady=1,row=4) 

#create the entry box
url = StringVar()
Entry(master, width=40, fg="grey",font=("Roboto",20), textvariable=url).grid(sticky=N,row=2)


#create the "Download" button
Button(master,width=20,text="Download",font=("Roboto",12), command = download).grid(sticky=N,row=3,pady=15)


master.mainloop()

