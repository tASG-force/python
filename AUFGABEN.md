## Aufgaben

### Aufgabe 1 – Erste Fahrt
Programmiere den Roboter so, dass er:

- 50 cm geradeaus fährt
- danach stehen bleibt

**Bonus:** Lass ihn anschließend 20 cm rückwärts fahren.

---

### Aufgabe 2 – Abbiegen
Programmiere den Roboter so, dass er:

1. 40 cm geradeaus fährt
2. sich um 90° nach rechts dreht
3. weitere 40 cm fährt

**Bonus:** Ändere das Programm so, dass er nach links abbiegt.

---

### Aufgabe 3 – Quadrat fahren
Der Roboter soll ein Quadrat fahren.

Vorgaben:

- Seitenlänge: 40 cm
- Nach jeder Seite: 90° drehen

Versuche es zunächst **ohne Loop**.

**Bonus:** Schreibe das gleiche Programm anschließend mit einer `for`-Schleife.

---

### Aufgabe 4 – Dreieck
Programmiere den Roboter so, dass er ein möglichst genaues Dreieck fährt.

Überlege selbst:

- Wie viele Seiten braucht ihr?
- Wie oft muss sich der Roboter drehen?
- Welcher Drehwinkel wird benötigt?

**Bonus:** Versucht danach ein Sechseck.

---

### Aufgabe 5 – Geschwindigkeit
Lasst den Roboter dieselbe Strecke mit verschiedenen Geschwindigkeiten fahren.

Zum Beispiel:

```python
db.settings(straight_speed=200)
```

und danach:

```python
db.settings(straight_speed=500)
```

Aufgabe:

- Fahrt jeweils 1 Meter.
- Beobachtet den Unterschied.

**Frage:** Ändert sich durch die Geschwindigkeit auch die gefahrene Distanz?

---

### Aufgabe 6 – Eigene Funktion
Erstellt eine Funktion:

```python
def square():
    ...
```

Die Funktion soll den Roboter ein Quadrat fahren lassen.

Danach soll nur noch

```python
square()
```

aufgerufen werden müssen.

**Bonus:** Fügt einen Parameter für die Größe hinzu:

```python
def square(size):
    ...
```
