inventory = []

leiri_items = ["roskapussi"]
maja_items = ["kartta", "köysi"]
metsa_items = ["lauta"]
joki_items = ["mela"]

roskat = ["metsä", "joki", "kukkula"]
siivotut_paikat = []


def main_menu():
    print("\n--- VALIKKO ---")
    print("katso - tutki nykyistä paikkaa")
    print("liiku - siirry toiseen paikkaan")
    print("ota - ota esine")
    print("tavarat - näytä tavaraluettelo")
    print("käytä - käytä esineitä")
    print("siivoa - kerää roskat")
    print("apua - näytä ohjeet")
    print("lopeta - lopeta peli")


def apua():
    print("\n--- OHJEET ---")
    print("Tavoitteesi on päästä pois metsästä.")
    print("Voit valita yhden kolmesta reitistä:")
    print("1. Etsi kartta ja seuraa kukkulan metsäpolkua.")
    print("2. Etsi köysi ja korjaa sillan kaide.")
    print("3. Etsi lauta ja mela, korjaa vene ja ylitä joki.")
    print("\nTutki paikkoja komennolla katso.")
    print("Kerää esineitä komennolla ota.")
    print("Komento käytä yrittää avata nykyisen paikan reitin.")
    print("Voit myös kerätä roskia, jos sinulla on roskapussi.")
    print("Roskat eivät estä pelin läpäisemistä.")
    print("Virheellinen komento ei lopeta peliä.")
    print("Peli ei tallenna edistymistä sulkemisen jälkeen.")


def mahdolliset_reitit(paikka):
    if paikka == "leiri":
        return ["maja", "metsä", "kukkula"]
    elif paikka == "maja":
        return ["leiri"]
    elif paikka == "metsä":
        return ["leiri", "silta", "joki"]
    elif paikka == "kukkula":
        return ["leiri"]
    elif paikka == "silta":
        return ["metsä"]
    elif paikka == "joki":
        return ["metsä"]

    return []


def paikan_esineet(paikka):
    if paikka == "leiri":
        return leiri_items
    elif paikka == "maja":
        return maja_items
    elif paikka == "metsä":
        return metsa_items
    elif paikka == "joki":
        return joki_items

    return []


def katso(paikka):
    print(f"\n--- {paikka.upper()} ---")

    if paikka == "leiri":
        print("Olet pienellä leiripaikalla.")
        print("Myrsky on kaatanut puun päätielle.")
        print("Sinun täytyy löytää toinen reitti kylään.")
        print("Lähellä ovat huoltomaja, metsä ja kukkula.")

    elif paikka == "maja":
        print("Saavut avoimeen huoltomajaan.")
        print("Seinällä lukee: Hätätilanteessa lainaa tarvikkeita.")
        print("Kartta näyttää kukkulalta alkavan polun.")
        print("Köysi voisi auttaa sillan korjaamisessa.")

    elif paikka == "metsä":
        print("Metsässä on hiljaista myrskyn jälkeen.")
        print("Polku haarautuu sillalle ja joelle.")
        print("Vanhan puupinon vieressä on ehjä lauta.")
        print("Sitä voisi käyttää korjaamiseen.")

    elif paikka == "kukkula":
        print("Kukkulalta näkyvät kylän valot.")
        print("Alhaalla alkaa monta samannäköistä polkua.")
        print("Tarvitset kartan oikean polun löytämiseen.")

    elif paikka == "silta":
        print("Pieni silta johtaa kylään vievälle tielle.")
        print("Sillan kansi on ehjä, mutta köysikaide on irronnut.")
        print("Uudella köydellä voit kiinnittää kaiteen.")

    elif paikka == "joki":
        print("Rannalla on pieni soutuvene.")
        print("Vene on ehjä, mutta sen istuinlauta puuttuu.")
        print("Tarvitset laudan ja melan päästäksesi vastarannalle.")
        print("Veneessä on valmiiksi pelastusliivit.")

    items = paikan_esineet(paikka)

    if len(items) > 0:
        print("\nNäet seuraavat esineet:")
        for item in items:
            print("- " + item)
    else:
        print("\nTäällä ei ole kerättäviä esineitä.")

    if paikka in roskat:
        print("Maassa on myös roskia.")
    elif paikka in siivotut_paikat:
        print("Olet jo kerännyt tämän paikan roskat.")

    print("\nVoit liikkua seuraaviin paikkoihin:")
    for reitti in mahdolliset_reitit(paikka):
        print("- " + reitti)


def liiku(paikka):
    reitit = mahdolliset_reitit(paikka)

    print("\nMinne haluat mennä?")
    for reitti in reitit:
        print("- " + reitti)

    kohde = input("Paikka tai takaisin: ").strip().lower()

    if kohde == "takaisin":
        return paikka

    if kohde in reitit:
        print(f"\nSiirryit paikkaan: {kohde}.")
        katso(kohde)
        return kohde

    print("Et pääse täältä suoraan tuohon paikkaan.")
    return paikka


def add_item(paikka):
    items = paikan_esineet(paikka)

    if len(items) == 0:
        print("\nTäällä ei ole kerättäviä esineitä.")
        return

    print("\nVoit ottaa:")
    for item in items:
        print("- " + item)

    item = input("Esine tai takaisin: ").strip().lower()

    if item == "takaisin":
        return

    if item in items:
        inventory.append(item)
        items.remove(item)
        print(f"Otit esineen: {item}.")
    elif item in inventory:
        print("Sinulla on jo tämä esine.")
    else:
        print("Tätä esinettä ei ole täällä.")


