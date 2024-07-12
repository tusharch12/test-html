from pytube import YouTube
# YouTube('https://youtu.be/PcXWRsdVmh8?si=HEUPCIMJBxJJSwEA').streams.first().download()
yt = YouTube('https://youtu.be/yDLFj-grBnQ?si=jTozv1iegB3U7C-X')
thumbnail_url=yt.thumbnail_url
videoes = yt.streams.filter(subtype = 'mp4').order_by('resolution').desc()
List =[]
for stream in videoes:
    List.append({'itag': stream.itag, 'resolution': stream.resolution, 'mime_type': stream.mime_type})

print(List)
# Listen =[{'itag': stream.itag, 'resolution': stream.resolution, 'mime_type': stream.mime_type}
# for stream in yt.streams.filter(progressive=True, file_extension='mp4')]
# print(Listen)
# videos = yt.streams.filter(progressive=True, file_extension='mp4',).order_by('resolution')[-1]
# print(thumbnail_url)
# for video in videoes:
#     print(video.resolution)
