import os
from folder_paths import movie_paths

def play_movie(command):
    movie=command.lower().strip()
    file=movie_paths.get(movie)
    
    if file:
        os.startfile(file)
        print("Playing movie")

    else:
        print("Error")    


play_movie("1")


