import cv2
import pygame
import pygame_widgets as pw
from pygame_widgets.button import Button


def apartment_func(apartment, roommates, findTenants, ap, ro, fi):
    screen_image = pygame.image.load(r'screen.jpg')
    screen.blit(screen_image, (-100, -100))

    # set displat
    if ap is not None:
        pygame.display.set_caption('Apartment for Rent')
    if ro is not None:
        pygame.display.set_caption('Looking for Roommates')
    if fi is not None:
        pygame.display.set_caption('Find Tenants')

    img = pygame.image.load('home.png')
    pygame.display.set_icon(img)
    # set font
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    color = color_inactive = pygame.Color((0, 0, 0))
    done = False


    # defining a font
    smallfont = pygame.font.SysFont('georgia', 20)
    # rendering a text written in this font
    text = smallfont.render('quit', True, color)

    while not done:
        apartment.hide()
        roommates.hide()
        findTenants.hide()
        # stores the (x,y) coordinates into the variable as a tuple
        mouse = pygame.mouse.get_pos()
        # define events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button the app is terminated
                if 0 <= mouse[0] <= 40 and 0 <= mouse[1] <= 30:
                    done = True

        screen.blit(screen_image, (-100, -100))

        # quit
        screen.blit(text, (0, 0))

        pygame.display.update()
        pygame.display.flip()
        clock.tick(30)


def display_slide(screen):
    # set displat
    pygame.display.set_caption('SwipingHome')
    img = pygame.image.load('home.png')
    pygame.display.set_icon(img)
    # set font
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    color = color_inactive = pygame.Color((0, 0, 0))
    done = False

    # defining a font
    smallfont = pygame.font.SysFont('georgia', 20)
    # rendering a text written in this font
    text = smallfont.render('quit', True, color)

    # set screen image
    screen_image = pygame.image.load(r'screen.jpg')
    # screen_image = pygame.image.load(r'hands_key.jpg')

    while not done:
        # stores the (x,y) coordinates into the variable as a tuple
        mouse = pygame.mouse.get_pos()
        # define events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button the app is terminated
                if 0 <= mouse[0] <= 40 and 0 <= mouse[1] <= 30:
                    pygame.quit()

        # first button:
        apartment = Button(
            screen, SCREEN_WIDTH // 2 - 107, SCREEN_HEIGHT // 2 + 100, 210, 60, text='Apartments for Rent',
            fontSize=25, margin=20,
            inactiveColour=(240, 240, 240),
            pressedColour=(50, 50, 50), radius=20,
            onClick=lambda: apartment_func(apartment, roommates, findTenants, True, None, None)
        )
        # apartment.hide()
        pygame.display.set_caption('SwipingHome')
        # second button:
        roommates = Button(
            screen, SCREEN_WIDTH // 2 - 107, SCREEN_HEIGHT // 2, 210, 60, text='Looking for Roommates',
            fontSize=25, margin=20,
            inactiveColour=(240, 240, 240),
            pressedColour=(50, 50, 50), radius=20,
            onClick=lambda: apartment_func(apartment, roommates, findTenants, None, True, None)
        )
        # roommates.hide()
        pygame.display.set_caption('SwipingHome')
        # third button:
        findTenants = Button(
            screen, SCREEN_WIDTH // 2 - 107, SCREEN_HEIGHT // 2 + 190, 210, 60, text='Find Tenants',
            fontSize=25, margin=20,
            inactiveColour=(240, 240, 240),
            pressedColour=(50, 50, 50), radius=20,
            onClick=lambda: apartment_func(apartment, roommates, findTenants, None, None, True)
        )
        # findTenants.hide()
        pygame.display.set_caption('SwipingHome')

        screen.blit(screen_image, (-100, -100))

        # # apartment
        apartment.listen(event)
        apartment.draw()
        # # roommates
        roommates.listen(event)
        roommates.draw()
        # # findTenants
        findTenants.listen(event)
        findTenants.draw()
        # quit
        screen.blit(text, (0, 0))

        pw.update(events)
        pygame.display.flip()
        clock.tick(30)


pygame.init()
# set screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

display_slide(screen)

pygame.quit()
