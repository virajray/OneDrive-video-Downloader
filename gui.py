import subprocess
from pathlib import Path
from tkinter import filedialog

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Define a function to select the save directory
def select_save_dir():
        save_dir = filedialog.askdirectory(title="Select Directory to Save your file ")
        return save_dir

directory=select_save_dir()

def Main():

    #setting input boxes values assigned to variables
    url = url_entry.get()

    filename = filename_entry.get()

    command = f'ffmpeg -i "{url}" -codec copy "{directory}/{filename}.mp4"'
    subprocess.run(command, shell=True)


window = Tk()

window.geometry("700x550")
window.configure(bg = "#2B2B2B")


canvas = Canvas(
    window,
    bg = "#2B2B2B",
    height = 550,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    353.0,
    301.0,
    image=entry_image_1
)
url_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
url_entry.place(
    x=158.0,
    y=280.0,
    width=390.0,
    height=40.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    353.0,
    395.0,
    image=entry_image_2
)
filename_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
filename_entry.place(
    x=158.0,
    y=374.0,
    width=390.0,
    height=40.0
)

canvas.create_text(
    155.0,
    25.0,
    anchor="nw",
    text="OneDrive Downloader",
    fill="#00A3FF",
    font=("Inter Bold", 32 * -1)
)

canvas.create_text(
    182.0,
    253.0,
    anchor="nw",
    text="Enter extracted link:",
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    182.0,
    347.0,
    anchor="nw",
    text="Enter file name:",
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=Main,
    relief="flat"
)
button_1.place(
    x=255.0,
    y=458.0,
    width=190.0,
    height=42.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    340.0,
    158.0,
    image=image_image_1
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=select_save_dir,
    relief="flat"
)
button_2.place(
    x=561.625,
    y=375.625,
    width=39.75,
    height=39.75
)
window.resizable(False, False)

#Set the icon of tkinter window
window.iconbitmap(r"assets\cloud.ico")

window.title("OneDrive video Downloader")

window.mainloop()
