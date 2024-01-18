# Import necessary modules and libraries
import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image

# Class definition for the NewsApp
class NewsApp:

    # Constructor for initializing the NewsApp
    def __init__(self):
        # Fetch news data from News API
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=07ce6431517e45c5b04b589c36e5bed6').json()
        # Initialize the GUI
        self.load_gui()
        # Load the first news item
        self.load_news_item(0)

    # Method to load the initial GUI
    def load_gui(self):
        # Create a Tkinter window
        self.root = Tk()
        # Set window dimensions and make it non-resizable
        self.root.geometry('350x600')
        self.root.resizable(0, 0)
        # Set window title and background color
        self.root.title('Mera News App')
        self.root.configure(background='black')

    # Method to clear the current content on the screen
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    # Method to load and display a news item
    def load_news_item(self, index):
        # Clear the screen for the new news item
        self.clear()

        # Load image for the news item
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)
        except:
            # Use a default image if the news item has no image
            img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)

        # Display the image on the GUI
        label = Label(self.root, image=photo)
        label.pack()

        # Display the heading of the news item
        heading = Label(self.root, text=self.data['articles'][index]['title'], bg='black', fg='white', wraplength=350,
                        justify='center')
        heading.pack(pady=(10, 20))
        heading.config(font=('verdana', 15))

        # Display details/description of the news item
        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white',
                        wraplength=350, justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        # Create a frame for navigation buttons
        frame = Frame(self.root, bg='black')
        frame.pack(expand=True, fill=BOTH)

        # Display 'Prev' button if not the first news item
        if index != 0:
            prev = Button(frame, text='Prev', width=16, height=3, command=lambda: self.load_news_item(index - 1))
            prev.pack(side=LEFT)

        # Display 'Read More' button
        read = Button(frame, text='Read More', width=16, height=3,
                      command=lambda: self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        # Display 'Next' button if not the last news item
        if index != len(self.data['articles']) - 1:
            next = Button(frame, text='Next', width=16, height=3, command=lambda: self.load_news_item(index + 1))
            next.pack(side=LEFT)

        # Run the Tkinter main loop
        self.root.mainloop()

    # Method to open the link in a web browser
    def open_link(self, url):
        webbrowser.open(url)

# Create an instance of the NewsApp class
obj = NewsApp()
