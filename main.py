import pygame
from random import randint, choice
import time

DIMENSION_ECRAN = (1200, 300)

pos_tortue = [5, 5, 5]
vitesseAleatoire = [randint(1, 5), randint(1, 3), randint(1, 8)]
hasardTortueAccelerer = None
acceleration = 0.3

partirCourse = False

pygame.init() 

pygame.display.set_caption("Course de tortue")
ecran = pygame.display.set_mode(DIMENSION_ECRAN)

piste_img = pygame.image.load("pisteDeCourse.jpg")
tortue_img = [pygame.image.load("tortue.png"), pygame.image.load("tortue.png"), pygame.image.load("tortue.png")]

print("Appuyez sur (p) pour commencer la course")

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                # Sélectionner aléatoirement une tortue à accélérer
                hasardTortueAccelerer = choice([0, 1, 2])
                # Si on appuie sur "p" la course est lancee
                if event.key == pygame.K_p:
                    partirCourse = True    

        ecran.blit(piste_img, (0, 0))
        ecran.blit(tortue_img[0], (pos_tortue[0], 45))
        ecran.blit(tortue_img[1], (pos_tortue[1], 105))
        ecran.blit(tortue_img[2], (pos_tortue[2], 165))

        if partirCourse == True:
            pos_tortue[0] += vitesseAleatoire[0]
            pos_tortue[1] += vitesseAleatoire[1]
            pos_tortue[2] += vitesseAleatoire[2]

        if hasardTortueAccelerer is not None:
            vitesseAleatoire[hasardTortueAccelerer] += acceleration

        if pos_tortue[0] >= DIMENSION_ECRAN[0] - 25  or pos_tortue[1] >= DIMENSION_ECRAN[0] - 25 or pos_tortue[2] >= DIMENSION_ECRAN[0] - 25:
            if pos_tortue[0] >= DIMENSION_ECRAN[0] - 25: 
                print("La tortue de la piste rouge a gagné!")
            elif pos_tortue[1] >= DIMENSION_ECRAN[0] - 25:   
                print("La tortue de las piste verte a gagné!")
            elif pos_tortue[2] >= DIMENSION_ECRAN[0] - 25:   
                print("La tortue de la piste bleue a gagné!")

            time.sleep(5)
            pygame.quit()
            quit()
            

        pygame.display.flip()

        pygame.time.Clock().tick(30)