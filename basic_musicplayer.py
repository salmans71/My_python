from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog

current_volume = float(0.5)


def play_song():
    filename = filedialog.askopenfilename(initialdir="c:/", title="Please select a song")
    current_song = filename
    song_title = filename.split("/")
    song_title = song_title[-1]

    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg="green", text="now playing : " + str(song_title))
        volume_label.config(fg="green", text="volume : " + str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="error playing track")


def reduce_volume():
    try:
        global current_volume
        if current_volume <= 0:
            volume_label.config(fg="red", text="volume : muted")
            return
        current_volume = current_volume - float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text="volume : " + str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="track hasn't been selected")


def increase_volume():
    try:
        global current_volume
        if current_volume >= 2:
            volume_label.config(fg="green", text="volume : max")
            return
        current_volume = current_volume + float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text="volume : " + str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="track hasn't been selected")


def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="track not selected")


def resume():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="track not selected")


master = Tk()
master.title("Music Player")
Label(master, text="Custom Music Player", font=("Calibri", 15), fg="red").grid(sticky="N", row=0, padx=120)
Label(master, text="please select the music track u like", font=("Calibri", 12), fg="blue").grid(sticky="N", row=1)
Label(master, text="volume", font=("Calibri", 15), fg="red").grid(sticky="N", row=4)
song_title_label = Label(master, font=("Calibri", 12))
song_title_label.grid(sticky="N", row=3)
volume_label = Label(master, font=("Calibri", 12))
volume_label.grid(sticky="N", row=5)
Button(master, text="select song", font=("Calibri", 12), command=play_song).grid(row=2, sticky="N")
Button(master, text="pause", font=("Calibri", 12), command=pause).grid(row=3, sticky="E")
Button(master, text="resume", font=("Calibri", 12), command=resume).grid(row=3, sticky="W")
Button(master, text="-", font=("Calibri", 12), width=5, command=reduce_volume).grid(row=5, sticky="W")
Button(master, text="+", font=("Calibri", 12), width=5, command=increase_volume).grid(row=5, sticky="E")
master.mainloop()
