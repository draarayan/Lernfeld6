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
}

def produkt_informationen(abfrage, inventar):
    produkt_info = inventar.get(abfrage)
    if produkt_info:
        print("{} befindet sich im Regal {} in der Kategorie {}.".format(abfrage, produkt_info['Regalnummer'], produkt_info['Kategorie']))
        return produkt_info
    else:
        print("Es tut mir leid, wir haben {} nicht in unserem Inventar.".format(abfrage))
        return None

def lieferpreis_berechnen(produkt_info, kilogramm):
    preis_pro_kg = 5  # Annahme: Einheitspreis pro Kilogramm für alle Produkte ist 5 Euro
    lieferpreis = kilogramm * preis_pro_kg
    return lieferpreis if produkt_info else None

def produkt_suchen():
    suchbegriff = input("Wonach suchen Sie? ")
    produkt_info = produkt_informationen(suchbegriff, baumarkt_inventar)

    if produkt_info:
        lieferpreis_anzeigen = input("Möchten Sie den Lieferpreis erfahren? (ja/nein) ").lower()

        if lieferpreis_anzeigen == 'ja':
            kilogramm = float(input("Wie viele Kilogramm möchten Sie bestellen? "))
            lieferpreis = lieferpreis_berechnen(produkt_info, kilogramm)

            if lieferpreis:
                print("Der Lieferpreis für {} kg {} beträgt {} Euro.".format(kilogramm, suchbegriff, lieferpreis))
            else:
                print("Fehler bei der Lieferpreisberechnung.")
        else:
            print("Okay, kein Problem.")
    else:
        print("Produkt nicht gefunden.")

print("Willkommen im Baumarkt! Wie kann ich Ihnen helfen?")
print("Sie können nach Produkten suchen, indem Sie den Produktnamen eingeben.")
print("Wir zeigen Ihnen dann die Informationen zum Produkt, einschließlich Regalnummer und Kategorie.")
print("Um den Chat zu beenden, geben Sie 'exit' ein.")

while True:
    frage = input("Frage: ")

    if frage.lower() == 'exit':
        print("Vielen Dank für Ihren Besuch. Auf Wiedersehen!")
        break
    else:
        produkt_info = produkt_informationen(frage, baumarkt_inventar)

        if produkt_info:
            lieferpreis_anzeigen = input("Möchten Sie den Lieferpreis erfahren? (ja/nein) ").lower()

            if lieferpreis_anzeigen == 'ja':
                kilogramm = float(input("Wie viele Kilogramm möchten Sie bestellen? "))
                lieferpreis = lieferpreis_berechnen(produkt_info, kilogramm)

                if lieferpreis:
                    print("Der Lieferpreis für {} kg {} beträgt {} Euro.".format(kilogramm, frage, lieferpreis))
                else:
                    print("Fehler bei der Lieferpreisberechnung.")
            else:
                print("Okay, kein Problem.")

# Ende

# mögliche Erweiterung: wenn z.B. Kunden oder Lieferanten neue Produkte in das System hinzufügen möchten
