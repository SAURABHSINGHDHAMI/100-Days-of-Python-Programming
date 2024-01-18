from tkinter import *
from PIL import ImageTk, Image
import os

# Function to rotate the displayed image
def rotate_image():
    global counter
    # Update the image displayed on the label with the next one in the img_array
    img_label.config(image = img_array[counter % len(img_array)])
    counter = counter + 1

# Initialize a counter for tracking the current image
counter = 1

# Create the main Tkinter window
root = Tk()
root.title('Wallpaper Viewer')

# Set the window size
root.geometry('250x400')

# Set the background color
root.configure(background = 'black')

# Get the list of files in the 'wallpapers' directory
files = os.listdir('wallpapers')

# Initialize an array to store PhotoImage objects for each image in the directory
img_array = []

# Loop through each file in the 'wallpapers' directory
for file in files:
    # Open the image file using PIL
    img = Image.open(os.path.join('wallpapers', file))
    
    # Resize the image to fit the window
    resized_img = img.resize((200, 300))
    
    # Convert the resized image to a PhotoImage object and append it to the img_array
    img_array.append(ImageTk.PhotoImage(resized_img))

# Create a label to display the initial image
img_label = Label(root, image=img_array[0])
img_label.pack(pady=(15, 10))

# Create a button to switch to the next image
next_btn = Button(root, text = 'Next', bg = 'white', fg = 'black', width = 28, height = 2, command = rotate_image)
next_btn.pack()

# Start the Tkinter main loop
root.mainloop()
