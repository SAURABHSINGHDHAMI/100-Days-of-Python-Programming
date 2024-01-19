# 📰 Inshort Clone

A simplified clone of the Inshorts app, this Python application fetches top headlines from a news API and displays them in a graphical user interface (GUI). Users can navigate through news items, read more about a particular news piece, and view corresponding images.

<p align="center">
  <img src="https://github.com/SAURABHSINGHDHAMI/100-Days-of-Python-Programming/blob/main/Python%20GUIs%20using%20Tkinter/Inshorts%20Clone/Test%20Image/Img%20-%201.jpg" />
</p>

## Features 🌟

- Fetches top news headlines from an API.
- Displays news title, description, and an image for each news item.
- Allows navigation through news items (Prev, Next).
- Opens the full news article in a web browser when "Read More" is clicked.

## Getting Started 🚀

1. Clone the repository.

2. Navigate to the project directory:
   ```bash
   cd Inshorts Clone
   ```

3. Run the application:
   ```bash
   python news.py
   ```

4. The GUI window will appear, displaying the top news headlines.

## GUI Layout 🖼️

The GUI layout consists of an image, news title, news description, and navigation buttons.

## API Usage 🚀

The application uses the [News API](https://newsapi.org/) to fetch top headlines. You need to replace the API key in the `requests.get` method with your own valid API key.

```python
self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=YOUR_API_KEY').json()
```

## Dependencies 🛠️

- Tkinter
- Pillow (PIL)
- Requests
