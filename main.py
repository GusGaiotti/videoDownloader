from pytube import YouTube
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-url", "--url", help="Video link", required=True)
parser.add_argument("-start", "--start_time", type=int, help="Start time (in seconds)")
parser.add_argument("-end", "--end_time", type=int, help="End time (in seconds)")
args = parser.parse_args()

if args.url is None:
    print("Need to insert a value for --output")
else:
    if args.start_time is not None and args.end_time is not None:
        yt = YouTube(args.url)
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

        path = stream.first().download(filename= yt.title + '.mp4')

        print('Seu vídeo: "',yt.title,'" está em: ',path)
        input("Aperte ENTER para encerrar")
        print('-------------')
        print('Download concluido.')