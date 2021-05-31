import pygame
import math
 # Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (10, 10, 92.16)
GREEN = (10, 130, 92.16)
RED = (255, 0, 0)
GREY = (150,150,150)
BROWN =(128, 64,0)
TREE_GREEN= (0,128,0)
 
PI = 3.141592653
 

# Set the height and width of the screen
size = (600, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My house by night")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
# Loop as long as done == False
while not done:
 
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Clear the screen and set the screen background
    screen.fill(BLUE)
    # Draw a rectangle
    pygame.draw.rect(screen, GREEN, [0, 400, 600, 200], 0)

    #triangle house
    pygame.draw.polygon(screen, RED, [[250, 20], [70,130],[430,130]], 0)

    #rectangle house
    pygame.draw.rect(screen, GREY, [70,130 , 360,270],0)

    #arc moon
    pygame.draw.arc(screen, WHITE, [20, 40, 50, 50], 0,2*PI )

    #rectangle tree
    pygame.draw.rect(screen, BROWN, [ 500,200,50,200],0)

    #rectangle tree
    pygame.draw.rect(screen, TREE_GREEN, [485,140,80,80],0)

    #falling star
    for y_offset in range(0, 100, 30):
        pygame.draw.arc(screen, WHITE, [400+ y_offset, 40+ y_offset, 5, 5 ], 0,2*PI )

    #windows
        for y_offset in range(0, 250, 50):
            pygame.draw.rect(screen, BLACK, [90+ y_offset, 150 + y_offset, 30, 30], 0)
        for y_offset in range(0, 200, 50):
            pygame.draw.rect(screen, BLACK, [140+ y_offset, 150 + y_offset, 30, 30], 0)
        for y_offset in range(0, 150, 50):
            pygame.draw.rect(screen, BLACK, [190+ y_offset, 150 + y_offset, 30, 30], 0)
        for y_offset in range(0, 150, 50):
            pygame.draw.rect(screen, BLACK, [240+ y_offset, 150 + y_offset, 30, 30], 0)
        for y_offset in range(0, 150, 50):
            pygame.draw.rect(screen, BLACK, [290+ y_offset, 150 + y_offset, 30, 30], 0)
        for y_offset in range(0, 100, 50):
            pygame.draw.rect(screen, BLACK, [340+ y_offset, 150 + y_offset, 30, 30], 0)
        for y_offset in range(0, 200, 50):
            pygame.draw.rect(screen, BLACK, [90+ y_offset, 200 + y_offset, 30, 30], 0)
        for y_offset in range(0, 150, 50):
            pygame.draw.rect(screen, BLACK, [90+ y_offset, 250 + y_offset, 30, 30], 0)
        for y_offset in range(0, 100, 50):
            pygame.draw.rect(screen, BLACK, [90+ y_offset, 300 + y_offset, 30, 30], 0)
        pygame.draw.rect(screen, BLACK, [90, 350, 30, 30], 0)
        pygame.draw.rect(screen, BLACK, [390, 150, 30, 30], 0)

    #door
    pygame.draw.rect(screen, BLACK, [340, 300, 80, 100], 0)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()
