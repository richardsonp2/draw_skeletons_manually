from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from PIL import ImageTk,Image
import numpy as np

root = Tk()
root.title("GUI Skeleton generator")



def browse_folder():
    folder = filedialog.askdirectory()
    print(folder)

# Create a frame
frame = ttk.Frame(root)
frame.grid(row=0, column=0)

btn = ttk.Button(frame, text="Browse for folder", command=browse_folder)
btn.grid(row=1, column=0)

quit_btn = ttk.Button(frame, text="Quit", command=root.quit)
quit_btn.grid(row=1, column=1)

image_viewer = Toplevel(root)
image_viewer.title("Image viewer")

skeleton_drawer = Toplevel(root)
skeleton_drawer.title("Skeleton drawer")
# Initialize a blank image with the same size as your input image
image = ImageTk.PhotoImage(Image.open("../image/im_M_PBS_4_8359_s8_Cell00005.png"))
skeleton_image = np.zeros_like(image)

# Choose your folder containing the images to skeltonise
ttk.Label(frame, text="Choose your folder containing the images to skeltonise").grid(row=0, column=0, columnspan=2)

canvas = Canvas(image_viewer, width = 800, height = 800)
canvas.grid()

canvas.create_image(20, 20, anchor=NW, image=image)

# Choose your output folder

root.mainloop()