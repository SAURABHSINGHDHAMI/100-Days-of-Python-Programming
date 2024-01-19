# 🚂 IRCTC Clone

This project is an implementation of an IRCTC clone using object-oriented programming (OOP) concepts in Python.

## 🌐 Overview

The `app.py` file serves as the main entry point for the IRCTC Clone application. It showcases the following OOP concepts:

### 🧬 Inheritance
The concept of inheritance is employed to create a base `IRCTC` class with common functionality. This class is then inherited to create more specific subclasses, promoting code reuse.

### 🔀 Polymorphism
Polymorphism is demonstrated through the use of different methods (`train_schedule`, `fetch_data`) within the `IRCTC` class, allowing flexibility in handling different types of tasks.

### 🎨 Abstraction
Abstraction is achieved by encapsulating the details of the implementation within the `IRCTC` class. Users interact with a simplified interface provided by the class without needing to understand the internal complexities.

### 📦 Encapsulation
Encapsulation is applied by bundling the data (train details, API response) and methods that operate on the data within the `IRCTC` class. This helps in organizing and securing the code.

## 🚀 Usage

1. Clone the repository.

2. Navigate to the project directory:
   ```bash
   cd IRCTC Clone
   ```
   
3. Install the required packages by running the following command in your terminal:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
   ```bash
   python app.py
   ```
Follow the on-screen instructions to interact with the IRCTC clone. Choose an option to check live train status, PNR, or train schedule.

## 🛠 Dependencies

- requests==2.28.1

This library is used for making HTTP requests to fetch train schedule data.
