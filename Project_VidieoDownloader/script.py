# pip install pytube

from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=_1fuQco3Tes")
print(yt.streams.all())
print("\n")
dw = yt.streams.get_by_itag(22)
dw.download(
    "c:\\Users\\anamarquez\\source\\Repass\\PythonA-Z-LearnPythonProgramming\\Project_VidieoDownloader\\")
