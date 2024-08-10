from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np
import cv2
import os  # Import the os module to handle directory operations

root = Tk()
root.title("GUI Skeleton Generator")
ico = Image.open('./icons/skeleton.jpg')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# Initialize global variables
skeleton_image = None
original_image = None
drawing = False
file_path = None  # Store the file path of the loaded image
save_directory = None  # Store the directory where skeletons will be saved
input_directory = None  # Store the directory where images are loaded
file_list = []  # List of image files in the input directory
current_file_index = 0  # Index to keep track of the current file

# Callback function to draw the skeleton
def draw_skeleton(event):
    global drawing, skeleton_image, original_image
    if drawing:
        x, y = event.x, event.y
        cv2.circle(skeleton_image, (x, y), 1, (255, 255, 255), -1)
        update_canvas()

def start_drawing(event):
    global drawing
    drawing = True

def stop_drawing(event):
    global drawing
    drawing = False

def update_canvas():
    global skeleton_image, original_image
    # Combine original image and skeleton
    combined_image = cv2.addWeighted(original_image, 0.7, skeleton_image, 0.3, 0)
    # Convert to RGB for Tkinter
    combined_image = cv2.cvtColor(combined_image, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(combined_image)
    img = ImageTk.PhotoImage(image=im)
    canvas.create_image(0, 0, anchor=NW, image=img)
    canvas.image = img

def choose_input_directory():
    global input_directory, file_list, current_file_index
    input_directory = filedialog.askdirectory()
    input_folder.config(text=input_directory)
    if input_directory:
        # List all image files in the directory
        file_list = [f for f in os.listdir(input_directory) if f.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp'))]
        file_list.sort()  # Sort the files alphabetically
        current_file_index = 0  # Reset to the first file
        load_next_image()

def load_next_image():
    global skeleton_image, original_image, file_path, current_file_index
    if current_file_index < len(file_list):
        file_path = os.path.join(input_directory, file_list[current_file_index])
        # Load the image using OpenCV
        original_image = cv2.imread(file_path)
        # Convert the image to grayscale
        original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        # Create a blank skeleton image
        skeleton_image = np.zeros_like(original_image)
        update_canvas()

def choose_save_directory():
    global save_directory
    save_directory = filedialog.askdirectory()
    saved_folder.config(text=save_directory)

def save_skeleton():
    global save_directory, current_file_index
    if skeleton_image is not None:
        if not save_directory:
            save_directory = filedialog.askdirectory()
            saved_folder.config(text=save_directory)
        if save_directory:
            # Get the original file name
            original_filename = os.path.basename(file_path)
            # Construct the full path to save the skeleton image
            save_path = os.path.join(save_directory, original_filename)
            # Save the skeleton image
            cv2.imwrite(save_path, skeleton_image)
            print(f"Skeleton saved to {save_path}")
            # Move to the next image
            current_file_index += 1
            if current_file_index < len(file_list):
                load_next_image()
            else:
                print("All images processed!")
                current_file_index = 0  # Reset index if needed

# Create the main frame
frame = ttk.Frame(root)
frame.grid(row=0, column=0)

# Label to show the input directory
input_label = ttk.Label(frame, text="Input directory:")
input_label.grid(row=0, column=0)

# Label to display the directory where the images are loaded
input_folder = ttk.Label(frame, text="No folder selected")
input_folder.grid(row=0, column=1)

# Label to show the save directory
save_label = ttk.Label(frame, text="Save skeletons to:")
save_label.grid(row=1, column=0)

# Label to display the directory where the skeletons are saved
saved_folder = ttk.Label(frame, text="No folder selected")
saved_folder.grid(row=1, column=1)

# Load image button
load_btn = ttk.Button(frame, text="Load Input Directory", command=choose_input_directory)
load_btn.grid(row=2, column=0)

# Choose save directory button
save_btn = ttk.Button(frame, text="Choose Save Directory", command=lambda: save_directory())
save_btn.grid(row=2, column=1)

# Save skeleton button
save_btn = ttk.Button(frame, text="Save Skeleton and Next", command=save_skeleton)
save_btn.grid(row=2, column=3)

# Quit button
quit_btn = ttk.Button(frame, text="Quit", command=root.quit)
quit_btn.grid(row=2, column=4)

# Canvas for image display
canvas = Canvas(root, width=800, height=800, bg="white")
canvas.grid(row=0, column=1)

# Bind mouse events to the canvas
canvas.bind("<ButtonPress-1>", start_drawing)
canvas.bind("<ButtonRelease-1>", stop_drawing)
canvas.bind("<B1-Motion>", draw_skeleton)

root.mainloop()
