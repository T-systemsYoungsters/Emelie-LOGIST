## SD Karte vorbereiten: 
Betiebsystem (als ZIP-Datei) auf diese geladen
ssh Datei anlegen, beliebige Datei duplizieren und ssh benennen. Ohne Endung. Inhalt löschen
Karte in Raspberry Pi stecken und Raspberry Pi starten

## Raspberry Pi mit Wifi verbinden
pa_supplicant.conf im (/boot) auf der sd karte abspeichern 
Wlan und Passwort in der Datei hinterlegen
IP adresse rausfinden (Ping Methode:https://bitreporter.de/raspberrypi/raspberry-pi-ip-adresse-herausfinden/)
in 'cmd' ssh pi@< IP >
succssefully connected
 
 sudo apt-get update
sudo apt-get upgrade

## Zeit, Sprache einstellen
 sudo raspi-config
change user password; Passwort ändern
locations caption; change locations; Deutschland de_DE.UFT-8; Sprache geändert
 locations caption; change timezone; Europe; Berlin; Zeit anpassen
Advanced options;Expand filesystem; neustart; volle Speicherplatznutzung
