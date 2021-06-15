
1.
```Python
rect_x = 50
pygame.draw.rect(screen, WHITE, [rect_x, 50, 50, 50])
rect_x += 1
```
weil er es immer zurück auf die 50 setzt

2.
```Python
if rect_y > 450 or rect_y < 0:
    rect_change_y = rect_change_y * -1
if rect_x > 650 or rect_x < 0:
    rect_change_x = rect_change_x * -1
```
rect_x: x-Koordinate    rect_change_x: veränderung der x-Koordinate
rect_y: y-Koordinate    rect_change_y: Veränderung der y Koordinate

3.

bei 380 (=400-20)

4.
falsch:
```Python
if rect_y > 450 or rect_y < 0:
    rect_y = rect_y * -1
```
es würde nun nicht bouncen sondern jediglich seine Position ändern
korrigiert:
```Python
if rect_y > 450 or rect_y <0:
    rect_change_y = rect_change_y *-1
```

5.
Man muss zwei außenstehende Variablen definieren die man dann anstelle der x und y koordinate einsetzt

6.
Die ersten drei Zeilen des Codes gehören vor dem Main Program. Die letzte Zeile kommt nur in das Main Program

7.
mit einer Liste

8.
```Python
print(stars[1][0])
```

9.
weil bei dem 2. Code nur der Start ausgelassen wird. Der wäre bei beiden Codes bei 0 und somit automatisch gesetzt bei dem 2. Code

10.
Es funktioniert ähnlich wie ein Daumenkino, der Bildschirm wird innerhalb von einer Sekunde 60 mal erneuert. Dabei ändert sich der Winkel innerhalb des Kreises (Linie wird mit hilfe eines Dreiecks verschoben (Sinus und Cosinus)) um 0.3 Grad. So wandert die Linie im Kreis

