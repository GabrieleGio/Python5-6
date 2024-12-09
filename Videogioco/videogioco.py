import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("La Bottega Italiana")


WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 32)


sfondo = pygame.image.load("bottega.png")
sfondo = pygame.transform.scale(sfondo, (WIDTH, HEIGHT))


personaggio_img = pygame.image.load("personaggio.png")
personaggio_rect = personaggio_img.get_rect(topleft=(400, 300))  # Modifica la posizione del personaggio se necessario


dialogo = ["Benvenuto nella mia bottega!", "Vuoi comprare qualcosa?", "Abbiamo prodotti freschi ogni giorno."]
mostra_dialogo = False
dialogo_index = 0


def disegna_dialogo():
    if mostra_dialogo:
        testo = FONT.render(dialogo[dialogo_index], True, WHITE)
        screen.blit(testo, (50, HEIGHT - 50))


def gioco():
    global mostra_dialogo, dialogo_index

    while True:
        # Gestisci eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if personaggio_rect.collidepoint(event.pos):
                    # Se clicchi sul personaggio, mostra il dialogo
                    mostra_dialogo = True
                    dialogo_index = (dialogo_index + 1) % len(dialogo)

        # Disegna sfondo e elementi
        screen.blit(sfondo, (0, 0))  # Il background ora è scalato a tutta la finestra
        screen.blit(personaggio_img, personaggio_rect.topleft)

        # Disegna dialogo, se attivo
        disegna_dialogo()

        # Aggiorna display
        pygame.display.flip()
gioco()
