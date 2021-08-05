import webbrowser
from tkinter import *
from readnumber import readNumber
from PIL import Image, ImageTk
from speak_text import speak

def clear():
    input_box.delete(1.0, END)
    output_box.delete(1.0, END)

def read():
    try:
        output_box.delete(1.0, END)
        INPUT = input_box.get(1.0, END)
        INPUT = INPUT.strip()
        INPUT = readNumber(INPUT)
        output_box.insert(1.0, INPUT)
    except:
        output_box.insert(1.0, "Vui lòng kiểm tra lại!")

def voice():
    try:
        INPUT = input_box.get(1.0, END)
        INPUT = INPUT.strip()
        INPUT = readNumber(INPUT)
        speak(INPUT)
    except:
        speak("Vui lòng kiểm tra lại!")

def openFB():
	url = "https://www.facebook.com/thanhanphan17"
	webbrowser.open_new_tab(url)

root = Tk()
root.title("Đọc số tiếng việt")
root.geometry("800x600")
root.resizable(height = False, width = False)

load = Image.open("img/background.jpg")
render = ImageTk.PhotoImage(load)
img = Label(root, image = render)
img.place(x = -2, y = -2)

name = Label(root, text="Read Vietnamese Number", fg = "#FFFFFF", bd = 0, bg = "#001020")
name.config(font = ("Transformers Movie", 30))
name.pack(pady = 20)

input_box = Text(root, width = 60, height = 4, font = ("ROBOTO", 16))
input_box.pack(pady = 15)
output_box = Text(root, width = 60, height = 10, font = ("ROBOTO", 16))
output_box.pack(pady = 80)

button_frame = Frame(root).pack(side = BOTTOM)

clear_button = Button(button_frame, text = "Clear", font = "Helvetica 16 bold", 
               bg = "#303030", fg = "#FFFFFF", command = clear)
clear_button.place(x = 350, y = 235)

write_button = Button(button_frame, text = "Bằng chữ", font = "Helvetica 16 bold", 
               bg = "#303030", fg = "#FFFFFF", command = read)
write_button.place(x = 150, y = 235)

read_button = Button(button_frame, text="Bằng lời", font = "Helvetica 16 bold", 
              bg = "#303030", fg = "#FFFFFF", command = voice)
read_button.place(x = 550, y = 235)

author_button = Button(button_frame, text = "Copyright: Phan Thanh An - facebook.com/thanhanphan17", 
                font = "Helvetica 13", bg = "#011837", fg = "#FFFFFF", command = openFB)
author_button.place(x = 160, y = 570)

root.mainloop()