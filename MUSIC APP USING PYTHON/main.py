#importing libraries 

import os
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
import pygame 
from pygame import mixer

class MusicPlayer:
    def __init__(self,root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("1000x200")
        pygame.init()
        pygame.mixer.init()
        self.track = StringVar()
        self.status = StringVar()

        # Creating the Track Frames for Song label & status label
        trackframe = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="purple",fg="white",bd=5,relief=GROOVE)
        trackframe.place(x=0,y=0,width=600,height=100)
    # Inserting Song Track Label
        songtrack = Label(trackframe,textvariable=self.track,width=20,font=("times new roman",24,"bold"),bg="yellow",fg="black").grid(row=0,column=0,padx=10,pady=5)
    # Inserting Status Label
        trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",24,"bold"),bg="pink",fg="gold").grid(row=0,column=1,padx=10,pady=5)

    # Creating Button Frame
        buttonframe = LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        buttonframe.place(x=0,y=100,width=600,height=100)
    # Inserting Play Button
        playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=10,height=1,font=("Arial Greek",16,"bold"),fg="white",bg="black").grid(row=0,column=0,padx=10,pady=5)
    # Inserting Pause Button
        playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,font=("times new roman",16,"bold"),fg="white",bg="black").grid(row=0,column=1,padx=10,pady=5)
    # Inserting Unpause Button
        playbtn = Button(buttonframe,text="UNPAUSE",command=self.unpausesong,width=10,height=1,font=("times new roman",16,"bold"),fg="white",bg="black").grid(row=0,column=2,padx=10,pady=5)
    # Inserting Stop Button
        playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=10,height=1,font=("times new roman",16,"bold"),fg="white",bg="black").grid(row=0,column=3,padx=10,pady=5)

    # Creating Playlist Frame
        songsframe = LabelFrame(self.root,text="Playlist",font=("times new roman",15,"bold"),bg="BLACK",fg="white",bd=5,relief=GROOVE)
        songsframe.place(x=600,y=0,width=400,height=200)
    # Inserting scrollbar
        scrol_y = Scrollbar(songsframe,orient=VERTICAL)
    # Inserting Playlist listbox
        self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
    # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
    # Changing Directory for fetching Songs
        os.chdir(r"C:\Users\sneha\OneDrive\Desktop\MUSIC APP USING PYTHON\SONGS")
    # Fetching Songs
        songtracks = os.listdir()
    # Inserting Songs into Playlist
        for track in songtracks:
            self.playlist.insert(END,track)


    

    def playsong(self):
        self.track.set(self.playlist.get(ACTIVE))
    # Displaying Status
        self.status.set(".........")
    # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
    # Playing Selected Song
        pygame.mixer.music.play()

    def stopsong(self):
    # Displaying Status
        self.status.set("|>")
    # Stopped Song
        pygame.mixer.music.stop()

    def pausesong(self):
    # Displaying Status
        self.status.set("||>")
    # Paused Song
        pygame.mixer.music.pause()

    def unpausesong(self):
        self.status.set("........")
    # Playing back Song
        pygame.mixer.music.unpause()

root = Tk()
MusicPlayer(root)
root.mainloop()