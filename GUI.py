import cv2
import pygame
import pygame_widgets as pw
from pygame_widgets.button import Button


pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('SwipingHome')
img = pygame.image.load('home.png')
pygame.display.set_icon(img)
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()
color = color_inactive = pygame.Color((0, 0, 0))
color_dark = pygame.Color((255, 255, 255))
active = False
done = False



# defining a font
smallfont = pygame.font.SysFont('georgia', 20)
# rendering a text written in
# this font
text = smallfont.render('quit', True, color)

# first button:
# apartment_font = pygame.font.SysFont('georgia', 20)
# apartment = apartment_font.render('Apartments for Rent', True, color)
apartment = Button(
        screen, SCREEN_WIDTH // 2 - 107, SCREEN_HEIGHT // 2 + 100, 210, 60, text='Apartments for Rent',
        fontSize=25, margin=20,
        inactiveColour=(240, 240, 240),
        pressedColour=(0, 255, 0), radius=20,
        onClick=lambda: print('Click')
    )
# second button:
# roommates_font = pygame.font.SysFont('georgia', 20)
# roommates = roommates_font.render('Looking for Roommates', True, color)
roommates = Button(
        screen, SCREEN_WIDTH // 2 - 107, SCREEN_HEIGHT // 2, 210, 60, text='Looking for Roommates',
        fontSize=25, margin=20,
        inactiveColour=(240, 240, 240),
        pressedColour=(0, 255, 0), radius=20,
        onClick=lambda: print('Click')
    )
# third button:
# findTenants_font = pygame.font.SysFont('georgia', 20)
# findTenants = findTenants_font.render('Find Tenants', True, color)
findTenants = Button(
        screen, SCREEN_WIDTH // 2 - 107, SCREEN_HEIGHT // 2 + 190, 210, 60, text='Find Tenants',
        fontSize=25, margin=20,
        inactiveColour=(240, 240, 240),
        pressedColour=(0, 255, 0), radius=20,
        onClick=lambda: print('Click')
    )

# set screen image
screen_image = pygame.image.load(r'screen.jpg')
# screen_image = pygame.image.load(r'hands_key.jpg')

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if the mouse is clicked on the button the app is terminated
            if 0 <= mouse[0] <= 40 and 0 <= mouse[1] <= 30:
                pygame.quit()

            if apartment.collidepoint(mouse):
                # prints current location of mouse
                print('button was pressed at {0}'.format(mouse))
            # # if the mouse is clicked on the apartment button go to the relevant screen
            # if 0 <= mouse[0] <= 40 and 0 <= mouse[1] <= 30:
            #     pygame.quit()
            # # if the mouse is clicked on the roommates button go to the relevant screen
            # if 0 <= mouse[0] <= 40 and 0 <= mouse[1] <= 30:
            #     pygame.quit()
            # # if the mouse is clicked on the findTenants button go to the relevant screen
            # if 0 <= mouse[0] <= 40 and 0 <= mouse[1] <= 30:
            #     pygame.quit()

    # screen.fill((200, 240, 250))
    # stores the (x,y) coordinates into the variable as a tuple
    mouse = pygame.mouse.get_pos()
    # # if mouse is hovered on a button it changes to darker shade
    # if 0 <= mouse[0] <= 30 and 0 <= mouse[1] <= 40:
    #     pygame.draw.rect(screen, color_dark, [0, 0, 40, 30])
    # else:
    #     pygame.draw.rect(screen, color_dark, [0, 0, 40, 30])

    screen.blit(screen_image, (-100, -100))

    # apartment
    apartment.listen(event)
    apartment.draw()
    # screen.blit(apartment, (SCREEN_WIDTH // 2 - 105, SCREEN_HEIGHT // 2 + 200))
    # roommates
    roommates.listen(event)
    roommates.draw()
    # screen.blit(roommates, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 + 100))
    # findTenants
    findTenants.listen(event)
    findTenants.draw()
    # screen.blit(findTenants, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2))
    # quit
    screen.blit(text, (0, 0))




    pygame.display.update()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
