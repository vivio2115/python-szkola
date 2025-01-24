def wyjasnij_vat():
    print("\n### Co to jest VAT? ###")
    print("VAT (Podatek od wartości dodanej) to podatek doliczany do towarów i usług.")
    print("Cena brutto: zawiera VAT.")
    print("Cena netto: to cena bez VAT.")
    print("W Polsce podstawowa stawka VAT wynosi 23%.\n")


def oblicz_netto_na_brutto():
    netto = float(input("Podaj cenę netto: "))
    vat = float(input("Podaj stawkę VAT (np. 23): "))
    brutto = netto * (1 + vat / 100)
    print(f"Cena netto: {netto} zł przy stawce VAT {vat}% daje cenę brutto: {brutto:.2f} zł.")


def oblicz_brutto_na_netto():
    brutto = float(input("Podaj cenę brutto: "))
    vat = float(input("Podaj stawkę VAT (np. 23): "))
    netto = brutto / (1 + vat / 100)
    print(f"Cena brutto: {brutto} zł przy stawce VAT {vat}% daje cenę netto: {netto:.2f} zł.")


def main():
    print("Program do obliczania cen netto i brutto oraz wyjaśnienia VAT")
    while True:
        print("\nWybierz opcję:")
        print("1. Wyjaśnienie, czym jest VAT")
        print("2. Oblicz z ceny netto cenę brutto")
        print("3. Oblicz z ceny brutto cenę netto")
        print("4. Wyjście z programu")

        wybor = input("Twój wybór: ")

        if wybor == "1":
            wyjasnij_vat()
        elif wybor == "2":
            oblicz_netto_na_brutto()
        elif wybor == "3":
            oblicz_brutto_na_netto()
        elif wybor == "4":
            print("Do zobaczenia!")
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")


main()
