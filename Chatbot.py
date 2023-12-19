# Datenstruktur für die Produkte im Baumarkt mit Regalnummern
baumarkt_inventar = {
    'Wandfarbe': {'Regalnummer': 'A1', 'Kategorie': 'Farbe'},
    'Lack': {'Regalnummer': 'A2', 'Kategorie': 'Farbe'},
    'Sprühfarbe': {'Regalnummer': 'A3', 'Kategorie': 'Farbe'},
    'Hammer': {'Regalnummer': 'B1', 'Kategorie': 'Werkzeug'},
    'Schraubendreher': {'Regalnummer': 'B2', 'Kategorie': 'Werkzeug'},
    'Säge': {'Regalnummer': 'B3', 'Kategorie': 'Werkzeug'},
    'Blumenerde': {'Regalnummer': 'C1', 'Kategorie': 'Garten'},
    'Gartenschlauch': {'Regalnummer': 'C2', 'Kategorie': 'Garten'},
    'Pflanzentöpfe': {'Regalnummer': 'C3', 'Kategorie': 'Garten'},
    # Fügen Sie weitere Produkte und Regalnummern nach Bedarf hinzu
}

def produkt_informationen(abfrage, inventar):
    if abfrage in inventar:
        produkt_info = inventar[abfrage]
        print("{} befindet sich im Regal {} in der Kategorie {}.".format(abfrage, produkt_info['Regalnummer'], produkt_info['Kategorie']))
        return produkt_info
    else:
        print("Es tut mir leid, wir haben {} nicht in unserem Inventar.".format(abfrage))
        return None

def lieferpreis_berechnen(produkt_info, kilogramm):
    if produkt_info:
        preis_pro_kg = 5  # Annahme: Einheitspreis pro Kilogramm für alle Produkte ist 5 Euro
        lieferpreis = kilogramm * preis_pro_kg
        return lieferpreis
    else:
        return None

def produkt_suchen():
    # Eingabe des Benutzers für die Produktsuche
    suchbegriff = input("Wonach suchen Sie? ")

    # Produktinformationen abrufen
    produkt_info = produkt_informationen(suchbegriff, baumarkt_inventar)

    if produkt_info:
        # Eingabe des Benutzers für die Lieferpreisberechnung
        kilogramm = float(input("Wie viele Kilogramm möchten Sie bestellen? "))

        # Lieferpreis berechnen
        lieferpreis = lieferpreis_berechnen(produkt_info, kilogramm)

        if lieferpreis:
            print("Der Lieferpreis für {} kg {} beträgt {} Euro.".format(kilogramm, suchbegriff, lieferpreis))

# Begrüßungsnachricht und Tutorial
print("Willkommen im Baumarkt! Wie kann ich Ihnen helfen?")
print("Sie können nach Produkten suchen, indem Sie den Produktnamen eingeben.")
print("Wenn Sie den Lieferpreis für ein Produkt berechnen möchten, geben Sie 'suche' ein und folgen Sie den Anweisungen.")

# Hauptschleife für den Chatbot
while True:
    # Eingabe des Benutzers
    frage = input("Frage: ")

    # Beenden Sie die Schleife, wenn der Benutzer "exit" eingibt
    if frage.lower() == 'exit':
        print("Vielen Dank für Ihren Besuch. Auf Wiedersehen!")
        break

    # Prüfen, ob der Benutzer nach einem Produkt sucht
    if frage.lower() == 'suche':
        produkt_suchen()
    else:
        # Produktinformationen abrufen
        produkt_info = produkt_informationen(frage, baumarkt_inventar)

# Ende

# mögliche Erweiterung: wenn z.B. Kunden oder Lieferanten neue Produkte in das System hinzufügen möchten

#Start
#1. Begrüßungsnachricht anzeigen
#2. Zeige ein kurzes Tutorial zum Benutzen des Chatbots:
#   - Benutzer kann nach Produkten suchen, indem er den Produktnamen eingibt
#   - Benutzer kann den Lieferpreis für ein Produkt berechnen, indem er 'suche' eingibt und den Anweisungen folgt
#3. Hauptschleife starten:
#   - Warte auf die Benutzereingabe
#
#   - Wenn Benutzer 'exit' eingibt:
#
#    - Beende die Schleife und das Programm
#   - Wenn Benutzer 'suche' eingibt:
#     - Rufe Funktion "produkt_suchen" auf
#       - Frage den Benutzer nach dem gesuchten Produkt
#      - Rufe Funktion "produkt_informationen" auf, um Produktinformationen zu erhalten
#      - Wenn Produkt gefunden:
#        - Frage den Benutzer nach der Anzahl der Kilogramm, die er bestellen möchte
#         - Rufe Funktion "lieferpreis_berechnen" auf, um den Lieferpreis zu berechnen
#         - Zeige den Lieferpreis an
#       - Wenn Produkt nicht gefunden:
#         - Zeige entsprechende Fehlermeldung
#
#   - Wenn Benutzer etwas anderes eingibt:
#     - Rufe Funktion "produkt_informationen" auf, um Produktinformationen zu erhalten
#     - Wenn Produkt gefunden:
#       - Zeige Produktinformationen an
#     - Wenn Produkt nicht gefunden:
#       - Zeige entsprechende Fehlermeldung
#Ende
