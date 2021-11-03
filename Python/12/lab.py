import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class rectangle():
    def __init__(self):
        self.x=random.randrange(701)
        self.y=random.randrange(501)
        self.color=RED
        
        self.change_x=random.randrange(-3,3)
        self.change_y=random.randrange(-3,3)
    def height(self):
        self.a=random.randrange(20,71)
    def width(self):
        self.b=random.randrange(20,71)

    def move(self):
        self.x += self.change_x
        self.y += self.change_y
    def setColor(self, color):
        self.color=color
    def draw(self):
        print(pygame.draw.rect(screen,self.color,[self.x,self.y,self.a,self.b],0))

class ellipse(rectangle):
    def draw(self):
        print(pygame.draw.ellipse(screen, self.color, [self.x,self.y,30,15], 0))




        

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

my_list=[]
my_color=[RED, GREEN, WHITE]
for i in range(100):
    my_object= rectangle()
    my_object.a=10
    my_object.b=20
    my_object.setColor(my_color[random.randrange(0, 3)])
    my_object.move() 
    my_object.draw() 
    my_list.append(my_object) 
    my_object2= ellipse()
    my_object2.setColor(my_color[random.randrange(0, 3)])
    my_object2.draw()
    my_list.append(my_object2)
   

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
    #screen.fill(BLACK)
 
    
    # --- Drawing code should go here
      
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()

