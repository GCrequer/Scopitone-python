import json
import vlc

class VideoManager:
    def __init__(self, json_file_path):
        # Charger les données du fichier JSON dans une variable movies
        with open(json_file_path, 'r') as f:
            data = json.load(f)
            self.movies = data['films']

        # Initialiser VLC et charger la première vidéo de la bibliothèque
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        # Connecter l'évenement "MediaPlayerEndReached" (fin de video) à la méthode pour changer de video "next"
        self.event_manager = self.player.event_manager()
        self.event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, self._end_reached)
        
        #self.player.set_fullscreen(True)

        self.current_index = 0    #premiere video ecrite dans le fichier
        self.load_movie(self.current_index)
        #self.play_pause()


    def load_movie(self, index):
        # Charger la vidéo à l'index spécifié dans la bibliothèque
        movie = self.movies[index]

        try :
            media = self.instance.media_new(movie['chemin'])
            self.player.set_media(media)
            print(f"Chargement de la vidéo {movie['titre']} ({movie['chemin']})")

        except Exception as e :
            print(f"Erreur {e} lors du chargement de la vidéo {movie['titre']} ({movie['chemin']})")
            self.stop()


    def play_pause(self):
        # Mettre en pause ou reprendre la vidéo en cours de lecture
        if self.player.is_playing():
            self.player.pause()
        else:
            self.player.play()
        

    def next(self):
        # Passer à la vidéo suivante dans la bibliothèque
        self.current_index = (self.current_index + 1) % len(self.movies)

        self.load_movie(self.current_index)
        self.play_pause()
    

    def _end_reached(self, event):

        print(f"Fin de la vidéo : {event}")

        
        self.event_manager = self.player.event_manager()
        self.event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, self._end_reached)
        self.next()


    def previous(self):
        # Retourner à la vidéo précédente dans la bibliothèque
        self.current_index = (self.current_index - 1) % len(self.movies)

        self.load_movie(self.current_index)
        self.play_pause()

    
    def stop(self):
        # Arrêter la lecture de la vidéo en cours et arrete le programme
        self.player.stop()
        self.player.set_media(None)
        print("Arrêt de la lecture")
        exit()
