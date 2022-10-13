from youtubesearchpython import VideosSearch,Search
# from __future__ import unicode_literals
import youtube_dl
import os

#where to save
SAVE_PATH = "videos_dowloadeds/"
Search_Text = 'videos detecção'
video_qtd = 2
video_links = []

for vid in range(0,video_qtd,1):

    # videosSearch = VideosSearch('arrombamento de caixa', limit = video_qtd)
    try:
        videosSearch = Search(Search_Text, limit = video_qtd)
        video_links.append(videosSearch.result()['result'][vid]['link'])

        print(videosSearch.result()['result'][vid]['link'])
    except:
        break

#link of the video to be downloaded

videoArray = len(video_links)
count = 1
ydl_opts = {}
os.chdir('videos_dowloadeds/')
for videoLink in video_links:
    print('vídeo {}/{}'.format(count,videoArray))
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([videoLink])
    count +=1