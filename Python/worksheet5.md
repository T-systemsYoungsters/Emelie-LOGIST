1) The y-axis goes down and not up, (0/0) is in the upper left hand corner, focus on the upper right quadrant while the cartesian graphic focus on the uper right quadrant
2)
```Python
import pygame
pygame.init()
```
3) WHITE = (255, 255, 255)
Uppercase because its a constant varriable which doesnt change, numbers in the bracket is the number of the colours red,green,blue ; je höher die Nummer desto mehr ist von der Farbe enthalten. Wenn alle drei Farben bei 255 liegen ist es weiß
4) when its a constant variable it is in upper case, if it isnt a constant it is in lower case, so the variable can change like the colours of the sky
5) it creates a window
6)es wird alles ausgeführt solange der user bestimmte sachen drückt/nicht drückt
7) es legt fest wie oft sich der screen updated 
8) 
```Python
pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
```
es gibt eine grüne Linie aus die bei (0,0) startet und bei (100,100) endet und 5 Pixel lang ist

9) with a for loop
10) 
```Python
pygame.draw.rect(screen, BLACK, [20, 20, 250, 100],0)
``` 
there is no black border around the rectangle it is just filled in with black
11)
```Python
pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)
```
x,y = 20,20
tall=100
wide=250
line width= 2 pixel
origin coordinate= corne on the upper lelft, where the rectangle of the ellipse is starting 
12) it has a strat and an end
13) a variable where everything is stored thats important for the text (typeface, size,...); creates an image so the third step is to tell them where it is supposed to be
14)
15)
```Python
pygame.draw.polygon(screen, BLACK, [[50,100],[0,200],[200,200],[100,50]], 5)
```
first corner(50,100); second corner (0,200); third (200,200), fourth (100,50) with a line thickness of 5
16) shows the drawing
17) nessessary to close the window
18)
```Python
circle(surface, color, center, radius, width=0, draw_top_right=None, draw_top_left=None, draw_bottom_left=None, draw_bottom_right=None) 
```