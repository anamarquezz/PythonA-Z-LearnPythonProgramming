# pip install pytube

from pytube import YouTube

video_list = open(
    "c:\\Users\\anamarquez\\source\\Repass\\PythonA-Z-LearnPythonProgramming\\Project_VidieoDownloader\\sample.txt", "r")


for vds in video_list:
    yt = YouTube(vds)
    try:
        dw = yt.streams.get_by_itag(22)
        dw.download(
            "c:\\Users\\anamarquez\\source\\Repass\\PythonA-Z-LearnPythonProgramming\\Project_VidieoDownloader\\")
        print("\n Download", vds)
    except:
        print("Download Failed For", vds)
