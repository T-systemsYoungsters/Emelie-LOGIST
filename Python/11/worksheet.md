1.
Explorer öffnen --> Ansicht --> Dateinamenerweiterung auswählen

2.
Bilder: .jpg
Grafiken: .gif, .png
unkomprimierte Bilder: .bpm
Songs und sound effekte: .mp3, .ogg
unkomprimierte songs: .wav

3.
Die Datei sollte vor dem main programm loop sein und das blit nicht.

4.
Man brauch ein spezielles Programm, welche die Datei in ein anderes Format umwandelt. Aber sobald ein .jpg verändert wurde kann es dies nicht durch die Änderung des Formates rückgängig gemacht werden.

5.
Das Foto welches in einem .jpg Format gespeichert werden, wird durch einen Algorithmus verändert, anders bei .gif und .png. Durch die Veränderung in ein .jpg wird die Hintergrundfarbe auch verändert und ist nun nicht mehr die selbe Farbe. Daher kann man nicht einfach sagen "änder schwarz", da das schwarz nicht genau schwarz ist sondern nur sehr nahe dran.

6.
Wie bei den Bildern muss auch hier der SOund vor dem main programm loop geladen werden. Damit es nicht die 20 mal pro Sekunde abgespielt wird muss man einen Auslöser festlegen. 

Wenn ein Song aufhört zu spielen löst dieser Befehl ihn ab: 


```Python
elif event.type == pygame.constants.USEREVENT:
            pygame.mixer.music.load() #Name des Songs eingeben in den Klammern
            pygame.mixer.music.play()
```
So stellt man eine kleine Playlist zusammen und spielt diese nacheinander ab
