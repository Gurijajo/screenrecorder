from tkinter import *
from PIL import Image, ImageTk
import pyscreenrec

root = Tk()
root.geometry("400x600")
root.title("Screen Recorder")
root.config(bg="#fff")
root.resizable(False, False)

def start_rec():
    file = Filename.get()
    rec.start_recording(str(file + ".mp4"), 15)

def pause_rec():
    rec.pause_recording()

def resume_rec():
    rec.resume_recording()

def stop_rec():
    rec.stop_recording()

rec = pyscreenrec.ScreenRecorder()


image_icon = Image.open("video.png")
image_icon = ImageTk.PhotoImage(image_icon)
root.iconphoto(False, image_icon)

lbl = Label(root, text="Screen Recorder", bg="#fff", font="arial 15 bold")
lbl.pack(pady=20)

image3 = Image.open("camera.png")
image3 = ImageTk.PhotoImage(image3)
Label(root, image=image3, bg="#fff", bd=0).pack(pady=30)

Filename = StringVar()
entry = Entry(root, textvariable=Filename, width=20, font="arial 15")
entry.place(x=60, y=350)
Filename.set("Recording N1")

start = Button(root, text="Start", font="arial 22", bg="#fff", command=start_rec)
start.place(x=140, y=250)

image4 = Image.open("pause-button-svgrepo-com.svg.png")
image4 = ImageTk.PhotoImage(image4)
pause = Button(root, image=image4, bg="#fff", command=pause_rec)
pause.place(x=60, y=450)

image5 = Image.open("resume-svgrepo-com.svg.png")
image5 = ImageTk.PhotoImage(image5)
resume = Button(root, image=image5, bg="#fff", command=resume_rec)
resume.place(x=160, y=450)

image6 = Image.open("stop-circle-svgrepo-com.svg.png")
image6 = ImageTk.PhotoImage(image6)
stop = Button(root, image=image6, bg="#fff", command=stop_rec)
stop.place(x=260, y=450)

root.mainloop()
