# Marketing-Analyse

Voraussetzungen installieren
Nutze dafür im Terminal oder der Eingabeaufforderung folgenden Befehl:
pip install pandas openpyxl

Skript ausführen:
python daten_analyse.py

Beim ersten Start wird eine umsatzdaten.csv angelegt und direkt verarbeitet.

Windows: Öffne die Aufgabenplanung (Task Scheduler) $\rightarrow$ Einfache Aufgabe erstellen $\rightarrow$ Auslöser (z. B. täglich 08:00 Uhr) festlegen $\rightarrow$ als Aktion python.exe mit dem Pfad zum Skript hinterlegen.

Linux/Mac: Erstelle einen Cronjob über crontab -e:

0 8 * * * /usr/bin/python3 /pfad/zu/daten_analyse.py



