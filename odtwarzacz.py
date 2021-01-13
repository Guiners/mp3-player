from tkinter import *
screen = Tk()

class Odtwarzacz(Frame, object):

    def __init__(self, master):
        super(Odtwarzacz, self).__init__(master)
        self.x = 420
        self.y = 240
        self.master.geometry("400x200")
        self.master.resizable(0, 0)
        self.master.title("Spotify 2.0")
        self.large_font = ('Verdana', 15)
        self.screen_font = ('Verdana', 40)
        self.is_playing = False



    def przycisk(self):
        self.button1 = Button(self, text = "odtwarzaj")
        self.button1['command'] = lambda: self.add_song()
        self.button1.place(x = 40, y = 170)

        self.button2 = Button(self, text = "zatrzymaj")
        self.button2.place(x = 120, y = 170)

        self.button3 = Button(self, text = "otwórz folder")
        self.button3.place(x = 200, y = 170)

        self.button4 = Button(self, text = "otwórz plik")
        self.button4.place(x = 300, y = 170)

        self.song_box = Listbox(
            self, bg="black", fg=  "white", width = 180, selectbackground = "yellow")
        self.song_box.pack(pady = 10)

    def add_song(self):
        pass

"""
        self.my_menu = Menu(self.master)
        self.master.config(menu = self.my_menu)

        self.add_song = Menu(self.my_menu)
        self.my_menu.add_cascade(label="add song", menu = self.add_song)
        self.add_song.add_command(label = "add one song", command = self.add_song)
"""

app = Odtwarzacz(screen)
Odtwarzacz.przycisk(screen)
screen.mainloop()
