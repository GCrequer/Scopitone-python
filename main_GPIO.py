from libraries.VideoManager import VideoManager
from libraries.GPIO import myGPIO


# Définir le chemin vers le fichier JSON contenant les informations sur les vidéos
json_file_path = 'Films.json'

# Créer un objet de la classe VideoManager
video_manager = VideoManager(json_file_path)

# Définir les broches GPIO sur lesquels sont branchés les boutons
play_pause_pin = 17
next_pin       = 27
prev_pin       = 22
mygpio = myGPIO(play_pause_pin, next_pin, prev_pin)


# Définir les fonctions de callback pour chaque bouton
mygpio.set_callbacks(video_manager)

# Boucle principale
while True:
    pass

# Reset les broches GPIO
mygpio.cleanup()
