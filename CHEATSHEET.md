# Cheatsheet

## Bewegung

### Geradeaus

```python
db.straight(distance=500)
```

`distance`: Distanz, die der Roboter fahren soll, in Millimetern.

- Positive Zahl → vorwärts
- Negative Zahl → rückwärts

Beispiel:

```python
db.straight(500)   # 500 mm vorwärts
db.straight(-200)  # 200 mm rückwärts
```

---

### Drehen

```python
db.turn(angle=90, absolute=False)
```

`angle`: Winkel in Grad, um den bzw. auf den sich der Roboter drehen soll.  
`absolute`: Wenn `True`, dreht sich der Roboter **auf** den angegebenen Winkel. Wenn `False`, dreht er sich **um** den angegebenen Winkel.

Standardmäßig ist `absolute=False`.

- Positive Zahl → rechts
- Negative Zahl → links

Beispiel:

```python
db.turn(90)    # 90° nach rechts
db.turn(-90)   # 90° nach links
```

Mit absolutem Winkel:

```python
db.turn(90, absolute=True)
```

---

### Einen Bogen fahren

```python
db.arc(radius=300, angle=90)
```

`radius`: Radius des Kreises in Millimetern.  
`angle`: Wie viele Grad des Kreises gefahren werden sollen.

Beispiel:

```python
db.arc(radius=300, angle=90)
```

Der Roboter fährt einen Viertelkreis.

- Positiver Radius → Bogen nach rechts
- Negativer Radius → Bogen nach links

---

### Dauerhaft fahren

```python
db.drive(speed=200, turn_rate=0)
```

Der Roboter fährt so lange weiter, bis ein neuer Fahrbefehl oder `db.stop()` ausgeführt wird.

`speed`: Geschwindigkeit in Millimetern pro Sekunde.  
`turn_rate`: Drehgeschwindigkeit in Grad pro Sekunde.

Geradeaus:

```python
db.drive(200, 0)
```

Rückwärts:

```python
db.drive(-200, 0)
```

Nach rechts lenken:

```python
db.drive(200, 30)
```

Nach links lenken:

```python
db.drive(200, -30)
```

---

### Stoppen

```python
db.stop()
```

Stoppt den Roboter.

```python
db.brake()
```

Stoppt den Roboter und bremst die Motoren.

```python
db.hold()
```

Stoppt den Roboter und hält die aktuelle Position.

---

## Geschwindigkeit

### Geschwindigkeit einstellen

```python
db.settings(straight_speed=300, turn_rate=90)
```

`straight_speed`: Geschwindigkeit bei `straight()` in mm/s.  
`turn_rate`: Drehgeschwindigkeit bei `turn()` in Grad/s.

Beispiel:

```python
db.settings(straight_speed=500)
db.straight(1000)
```

---

## Werte des Roboters

### Gefahrene Distanz

```python
distance = db.distance()
```

Gibt zurück, wie weit der Roboter seit dem letzten Reset gefahren ist.

Beispiel:

```python
print(db.distance())
```

---

### Aktueller Winkel

```python
angle = db.angle()
```

Gibt den aktuellen Drehwinkel des Roboters zurück.

Beispiel:

```python
print(db.angle())
```

---

### Distanz und Winkel zurücksetzen

```python
db.reset()
```

Setzt Distanz und Winkel auf `0`.

Eigene Werte setzen:

```python
db.reset(distance=0, angle=90)
```

---

## Warten

```python
wait(1000)
```

Pausiert das Programm.

Die Zeit wird in **Millisekunden** angegeben.

```python
wait(1000)  # 1 Sekunde
wait(500)   # 0,5 Sekunden
wait(2000)  # 2 Sekunden
```

Dafür muss `wait` importiert werden:

```python
from pybricks.tools import wait
```

---

# Python Grundlagen

## Variablen

Mit Variablen können Werte gespeichert werden.

```python
speed = 300
distance = 500
```

Die Variable kann anschließend verwendet werden:

```python
db.straight(distance)
```

Variablen können verändert werden:

```python
speed = 200
speed = speed + 100
```

---

## Loops

### Etwas mehrmals wiederholen

```python
for i in range(4):
    db.straight(500)
    db.turn(90)
```

`range(4)` bedeutet: Wiederhole den eingerückten Code **4-mal**.

Damit fährt der Roboter zum Beispiel ein Quadrat.

---

### Endlosschleife

```python
while True:
    db.straight(100)
```

`while True` bedeutet: Wiederhole den Code immer weiter.

Die Schleife endet erst, wenn das Programm beendet wird oder `break` verwendet wird.

---

## Bedingungen

### Wenn etwas zutrifft

```python
if db.distance() > 500:
    db.stop()
```

`if` bedeutet **wenn**.

Hier:

> Wenn der Roboter mehr als 500 mm gefahren ist → stoppen.

---

### Wenn / sonst

```python
if db.distance() > 500:
    db.stop()
else:
    db.drive(200, 0)
```

`else` bedeutet **ansonsten**.

---

### Vergleiche

```python
x == 5   # gleich
x != 5   # ungleich
x > 5    # größer als
x < 5    # kleiner als
x >= 5   # größer oder gleich
x <= 5   # kleiner oder gleich
```

Wichtig:

```python
x = 5
```

speichert einen Wert.

```python
x == 5
```

vergleicht zwei Werte.

---

## Schleifen und Bedingungen kombinieren

```python
db.reset()

while True:
    db.drive(200, 0)

    if db.distance() >= 1000:
        db.stop()
        break
```

Der Roboter:

1. beginnt zu fahren
2. überprüft ständig die gefahrene Distanz
3. stoppt nach 1000 mm
4. beendet die Schleife

---

## Eigene Funktionen

Wiederkehrenden Code kann man in eine Funktion packen.

```python
def square():
    for i in range(4):
        db.straight(500)
        db.turn(90)
```

Die Funktion wird anschließend so ausgeführt:

```python
square()
```

Mit Parametern:

```python
def square(size):
    for i in range(4):
        db.straight(size)
        db.turn(90)

square(500)
```

---

# Nützliche Merkhilfe

```Python
Distanz:
+ = vorwärts
- = rückwärts

Winkel:
+ = rechts
- = links

Einheiten:
Distanz          → mm
Geschwindigkeit  → mm/s
Winkel           → Grad °
Zeit             → ms
```
