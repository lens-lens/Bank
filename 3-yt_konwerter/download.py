from pytube import YouTube

def Download(link):
    yt_object = YouTube(link)
    yt_object = yt_object.streams.get_highest_resolution()

    try:
        yt_object.download()
    except:
        print('An error has occured')
    print('Download is completed succesfully')

link = input('Enter the YouTube video URL: ')

go = Download(link)
    # return go(f, seed, [])
