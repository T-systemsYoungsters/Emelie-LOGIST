```Python 
# Import a library of functions called 'pygame'
import pygame
import random

def draw_house():
    pygame.draw.rect(screen, BROWN, [200,230,250, 100],0)
    pygame.draw.rect(screen, BROWN, [200,150,70, 100],0)
    pygame.draw.rect(screen, GREY, [0,350,400, 50],0)
    pygame.draw.rect(screen, GREY, [30,250,50, 100],0)
    pygame.draw.ellipse(screen, WHITE, [210, 160,50,50],0)
    pygame.draw.polygon(screen, GREY, [[240,100], [200,150], [270,150]], 0)

def draw_street():
    pygame.draw.rect(screen, GREY, [30,250,50, 100],0)
    pygame.draw.rect(screen, GREY, [270,210,300, 20],0)
    
 
# Initialize the game engine
pygame.init()
 
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [51,255,51]
RED = [255,0,0]
BLUE =[94, 174, 255]
GREY =[128,128,128]
BROWN = [255,167,79]
DBLUE= [0,0,255]
 
# Set the height and width of the screen
SIZE = [400, 400]
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")
 
# Create an empty array
rain_list = []
 
# Loop 50 times and add a snow flake in a random x,y position
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    rain_list.append([x, y])
 
clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.
done = False
while not done:
 
    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop
 
    # Set the screen background
    screen.fill(BLUE)
 
    # Process each snow flake in the list
    for i in range(len(rain_list)):
 
        # Draw the snow flake
        pygame.draw.circle(screen, DBLUE, rain_list[i], 2)
        pygame.draw.rect(screen, GREEN, [0,250,400, 400],0)
        draw_house()
        draw_street()
        
        
 
        # Move the snow flake down one pixel
        rain_list[i][1] += 1
 
        # If the snow flake has moved off the bottom of the screen
        if rain_list[i][1] > 400:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            rain_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 400)
            rain_list[i][0] = x
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(20)
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

```
