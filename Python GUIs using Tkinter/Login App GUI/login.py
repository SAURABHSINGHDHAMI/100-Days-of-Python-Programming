# Import necessary modules from tkinter and PIL
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

# Function to handle the login process
def handle_login():
    # Retrieve email and password from the input fields
    email = email_input.get()
    password = password_input.get()

    # Check if the entered credentials are correct
    if email == 'saurabh@gmail.com' and password == '1234':
        # Show a success message if login is successful
        messagebox.showinfo('Yayyy', 'Login Successful')
    else:
        # Show an error message if login fails
        messagebox.showerror('Error', 'Login Failed')

# Create the main window
root = Tk()

# Set window title and icon
root.title('Login Form')
root.iconbitmap('favicon.ico')

# Set window dimensions
root.geometry('350x500')

# Set window background color
root.configure(background='#0096DC')

# Open and resize the Flipkart logo
img = Image.open('flipkart-logo.png')
resized_img = img.resize((70, 70))
img = ImageTk.PhotoImage(resized_img)

# Create a label for the logo and pack it into the window
img_label = Label(root, image=img)
img_label.pack(pady=(10, 10))

# Create a label for the text "Flipkart" and pack it into the window
text_label = Label(root, text='Flipkart', fg='white', bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana', 24))

# Create a label for the email input field and pack it into the window
email_label = Label(root, text='Enter Email', fg='white', bg='#0096DC')
email_label.pack(pady=(20, 5))
email_label.config(font=('verdana', 12))

# Create an entry widget for email input and pack it into the window
email_input = Entry(root, width=50)
email_input.pack(ipady=6, pady=(1, 15))

# Create a label for the password input field and pack it into the window
password_label = Label(root, text='Enter Password', fg='white', bg='#0096DC')
password_label.pack(pady=(20, 5))
password_label.config(font=('verdana', 12))

# Create an entry widget for password input and pack it into the window
password_input = Entry(root, width=50)
password_input.pack(ipady=6, pady=(1, 15))

# Create a button for login and pack it into the window, associating it with the handle_login function
login_btn = Button(root, text='Login Here', bg='white', fg='black', width=20, height=2, command=handle_login)
login_btn.pack(pady=(10, 20))
login_btn.config(font=('verdana', 10))

# Start the Tkinter event loop
root.mainloop()
