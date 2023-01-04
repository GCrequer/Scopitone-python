import pygame
from pygame.locals import *
from libraries.VideoManager import VideoManager

# Définir le chemin vers le fichier JSON contenant les informations sur les vidéos

json_file_path = 'Films.json'

# Initialiser pygame
pygame.init()

# Créer un objet de la classe VideoManager
#video_manager = VideoManager(json_file_path)

# Boucle principale
while True:
    # Récupérer les événements de pygame
    for event in pygame.event.get():
        # Si l'utilisateur quitte, arrêter le programme
        if event.type == pygame.QUIT:
            #video_manager.stop()
            pygame.quit()
        
        # Si l'utilisateur appuie sur une touche
        if event.type == pygame.KEYDOWN:
            print(f"Appui sur la touche {event.key}")
            # Si l'utilisateur appuie sur la touche "espace", mettre en pause ou reprendre la vidéo
            if event.key == pygame.K_SPACE:
                #video_manager.play_pause()
                print("espace")
            # Si l'utilisateur appuie sur la touche "flèche droite", passer à la vidéo suivante
            elif event.key == pygame.K_RIGHT:
                #video_manager.next()
                print("droite")
            # Si l'utilisateur appuie sur la touche "flèche gauche", retourner à la vidéo précédente
            elif event.key == pygame.K_LEFT:
                #video_manager.previous()
                print("gauche")
            # Si l'utilisateur appuie sur la touche "échap", arrêter la vidéo
            elif event.key == pygame.K_ESCAPE:
                #video_manager.stop()
                print("échap")
