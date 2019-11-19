
'''
# download multiple videos

'''
# video_list = ["https://www.youtube.com/watch?v=UBnfm4s7CRA",
#             "https://www.youtube.com/watch?v=I8uqz-hQnZs", "https://www.youtube.com/watch?v=_lwn4uDGKfU"]
video_list = open(
    "c:\\Users\\anamarquez\\source\\Repass\\PythonA-Z-LearnPythonProgramming\\Project_VidieoDownloader\\sample.txt", "r")

for vds in video_list:
    yt = YouTube(vds)
    dw = yt.streams.get_by_itag(22)
    print(yt.streams.all())
    print("\n")
    dw.download(
        "c:\\Users\\anamarquez\\source\\Repass\\PythonA-Z-LearnPythonProgramming\\Project_VidieoDownloader\\")
