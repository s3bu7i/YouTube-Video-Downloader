
import string
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from cv2 import dft
from pytube import YouTube

def createwidgits():
    
    link_label = Label(root, text ='Paste URL\Link: ', bg="#999999")
    
    link_label.grid(row=1, column=0, pady=10, padx=10)

    
    root.link_text = Entry(root, width=60 , textvariable=video_link)
    
    root.link_text.grid(row=1, column=1,pady=10, padx=10)

    
    destination_label = Label(root, text ='Destination: ', bg="#999999")
    
    destination_label.grid(row=2, column=0, pady=10, padx=10)

    
    root.destination_label = Entry(root, width=60 , textvariable=Download_path)
    
    root.destination_label.grid(row=2, column=1,pady=10, padx=10)

    
    browse_but = Button(root, text="Browse", command=browse, width=10, bg="#FFD700")
    
    browse_but.grid(row=2, column=2, pady=10, padx=10)

    
    download_but = Button(root, text="Download", command=download_video, width=15, bg="#3333FF")
  
    download_but.grid(row=3, column=1, pady=3, padx=3)


def browse():
    
    downlaod_dir = filedialog.askdirectory(initialdir="Downlaod path")
    Download_path.set(downlaod_dir)


def download_video():

    url = video_link.get()
    folder = Download_path.get()
    get_video = YouTube(url)
    get_stream = get_video.streams.get_highest_resolution()
    get_stream.download(folder)
    


    messagebox.showinfo("Your video downloaded successfully")


root = tk.Tk()


root.geometry("600x180")
root.resizable(False,False)

root.title("downloader")

#background = PhotoImage(file = "C:\\code\\Python\\projects\\ytb_pyt.jpg")
#lable = Label(root, image=background)

root.config(background="#FF0000")

video_link = StringVar()
Download_path = StringVar()

createwidgits()

root.mainloop()






