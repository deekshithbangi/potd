from pytube import YouTube

url = 'https://youtu.be/qfyynHBFOsM?si=C3vRUcsjx2X9C3ek'
yt_video = YouTube(url)
# this method will download the highest resolution that video is available
yt_video = yt_video.streams.get_highest_resolution()
yt_video.download()

print('your video is downloaded successfully'