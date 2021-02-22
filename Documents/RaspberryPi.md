<h2>SD Karte vorbereiten: </h2>
<p>Betiebsystem (als ZIP-Datei) auf diese geladen
<p>ssh Datei anlegen, beliebige Datei duplizieren und ssh benennen. Ohne Endung. Inhalt löschen
<p>Karte in Raspberry Pi stecken und Raspberry Pi starten
<p>
<p><h2> Raspberry Pi mit Wifi verbinden</h2>
<p>wpa_supplicant.conf im (/boot) auf der sd karte abspeichern 
<p>Wlan und Passwort in der Datei hinterlegen
<p>IP adresse rausfinden (Ping Methode:https://bitreporter.de/raspberrypi/raspberry-pi-ip-adresse-herausfinden/)
<p>in 'cmd' ssh pi@<IP>
<p>succssefully connected
<p> 
<p> sudo apt-get update
<p> sudo apt-get upgrade
<p>
<p><h2>Zeit, Sprache einstellen</h2>
<p> sudo raspi-config
<p>change user password; Passwort ändern
<p>locations caption; change locations; Deutschland de_DE.UFT-8; Sprache geändert
<p> locations caption; change timezone; Europe; Berlin; Zeit anpassen
<p>Advanced options;Expand filesystem; neustart; volle Speicherplatznutzung
