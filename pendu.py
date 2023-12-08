import pygame
import random
import sys
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height ))
white = (255, 255, 255)
black = (0, 0, 0)
with open("mots.txt", "r") as fichier:
    mots = fichier.readlines()
def choose_word():
    return random.choice(mots).strip()
def afficher_mot_cache(mot, lettres_trouvees):
    mot_cache = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cache += lettre
        else:
            mot_cache += "_ "
    return mot_cache
def dessiner_pendu(erreurs):
    pendu_images = [
        pygame.image.load("image/1.png"),
        pygame.image.load("image/2.png"),
        pygame.image.load("image/3.png"),
        pygame.image.load("image/4.png"),
        pygame.image.load("image/5.png"),
        pygame.image.load("image/6.png"),
        pygame.image.load("image/7.png"),
    ]
    return pendu_images[erreurs]
def pendu():
    mot_a_deviner = choose_wordss()
    lettres_trouvees = []
    erreurs = 0
    tentatives_max = 6
    police = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    proposition = chr(event.key).lower()
                    if proposition in lettres_trouvees:
                        print("Vous avez déjà proposé cette lettre.")
                    elif proposition in mot_a_deviner:
                        print("Bonne proposition !")
                        lettres_trouvees.append(proposition)
                    else:
                        print("Mauvaise proposition.")
                        erreurs += 1
        screen.fill(white)
        mot_affiche = afficher_mot_cache(mot_a_deviner, lettres_trouvees)
        mot_texte = police.render(mot_affiche, True, black)
        screen.blit(mot_texte, (20, 20))
        pendu_image = dessiner_pendu(erreurs)
        screen.blit(pendu_image, (400, 20))
        pygame.display.flip()
        clock.tick(60)
if __name__ == "__main__":
    pendu()
