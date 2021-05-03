Part1
```Python
row=10
column=10
i=10
for row in range(9):
    for column in range(row+1):
        print (i,end=" ")
        i=i+1
 
    # Print a blank line
    # to move to the next row
    print()
    ```
   Part2
   ```Python 
i=int(input("Wie viele Reihen soll das Viereck haben?"))
j=int(input("Wie viele Spalten soll das Viereck haben?"))
for row in range(i):
    for column in range(j):
        if row==0 or row==i-1 or column==0 or column==j-1:
            print("o", end=" ")
        else:
            print(" ", end=" ")
        
    
    print()
    
```

```Python 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (300, 200)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    #ay=0
    #for ay in range (20):
       # ay=ay+10
    for y_offset in range(0, 400, 10):
         pygame.draw.rect(screen, GREEN, [0+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [10+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [20+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [30+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [40+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [50+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [60+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [70+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [80+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [90+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [100+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [110+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [120+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [130+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [140+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [150+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [160+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [170+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [180+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [190+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [200+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [210+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [220+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [230+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [240+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [250+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [260+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [270+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [280+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [290+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [300+y_offset, 0+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [0+y_offset, 10+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [0+y_offset, 20+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [0+y_offset, 30+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [0+y_offset, 40+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [0+y_offset, 50+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [0+y_offset, 60+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [0+y_offset, 70+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [0+y_offset, 80+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [0+y_offset, 90+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [0+y_offset, 100+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [0+y_offset, 110+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [0+y_offset, 120+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [0+y_offset, 130+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [0+y_offset, 140+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [0+y_offset, 150+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [0+y_offset, 160+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [0+y_offset, 170+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [0+y_offset, 180+y_offset, 5, 5])
    for y_offset in range(0, 400, 10):
        pygame.draw.rect(screen, GREEN, [0+y_offset, 190+y_offset, 5, 5])
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
```

Mit Phans Hilfe
```Python

import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (300, 200)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    for row in range(0,300,10):
        for column in range(0,200,10):
             pygame.draw.rect(screen, GREEN, [row, column, 5, 5])
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
```

