from pytubefix import *
import os

urlPlaylist = input("Ingrese la URL de la playlist que desea descargar: ")
pl = Playlist(urlPlaylist)

print("\nSe ingreso esta playlist: ")
print(pl.title)
print("\n")
errores = []
i = 0    
for v in pl.videos:
    i=i+1
    try:
        descarga = v.streams.filter(only_audio=True).first()           
        print(str(i) + ". Descargando: " + v.title + "\n -Tamaño: " + str(descarga.filesize_mb) + "Mb\n")
        descarga.download(filename_prefix=str(i) + ".",output_path="Audios descargados")
    except:
        errores.append((v,i))
        print("ERROR: " + v.title + " no disponible\nPasando al siguiente..\n")

print("\n\nVideos no descargados:\n\n")


for x in errores:
        print("No se descargo " + str(x[1]) + ". " + x[0].title + "\n\n")

path="./Audios descargados"
for archivo in os.listdir(path):
    os.rename(os.path.join(path, archivo), os.path.join(path,archivo.replace(".mp4", ".mp3")))

input("Listo\nPresione Enter para cerrar el programa\n")



