# 🖼️ Wallpaper Viewer

A simple wallpaper viewer application that allows users to view a collection of wallpapers stored in the "wallpapers" directory. Users can navigate through the wallpapers using the "Next" button, and the application will display each image in the collection.

<p align="center">
  <img src="https://github.com/SAURABHSINGHDHAMI/100-Days-of-Python-Programming/blob/main/Python%20GUIs%20using%20Tkinter/Wallpaper%20Viewer/Test%20Image/Test%20Image.jpg" />
</p>

## Features 🌟

- Displays a collection of wallpapers stored in the "wallpapers" directory.
- Allows navigation through wallpapers using the "Next" button.
- Resizes images for a consistent display in the GUI.

## Getting Started 🚀

1. Clone the repository.

2. Navigate to the project directory:
   ```bash
   cd Wallpaper Viewer
   ```

3. Place your wallpaper images in the "wallpapers" directory.

4. Run the application:
   ```bash
   python wallpaper_viewer.py
   ```

5. The GUI window will appear, displaying the first wallpaper in the collection.

## GUI Layout 🖼️

The GUI layout includes an image label and a "Next" button for navigating through wallpapers.

## Application Logic 🧠

The application uses the `os` module to list files in the "wallpapers" directory and `PIL` (Pillow) to open and resize each image. The `rotate_image` function is called when the "Next" button is clicked, updating the displayed image.

```python
def rotate_image():
    global counter
    img_label.config(image = img_array[counter % len(img_array)])
    counter = counter + 1
```

## Dependencies 🛠️

- Tkinter
- Pillow (PIL)
