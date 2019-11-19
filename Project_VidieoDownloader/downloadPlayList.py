# pip install pytube

# Download a playlist
import pytube

pytube.Playlist(
    "https://www.youtube.com/watch?v=9p0gq4x7HHw&list=PLCbA22__6_bNJJXfWZJ1yQQiMYENzwjeY").download_all("c:\\Users\\anamarquez\\source\\Repass\\PythonA-Z-LearnPythonProgramming\\Project_VidieoDownloader\\")
