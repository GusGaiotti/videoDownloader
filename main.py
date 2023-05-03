from pytube import YouTube


yt = YouTube((input('Digite a URL do vídeo:')))

print('-------------')

data =''

while data == '':
    try:
        data = yt.streams
        data = yt.streams.filter(file_extension='mp4')

    except:
        print('Estamos fazendo o download, por favor aguarde...')
        print('-------------')

preffered_resolution = ['144p', '240p', '360p', '480p', '720p', '1080p']
best_resolution = []

for resolution in preffered_resolution:
    video_streams = yt.streams.filter(progressive=True, res=resolution)

    if len(video_streams) > 0:
        best_resolution.append(resolution)

stream = yt.streams.filter(res= str(best_resolution[-1]))
#Dowload configurado para na melhor qualidade possível com audio disponível

download_path = "C:\pythonProject\VideoDownloader"
path = stream.first().download(download_path, filename= yt.title + '.mp4')

print('Seu vídeo: "',yt.title,'" está em: ',path)
input("Aperte ENTER para encerrar")
print('-------------')
print('Download concluido.')