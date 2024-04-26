# adbpython

## Beschreibung

adbpython ist ein Python-Modul, das eine Schnittstelle zur Android Debug Bridge (ADB) bietet. Mit diesem Modul können Entwickler ADB-Befehle ausführen und mit Android-Geräten interagieren.

## Installation

Um adbpython zu installieren, führen Sie einfach `pip install adbpython` aus.

## Verwendung

Nach der Installation können Sie adbpython in Ihren Python-Skripten importieren und verwenden, um ADB-Befehle auszuführen. Beispiel:

```python
import adbpython as adb

# Verbindung mit einem Android-Gerät herstellen
adb.connect(ip)

adb.shell.keyevent.keyevent(3) or
adb.shell.keyevent.home
```
