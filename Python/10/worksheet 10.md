1.
Es ist an sich richtig, jedoch sind die x und y Werte festgelegt und somit wird das Strichmännchen immer an der selben Stelle gezeichnet 

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
Die Aufgaben in einem Event loop würden die ganze Zeit durchlaufen. Er würde auf das Event reagieren, danach seine Aufgabe durchführen und würde den zweiten event loop zwar beachten, da aber keine Aufgabe danach folgt ist keine Veränderung sichtbar und er startet wieder mit dem ersten.
4.
Die Figur würde durch den Tastaturanschlag einen Schritt nach vorne gehen und durch die -1 einen Schritt zurück, das erweckt den Ansschein für uns, dass die Figur auf der Stelle stehen bleibt. 

5.
Weil die Maus x und y Koordinaten übergibt (ähnlich beim Tracking), die Tastatur und der Controller hingegen nicht sie geben nur Richtungen an und benötigen somit einen Startpunkt.


6.
(1,1)
