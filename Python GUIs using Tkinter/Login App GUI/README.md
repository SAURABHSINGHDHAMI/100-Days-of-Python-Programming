# 🔐 Login App GUI

A simple login application with a graphical user interface (GUI) built using Tkinter in Python. This application allows users to enter their email and password for login verification. If the provided credentials match the predefined values, a success message is displayed; otherwise, an error message is shown.

<p align="center">
  <img src="https://github.com/SAURABHSINGHDHAMI/100-Days-of-Python-Programming/blob/main/Python%20GUIs%20using%20Tkinter/Login%20App%20GUI/Test%20Image/Img%20-%201.jpg" />
</p>

## Features 🌟

- Simple and intuitive login interface.
- Verifies login credentials against predefined values.
- Displays success or error messages using Tkinter messagebox.

## Getting Started 🚀

1. Clone the repository.

2. Navigate to the project directory:
   ```bash
   cd Login App GUI
   ```

3. Run the application:
   ```bash
   python login_app.py
   ```

4. The GUI window will appear, prompting users to enter their email and password.

## GUI Layout 🖼️

The GUI layout consists of a logo, application title, input fields for email and password, and a login button.

## Application Logic 🧠

The application logic compares the entered email and password with predefined values. If the credentials match, a success message is displayed; otherwise, an error message is shown.

```python
if email == 'saurabh@gmail.com' and password == '1234':
    messagebox.showinfo('Yayyy', 'Login Successful')
else:
    messagebox.showerror('Error', 'Login Failed')
```

## Dependencies 🛠️

- Tkinter
- Pillow (PIL)
