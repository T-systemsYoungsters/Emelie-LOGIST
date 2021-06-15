import pygame

#colours
WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(51,255,51)
BROWN=(255,167,79)

def draw_tree (screen, x, y):
    pygame.draw.rect(screen, BROWN, [10+x,20+y, 8, 30],0)
    pygame.draw.ellipse(screen, GREEN, [1+x, 1+y,25,25],0)

# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([570, 456])

# This sets the name of the window
pygame.display.set_caption('CMSC 150 is cool')
 
clock = pygame.time.Clock()

# Before the loop, load the sounds:
click_sound = pygame.mixer.Sound("laser5.ogg")
 
# Set positions of graphics
background_position = [0, 0]

# Load and set up graphics.
background_image = pygame.image.load("test.jpg").convert()


done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
 
    # Copy image to screen:
    screen.blit(background_image, background_position)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    draw_tree_position = pygame.mouse.get_pos()
    x = draw_tree_position[0]
    y = draw_tree_position[1]

    draw_tree(screen, x, y)
 
    # Copy image to screen:
    #screen.blit(draw_tree, [x, y])
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
