from pytube import *
import os

urlPlaylist = input("Ingrese la URL de la playlist que desea descargar: ")
pl = Playlist(urlPlaylist)

print("\nSe ingreso esta playlist: ")
print(pl.title)
print("\n")

i = 0    
for v in pl.videos:
    i=i+1
    descarga = v.streams.filter(only_audio=True).first()  
    print(str(i) + ". Descargando: " + v.title + "\n -Tamaño: " + str(descarga.filesize_mb) + "Mb\n")
    descarga.download(filename_prefix=str(i) + ".",output_path="Audios descargados")

path="./Audios descargados"
for archivo in os.listdir(path):
    os.rename(os.path.join(path, archivo), os.path.join(path,archivo.replace(".mp4", ".mp3")))

input("Listo\nPresione Enter para cerrar el programa\n")



