from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import vlc
import os
import time

class Odtwarzacz(Frame, object):

    def __init__(self, master):
        super(Odtwarzacz, self).__init__(master)
        self.master = master
        self.master.geometry("423x200")
        self.master.title("Spotify 2.0")
        self.large_font = ('Verdana', 15)
        self.screen_font = ('Verdana', 40)
        self.is_playing = False
        self.path = []
        self.przycisk()


    def przycisk(self):
        button1 = Button(self.master, text = "odtwarzaj", command = self.play_song)
        button1.place(x = 40, y = 170)
        button2 = Button(self.master, text = "start/stop", command = self.stop_song)
        button2.place(x = 120, y = 170)
        button3 = Button(self.master, text = "otwórz folder", command = self.open_file)
        button3.place(x = 200, y = 170)
        button4 = Button(self.master, text = "otwórz plik", command = self.open_song)
        button4.place(x = 300, y = 170)
        self.song_box = Listbox(self.master, bg = "black", fg =  "white", width = 70)
        self.song_box.place(x = 0, y = 0)

    def open_song(self):
        file_path = tkinter.filedialog.askopenfilename(title = "wybierz plik", filetypes = (("wav files", "*.wav"), ("mp3 files", "*.mp3")))
        self.path.append(file_path)
        print(file_path)
        filename = os.path.basename(file_path)
        #print(filename)
        self.song_box.insert(END, str(filename))

    def open_file(self):
        playlist = tkinter.filedialog.askdirectory()
        print(playlist)
        if len(playlist) > 0:
            for i in os.listdir(playlist):
                if i.__contains__(".mp3") or i.__contains__(".wav"):
                    self.path.append(str(playlist + "/" + i))
                    print(self.path)
                    self.song_box.insert(END, i)

    def stop_song(self):
        if self.is_playing == True:
            self.is_playing == False
            self.player.pause()

    def play_song(self):
        if self.is_playing == False:
            for i in self.path:
                self.player = vlc.MediaPlayer(i)
                self.player.play()
                break
        self.is_playing = True



screen = Tk()
app = Odtwarzacz(screen)
screen.mainloop()
