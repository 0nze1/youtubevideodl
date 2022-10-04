import PySimpleGUI as sg
from pytube import YouTube
from pytube import Playlist
import os

def executar_download(link, path):
    video = YouTube(link)
    video.streams.get_highest_resolution().download(output_path=path)

def executar_download_mp3(link, path):
    video2 = YouTube(link)
    video2.streams.get_audio_only().download(output_path=path)
    

    
def executar_download_mp3_playlist(link, path):
   playlist = Playlist(link)
   for playlist in playlist.videos:
    playlist.streams.get_audio_only().download(output_path=path)
    

sg.theme('Topanga')

layout = [

    [sg.Titlebar("Video Downloader by Jonas")],

    [sg.Text('Informe o link do vídeo/playlist:'), sg.InputText()],

    [sg.Text('Informe a pasta de destino: '),sg.InputText(),sg.FolderBrowse(),],

    [sg.Button('Baixar'),sg.Button('MP3'),sg.Button('Playlist'),sg.Button('Cancelar'),]
]

janela = sg.Window("Video Downloader by Jonas", layout)

while True:
    event,values =  janela.read()
    if event == 'Cancelar' or event == sg.WINDOW_CLOSED:
        break

    elif event == 'Baixar':
        executar_download(values[0], values[1])
        sg.popup_ok("Download Concluído!")

    if event == 'MP3':
         executar_download_mp3(values[0], values[1])
         sg.Print()

    if event == 'Playlist':
         executar_download_mp3_playlist(values[0], values[1])
         sg.popup_ok("Download da playlist concluída!")

janela.close()