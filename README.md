# Scopitone-python : Commande de video par GPIO
Bibliothèque basée sur VLC pour commander la lecture de videos grâce aux pins GPIO d'une Raspberry pi.

## Auteurs
- CREQUER Gwendal [gwendal.crequer\@gmail.com](mailto:gwendal.crequer@gmail.com)
- VANPOUCKE Tony [tony.vanpoucke@univ-rennes2.fr](mailto:tony.vanpoucke@univ-rennes2.fr)
  
## Description

Projet d'introduction à la programmation python et à l'utilisation de bibliothèques tierces. Le but est de créer une bibliothèque permettant de commander la lecture de vidéos grâce aux pins GPIO d'une Raspberry pi.

La bibliothèque utilisée est une API VLC, VLC est donc indispensable pour faire fonctionner la bibliothèque.

## Remarques générales
Une alternative à ces programmes pythons pourrait être l'OS [**VideoLooper**](https://videolooper.de/), qui permet de créer des boucles de vidéos à partir d'une clé USB.
Toutefois nous n'avons pas la main mise sur la configuration des différentes commandes.

Il est aussi possible d'utiliser une API d'un autre lecteur Video, comme [**omxplayer**](https://raspberry-projects.com/pi/software_utilities/media-players/omxplayer), ou de faire tourner la video dans un environnement tkinter.

## Sommaire
1. [Auteurs](#auteurs)
2. [Description](#description)
3. [Remarques générales](#remarques-générales)
4. [Sommaire](#sommaire)
5. [Structure du projet](#structure-du-projet)
6. [Fonctionnement](#fonctionnement)
7. [Bibliothèques utilisées](#bibliothèques-utilisées)
  

## Structure du projet
```python
📦
 ┣ 📂data #Contient les vidéos
 ┃ ┗ 🎬Différents fichiers .mp4
 ┃
 ┣ 📂libraries #Contient les modules python développés pour le projet
 ┃ ┣ 💻GPIO.py 
 ┃ ┗ 💻VideoManager.py
 ┃
 ┣ 📜Films.json #référence les films et leur emplacement
 ┃
 ┣ 💻main_GPIO.py
 ┣ 💻main_keyboard.py
 ┗ 💻main_pygame.py
 ┃
 ┣📜requirements.txt #Liste des bibliothèques nécessaires
 ┗📜README.md
```
## Fonctionnement
Pour installer les bibliothèques nécessaires, il suffit de lancer la commande suivante dans le terminal, à la *racine* du projet :
```bash
pip3 install -r requirements.txt
```
Il est possible de lancer différents programmes :

- **main_keyboard.py** : permet de gérer la lecture des vidéos en appuyant sur une touche du clavier (besoin d'éxecution en mode administrateur)
- **main_pygame.py** : permet ausside gérer la lecture des vidéos en appuyant sur une touche du clavier. Pygame est plus généralement utilisé pour gérer les évènements clavier, mais est de plus en plus instable voire inutilisable sur les dernières versions de python.
- **main_GPIO.py** : permet de gérer la lecture des vidéos en appuyant sur un bouton relié à une pin GPIO. Il est possible de gérer jusqu'à 4 boutons différents.
  
Pour lancer un programme, il suffit de lancer la commande suivante dans le terminal, à la *racine* du projet :
```bash
python3 main_[nom du programme].py
```

## Bibliothèques utilisées
- [**VLC**](https://www.videolan.org/vlc/index.fr.html) : lecteur vidéo libre et multiplateforme
- [**Pygame**](https://www.pygame.org/news) : bibliothèque python permettant de créer des jeux vidéo
- [**RPi.GPIO**](https://pypi.org/project/RPi.GPIO/) : bibliothèque python permettant de gérer les pins GPIO d'une Raspberry pi
- [**JSON**](https://docs.python.org/fr/3/library/json.html) : bibliothèque python permettant de gérer les fichiers JSON
- [**keyboard**](https://pypi.org/project/keyboard/) : bibliothèque python permettant de gérer les évènements clavier
- **GPIO** : bibliothèque permettant de gérer les pins GPIO d'une Raspberry pi, simplifiée pour le projet
- **VideoManager** : bibliothèque permettant de gérer la lecture des vidéos
  
