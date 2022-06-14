from pytube import YouTube

DOWNLOAD_FOLDER = "C:\\Users\\dothe\\Documents\\카카오톡 받은 파일"

url = "https://www.youtube.com/watch?v=N3IwV4quNXg&list=PPSV"

yt = YouTube(url)

stream = yt.streams.get_highest_resolution()

stream.download(DOWNLOAD_FOLDER)
