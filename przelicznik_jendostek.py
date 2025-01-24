def przelicz_jednostki():
    print("Przelicznik jednostek")
    print("Dostępne jednostki: cm, m, km, mm, mile, cale, stopy, jardy, kg, g, mg")
    jednostka = input("Podaj jednostkę wyjściową (np. cm): ").lower()
    wartosc = float(input("Podaj wartość do przeliczenia: "))

    if jednostka == "cm":
        print(f"{wartosc} cm to:")
        print(f"{wartosc * 10} mm")
        print(f"{wartosc / 100} m")
        print(f"{wartosc / 100000} km")
        print(f"{wartosc / 100000} mil")
        print(f"{wartosc / 2.54} cali")
        print(f"{wartosc / 30.48} stóp")
        print(f"{wartosc / 91.44} jardów")
    elif jednostka == "m":
        print(f"{wartosc} m to:")
        print(f"{wartosc * 100} cm")
        print(f"{wartosc * 1000} mm")
        print(f"{wartosc / 1000} km")
        print(f"{wartosc / 1609.34} mil")
        print(f"{wartosc * 39.37} cali")
        print(f"{wartosc * 3.281} stóp")
        print(f"{wartosc * 1.094} jardów")
    elif jednostka == "km":
        print(f"{wartosc} km to:")
        print(f"{wartosc * 1000000} mm")
        print(f"{wartosc * 100000} cm")
        print(f"{wartosc * 1000} m")
        print(f"{wartosc / 1.609} mil")
    elif jednostka == "mm":
        print(f"{wartosc} mm to:")
        print(f"{wartosc / 10} cm")
        print(f"{wartosc / 1000} m")
        print(f"{wartosc / 1000000} km")
    elif jednostka == "mile":
        print(f"{wartosc} mil to:")
        print(f"{wartosc * 1609.34} m")
        print(f"{wartosc * 1.609} km")
        print(f"{wartosc * 160934} cm")
    elif jednostka == "cale":  # 1 cal = 2.54 cm
        print(f"{wartosc} cali to:")
        print(f"{wartosc * 2.54} cm")
        print(f"{wartosc / 12} stóp")
        print(f"{wartosc / 36} jardów")
    elif jednostka == "stopy":  # 1 stopa = 30.48 cm
        print(f"{wartosc} stóp to:")
        print(f"{wartosc * 30.48} cm")
        print(f"{wartosc / 3} jardów")
    elif jednostka == "jardy":  # 1 jard = 91.44 cm
        print(f"{wartosc} jardów to:")
        print(f"{wartosc * 91.44} cm")
        print(f"{wartosc * 3} stóp")
    elif jednostka == "kg":  # masa
        print(f"{wartosc} kg to:")
        print(f"{wartosc * 1000} g")
        print(f"{wartosc * 1000000} mg")
    elif jednostka == "g":
        print(f"{wartosc} g to:")
        print(f"{wartosc / 1000} kg")
        print(f"{wartosc * 1000} mg")
    elif jednostka == "mg":
        print(f"{wartosc} mg to:")
        print(f"{wartosc / 1000} g")
        print(f"{wartosc / 1000000} kg")
    else:
        print("Nieznana jednostka. Spróbuj ponownie.")


przelicz_jednostki()
