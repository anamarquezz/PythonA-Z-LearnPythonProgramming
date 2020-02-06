
'''
# download multiple videos

'''

from pytube import YouTube
# video_list = ["https://www.youtube.com/watch?v=UBnfm4s7CRA",
#             "https://www.youtube.com/watch?v=I8uqz-hQnZs", "https://www.youtube.com/watch?v=_lwn4uDGKfU"]
video_list = open(
    "c:\\Users\\anamarquez\\source\\Repass\\PythonA-Z-LearnPythonProgramming\\Project_VidieoDownloader\\sample.txt", "r")

for vds in video_list:   
    YouTube(vds).streams.first().download(
        "c:\\Users\\anamarquez\\source\\Repass\\PythonA-Z-LearnPythonProgramming\\Project_VidieoDownloader\\")
