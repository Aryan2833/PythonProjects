import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

# Create a tkinter window
window = tk.Tk()
window.title("YouTube Downloader")

# Define a function to download the video
def download_video():
    # Get the YouTube video URL from the user
    video_url = url_entry.get()

    # Create a YouTube object and get the highest resolution video
    yt = YouTube(video_url)
    video = yt.streams.get_highest_resolution()

    # Get the file path to save the video
    file_path = filedialog.asksaveasfilename(defaultextension=".mp4")

    # Download the video
    video.download(file_path)

    # Show a success message to the user
    result_label.config(text="Video downloaded successfully!")

# Create a label and an entry for the YouTube URL
url_label = tk.Label(window, text="Enter YouTube video URL:")
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()

# Create a button to download the video
download_button = tk.Button(window, text="Download", command=download_video)
download_button.pack()

# Create a label for the download result
result_label = tk.Label(window, text="")
result_label.pack()

# Run the tkinter event loop
window.mainloop()
