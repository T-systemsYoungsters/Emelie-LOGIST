1.
Nichts, sieht aus wie in der Anleitung

2.

```Python
# Game logic
pos = pygame.mouse.get_pos()
x = pos[0]
y = pos[1]
 
# Drawing section
draw_stick_figure(screen, x, 10)
```
3.
Die Aufgaben in einem anderen Event loop würden nur einmal zum Schluss durchlaufen und nicht die ganze Zeit, sowie die im ersten event loop

4.
Weil es dann nach links gehen würde und so auf der linken Seite aus dem Fenster raus wäre. 

5.
Weil die Maus x und y Koordinaten übergibt die Tastatur und der Controller hingegen nicht.

6.
(1,1)
