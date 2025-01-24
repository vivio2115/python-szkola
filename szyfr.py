def wyjasnij_szyfrowanie():
    print("\n### Co to jest szyfr Cezara? ###")
    print("Szyfr Cezara to prosty sposób szyfrowania tekstu.")
    print("Każda litera w tekście jest zastępowana inną literą, znajdującą się o określoną")
    print("liczbę miejsc dalej w alfabecie. Na przykład:")
    print("Przy kluczu 3: 'A' → 'D', 'B' → 'E', itd.")
    print("Deszyfrowanie to proces odwrotny, w którym przesunięcie cofamy.\n")


def szyfruj_cezarem(tekst, klucz):
    szyfrogram = ""
    for znak in tekst:
        if znak.isalpha():
            if znak.isupper():
                szyfrogram += chr((ord(znak) - ord('A') + klucz) % 26 + ord('A'))
            else:
                szyfrogram += chr((ord(znak) - ord('a') + klucz) % 26 + ord('a'))
        else:
            szyfrogram += znak
    return szyfrogram


def deszyfruj_cezarem(szyfrogram, klucz):
    return szyfruj_cezarem(szyfrogram, -klucz)


def main():
    print("Program do szyfrowania tekstu - Szyfr Cezara")
    while True:
        print("\nWybierz opcję:")
        print("1. Wyjaśnij, czym jest szyfr Cezara")
        print("2. Szyfruj tekst")
        print("3. Deszyfruj tekst")
        print("4. Wyjście z programu")

        wybor = input("Twój wybór: ")

        if wybor == "1":
            wyjasnij_szyfrowanie()
        elif wybor == "2":
            tekst = input("Podaj tekst do zaszyfrowania: ")
            klucz = int(input("Podaj klucz (liczba całkowita): "))
            szyfrogram = szyfruj_cezarem(tekst, klucz)
            print(f"Zaszyfrowany tekst: {szyfrogram}")
        elif wybor == "3":
            szyfrogram = input("Podaj szyfrogram do odszyfrowania: ")
            klucz = int(input("Podaj klucz (liczba całkowita): "))
            odszyfrowany_tekst = deszyfruj_cezarem(szyfrogram, klucz)
            print(f"Odszyfrowany tekst: {odszyfrowany_tekst}")
        elif wybor == "4":
            print("Do zobaczenia!")
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")


main()
