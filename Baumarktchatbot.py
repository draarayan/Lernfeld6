#Dicitonary mit den Produkten des Baumarkt und den jeweiligen Regalen und Kategorien.
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

#Funktion um die Eingabe des Nutzers mit der Datenbank abzugleichen.
def produkt_informationen(abfrage, inventar):
    produkt_info = inventar.get(abfrage)
    
    #Wenn eine Artikelbeschreibung in der Datenbank mit der Nutzereingabe übereinstimmt werden die hinterlegten Informationen ausgegeben.
    if produkt_info:
        print("{} befindet sich im Regal {} in der Kategorie {}.".format(abfrage, produkt_info['Regalnummer'], produkt_info['Kategorie']))
        return produkt_info
    
    #Ausgabe einer Rückmeldung falls kein Artikel in der Datenbank mit der Anfrage übereinstimmt.
    else:
        print("Es tut mir leid, wir haben {} nicht in unserem Inventar.".format(abfrage))
        return None
    
#Funktion um mit einer Kilogramm Angabe einen Preis zu berechnen.
def lieferpreis_berechnen(produkt_info, kilogramm):
    preis_pro_kg = 5  # Annahme des MvPs: Einheitspreis pro Kilogramm für alle Produkte ist 5 Euro.
    lieferpreis = kilogramm * preis_pro_kg
    return lieferpreis if produkt_info else None


#Der Teil des Codes ist auskommentiert, da er aktuell nicht genutzt wird, in Zukunft aber sinnvoll zu nutzen wäre.
'''def produkt_suchen():
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
        print("Produkt nicht gefunden.") '''

print("Willkommen im Baumarkt! Wie kann ich Ihnen helfen?")
print("Sie können nach Produkten suchen, indem Sie den Produktnamen eingeben.")
print("Wir zeigen Ihnen dann die Informationen zum Produkt, einschließlich Regalnummer und Kategorie.")
print("Um den Chat zu beenden, geben Sie 'exit' ein.")

#Abbruch Variable deffinieren
nutzer_exit = False

#Beginn der Hauptschleife, die so lange läuft bis der Wert der Variable nutzer_exit auf True gesetzt wird
while not nutzer_exit:

    #Abfragen des Angliegens
    frage = input("Frage: ")
    
    #Wenn der Nutzer exit eingibt, wird eine Verabschiedung ausgegeben und der Wert der Variable nutzer_exit auf True gesetzt und die Schleife wird beendet.
    if frage.lower() == 'exit':
        print("Vielen Dank für Ihren Besuch. Auf Wiedersehen!")
        nutzer_exit = True
    
    #Wenn der Nutzer nicht exit eingibt, wird die Funktion produkt_informationen genutzt.
    else:
        produkt_info = produkt_informationen(frage, baumarkt_inventar)

        #Wenn in der Abfrage zuvor ein Wert für produkt_info gegeben wurde, wird der Nutzer gefragt, ob er den Lieferpreis erfahren möchte.
        if produkt_info:
            lieferpreis_anzeigen = input("Möchten Sie den Lieferpreis erfahren? (ja/nein) ").lower()
            
            #Wenn der Nutzer zuvor "ja" eingegeben hat, wird er nach der Liefermenge gefragt und die Funktion lieferpreis_berechnen wird genutzt.
            if lieferpreis_anzeigen == 'ja':
                kilogramm = float(input("Wie viele Kilogramm möchten Sie bestellen? "))
                lieferpreis = lieferpreis_berechnen(produkt_info, kilogramm)

                #Wenn ein Wert für lieferpreis zurückgegeben wurde, wird dieser Ausgegeben, sonst wir eine Fehlermeldung ausgegeben.
                if lieferpreis:
                    print("Der Lieferpreis für {} kg {} beträgt {} Euro.".format(kilogramm, frage, lieferpreis))
                else:
                    print("Fehler bei der Lieferpreisberechnung.")
            
            #Wenn der Nutzer nicht "ja" eingibt, erhält er eine Rückmeldung und die Schleife beginnt von vorne.
            else:
                print("Okay, kein Problem.")

# Ende

# mögliche Erweiterung: wenn z.B. Kunden oder Lieferanten neue Produkte in das System hinzufügen möchten
