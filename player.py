
from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title(' Music Player')
root.iconbitmap('images/music.ico')
root.geometry("500x400")
# Intiialize Mixer
pygame.mixer.init()

#Add Song Function
def add_song():
   song = filedialog.askopenfile(initialdir='audiofiles/' , title="Choose A Song" , filetypes=(("mp3 Files", "*.mp3"),))
#    song = song.name.replace("C:/" ,"")
   
   song_box.insert(END, song.name)
    #play song
def play():
        song = song_box.get(ACTIVE)
        #song = f'audiofiles'
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

#create Playlist box

song_box = Listbox(root, bg="black",fg="blue", width=60,selectbackground="grey",selectforeground="black")

song_box.pack(pady=20)

# Player Button Control images
back_btn_img = PhotoImage(file="images/skipb.png")
forward_btn_img = PhotoImage(file="images/skipf.png")
pause_btn_img = PhotoImage(file="images/pause.png")
stop_btn_img = PhotoImage(file="images/stop.png")
play_btn_img = PhotoImage(file="images/play.png")

## Create Player Control Frames

controls_frame = Frame(root)
controls_frame.pack()

# create Player Control Buttons
back_button = Button(controls_frame, image=back_btn_img, borderwidth=0)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0)
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0)

back_button.grid(row=0,column=0,padx=10)
forward_button.grid(row=0,column=1,padx=10)
play_button.grid(row=0,column=2,padx=10)
pause_button.grid(row=0,column=3,padx=10)
stop_button.grid(row=0,column=4,padx=10)

# Create Menu

my_menu = Menu(root)
root.config(menu=my_menu)

# Add Song Menu

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song to Playlist", command= add_song)




root.mainloop()








