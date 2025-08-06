from tkinter import *
import tkinter as tk
import json
from tkinter import filedialog
from PIL import Image, ImageTk

window = Tk()
window.geometry("800x800")
window.resizable(0, 0)
window.title("Agenda")

FILE_NAME = "agenda.json"

def add_item():
    input_text = entry_widget.get()
    if input_text:
        listBox.insert(END, input_text)
        entry_widget.delete(0, END)

def remove_item():
    selected = listBox.curselection()
    if selected:
        listBox.delete(selected[0])

def save_list():
    items = listBox.get(0, END)
    with open(FILE_NAME, 'w') as file:
        json.dump(items, file)

def load_file():
    file_path = filedialog.askopenfilename(
        title="Select File",
        filetypes=[("JSON Files", "*.json")]
    )
    if file_path:
        try:
            with open(file_path, 'r') as file:
                items = json.load(file)
                listBox.delete(0, END)
                for item in items:
                    listBox.insert(END, item)
        except Exception as e:
            print("Error loading file:", e)

#Blank image to help resize buttons
blank_image = tk.PhotoImage(width=100, height=40)

#IU Logo image and Label
Iu_image = Image.open("IU.png").resize((200, 100))
IU_image = ImageTk.PhotoImage(Iu_image)
IU_Label = Label(window, image=IU_image)
IU_Label.place(x=320, y=30)

entry_widget = Entry(window)
entry_widget.place(x=360, y=150)
entry_widget.focus()

add_button = tk.Button(window, text="Add Item", command=add_item, image=blank_image, compound=CENTER)
window.bind("<Return>", lambda event: add_item())
add_button.place(x=80, y=220)

delete_button = tk.Button(window, text="Delete Item", command=remove_item, image=blank_image, compound=CENTER)
delete_button.place(x=630, y=220)

save_button = tk.Button(window, text="Save List", command=save_list, image=blank_image, compound=CENTER)
save_button.place(x=450, y=220)

load_button = tk.Button(window, text="Load List", command=load_file, image=blank_image, compound=CENTER)
load_button.place(x=260, y=220)

listBox = tk.Listbox(window, height=30, width=90)
listBox.pack(side=BOTTOM, pady=20)

window.mainloop()