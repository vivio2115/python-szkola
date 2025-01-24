import requests


def kantor():
    print("Kantor walut - przelicz waluty")
    print("Dostępne waluty: USD, EUR, PLN, GBP etc.")
    waluta_z = input("Podaj walutę, z której chcesz przeliczyć (np. USD): ").upper()
    waluta_do = input("Podaj walutę, na którą chcesz przeliczyć (np. EUR): ").upper()
    kwota = float(input("Podaj kwotę do przeliczenia: "))

    url = "https://open.er-api.com/v6/latest/" + waluta_z

    odpowiedz = requests.get(url)

    if odpowiedz.status_code == 200:
        dane = odpowiedz.json()
        if waluta_do in dane["rates"]:
            kurs = dane["rates"][waluta_do]
            wynik = kwota * kurs
            print(f"{kwota} {waluta_z} to {wynik:.2f} {waluta_do}. Kurs: {kurs:.2f}")
        else:
            print("Wybrana waluta docelowa nie jest obsługiwana.")
    else:
        print("Nie udało się pobrać danych dla podanej waluty.")


kantor()

# pip install requests