def show_inventory():
    print("\n--- TAVARALUETTELO ---")

    if len(inventory) == 0:
        print("Sinulla ei ole vielä esineitä.")
    else:
        for item in inventory:
            print("- " + item)

    print(f"Siivottuja paikkoja: {len(siivotut_paikat)}/3")


def siivoa(paikka):
    if paikka in siivotut_paikat:
        print("\nOlet jo siivonnut tämän paikan.")
    elif paikka not in roskat:
        print("\nTäällä ei ole kerättäviä roskia.")
    elif "roskapussi" not in inventory:
        print("\nTarvitset roskapussin. Sellainen löytyy leiristä.")
    else:
        roskat.remove(paikka)
        siivotut_paikat.append(paikka)
        print("\nKeräsit roskat pussiin.")
        print("Viet ne kylän jäteastiaan, kun pääset perille.")
        print(f"Siivottuja paikkoja: {len(siivotut_paikat)}/3")


def vahvista():
    vastaus = input("Haluatko jatkaa kylään? kyllä/ei: ").strip().lower()

    while vastaus not in ["kyllä", "ei"]:
        vastaus = input("Kirjoita kyllä tai ei: ").strip().lower()

    return vastaus == "kyllä"


def kayta(paikka):
    if paikka == "kukkula":
        if "kartta" not in inventory:
            print("\nTarvitset kartan. Etsi sitä huoltomajasta.")
        else:
            print("\nLöydät kartasta turvallisen polun kylään.")
            if vahvista():
                return "metsäpolku"

    elif paikka == "silta":
        if "köysi" not in inventory:
            print("\nTarvitset köyden kaiteen korjaamiseen.")
        else:
            print("\nKiinnität sillan kaiteen köydellä.")
            print("Silta on valmis ylittämistä varten.")
            if vahvista():
                return "silta"

    elif paikka == "joki":
        if "lauta" in inventory and "mela" in inventory:
            print("\nAsetat laudan veneen istuimeksi.")
            print("Puet pelastusliivit ja otat melan.")
            if vahvista():
                return "vene"
        else:
            print("\nEt ole vielä valmis lähtemään veneellä.")
            if "lauta" not in inventory:
                print("Tarvitset laudan. Etsi sitä metsästä.")
            if "mela" not in inventory:
                print("Tarvitset melan. Katso ympärillesi rannalla.")

    else:
        print("\nTäällä ei ole avattavaa poistumisreittiä.")
        print("Esineistä voi olla hyötyä kukkulalla, sillalla tai joella.")

    return ""


def lopetus(reitti, name):
    print(f"\nOnneksi olkoon, {name}!")
    print("Pääsit turvallisesti kylään.")

    if reitti == "metsäpolku":
        print("Seurasit karttaa ja löysit vanhan metsäpolun.")
        print("Kylän opastaulu näkyi pian puiden välissä.")
    elif reitti == "silta":
        print("Ylitit korjatun sillan ja saavuit kylätielle.")
        print("Korjaamastasi kaiteesta on hyötyä muillekin.")
    elif reitti == "vene":
        print("Ylitit joen veneellä ja saavuit kylän laituriin.")
        print("Jätit veneen ja melan seuraavaa käyttäjää varten.")

    if len(siivotut_paikat) == 3:
        print("\nLuonnon ystävä!")
        print("Keräsit roskat kaikista kolmesta paikasta.")
    elif len(siivotut_paikat) > 0:
        print(f"\nSiivosit matkan aikana {len(siivotut_paikat)} paikkaa.")
    else:
        print("\nSeuraavalla kerralla voit myös kerätä roskia.")

    if len(siivotut_paikat) > 0:
        print("Viet keräämäsi roskat kylän jäteastiaan.")

    print("Kiitos pelaamisesta!")


name = input("Anna nimesi: ").strip()

while name == "":
    name = input("Kirjoita nimesi: ").strip()

age_text = input("Anna ikäsi: ").strip()

while not age_text.isdecimal() or len(age_text) > 3:
    age_text = input("Anna ikä kokonaislukuna: ").strip()

age = int(age_text)

if age < 12:
    print("Olet liian nuori pelaamaan tätä peliä.")
else:
    print(f"\nTervetuloa peliin, {name}!")
    print("Olet ollut retkellä, mutta myrsky on sulkenut päätien.")
    print("Puhelimestasi on loppunut akku.")
    print("Löydä toinen reitti takaisin kylään.")

    paikka = "leiri"
    voitto_reitti = ""
    command = ""

    katso(paikka)
    apua()

    while command != "lopeta" and voitto_reitti == "":
        main_menu()
        command = input("\nAnna komento: ").strip().lower()

        if command == "katso":
            katso(paikka)
        elif command == "liiku":
            paikka = liiku(paikka)
        elif command == "ota":
            add_item(paikka)
        elif command == "tavarat":
            show_inventory()
        elif command == "käytä":
            voitto_reitti = kayta(paikka)
        elif command == "siivoa":
            siivoa(paikka)
        elif command == "apua":
            apua()
        elif command == "lopeta":
            print("Lopetit pelin. Näkemiin!")
        else:
            print("Tuntematon komento. Katso valikon vaihtoehdot.")

    if voitto_reitti != "":
        lopetus(voitto_reitti, name)