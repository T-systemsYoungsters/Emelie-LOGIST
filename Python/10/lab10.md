```Python
import pygame

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [51,255,51]
RED = [255,0,0]
BLUE =[94, 174, 255]
GREY =[128,128,128]
BROWN = [255,167,79]
DBLUE= [0,0,255]

a=1
b=1

def draw_house(screen, x, y):
    pygame.draw.rect(screen, BROWN, [100+x,131+y,250, 100],0)
    pygame.draw.rect(screen, BROWN, [100+x,51+y,70, 100],0)
    pygame.draw.polygon(screen, GREY, [[140+x,1+y], [100+x,51+y], [170+x,51+y]], 0)

def draw_tree (screen, x, y):
    pygame.draw.rect(screen, BROWN, [a+25+x,b+50+y, 30, 120],0)
    pygame.draw.ellipse(screen, GREEN, [a+x, b+y,80,80],0)


# Setup
pygame.init()
 
# Set the width and height of the screen [width,height]
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)

# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 10
y_coord = 10

#boundaries


 
# -------- Main Program Loop -----------
while not done:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0


    # --- Game Logic
 
    # Move the object according to the speed vector.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
 
 
    # Call draw  function
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
 
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
     #boundaries
    if pygame.K_LEFT and x_coord > 620:
        x_coord -= x_speed
    elif pygame.K_RIGHT and x_coord< 0:
        x_coord+= 3
    elif pygame.K_UP and y_coord > 320:
        y_coord-=y_speed
    elif pygame.K_DOWN and y_coord <0:
        y_coord+=3
    
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    draw_house(screen, x, y)
    draw_tree (screen, x_coord,y_coord)
 
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
 
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 20 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
```