# Marketing-Analyse

Voraussetzungen installierenNutze dafür im Terminal oder der Eingabeaufforderung folgenden Befehl:Bashpip install pandas openpyxl
Skript ausführenBashpython daten_analyse.py 

Beim ersten Start wird eine umsatzdaten.csv angelegt und direkt verarbeitet.Wiederkehrende Aufgaben automatisierenWindows: Öffne die Aufgabenplanung (Task Scheduler) $\rightarrow$ Einfache Aufgabe erstellen $\rightarrow$ Auslöser (z. B. täglich 08:00 Uhr) festlegen $\rightarrow$ als Aktion python.exe mit dem Pfad zum Skript hinterlegen.Linux/Mac: Erstelle einen Cronjob über crontab -e:Bash0 8 * * * /usr/bin/python3 /pfad/zu/daten_analyse.py
