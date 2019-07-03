from youtube_dl import YoutubeDL

dl=YoutubeDL()
#download one video
dl.download(['https://www.youtube.com/watch?v=4Njp-J2s5uw'])
#download multiple videos
dl.download(['https://www.youtube.com/watch?v=12N0qEr_RGk','https://www.youtube.com/watch?v=kh-A6z7M0zc'])
#download audio
options = {
    'format': 'bestaudio/audio' 
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=Pkh8UtuejGw'])
#search and then download the first video
options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1 
}
dl = YoutubeDL(options)
dl.download(['Nếu anh đi mỹ tâm'])
#search and then download the first audio
options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Lạc trôi sơn tùng mtp'])