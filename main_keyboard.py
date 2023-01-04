from libraries.VideoManager import VideoManager
import keyboard

# Créer un objet de la classe VideoManager
video_manager = VideoManager('Films.json')

# Associer les fonctions aux touches
keyboard.add_hotkey('space', video_manager.play_pause)
keyboard.add_hotkey('Right', video_manager.next)
keyboard.add_hotkey('Left', video_manager.previous)
#keyboard.add_hotkey('flèche gauche', video_manager.previous)
keyboard.add_hotkey('Ctrl+q', video_manager.stop)

# Attendre l'appui sur une touche
keyboard.wait()
