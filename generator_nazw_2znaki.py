import random
import string
import os

NAZWA_PLIKU = "nazwy_uzytkownikow.txt"
DLUGOSC_LOSOWEJ_CZESCI = 6

def wczytaj_istniejace_nazwy():
    if not os.path.exists(NAZWA_PLIKU):
        return set()
    with open(NAZWA_PLIKU, "r") as f:
        return set(line.strip() for line in f if line.strip())

def zapisz_nazwe(nazwa):
    with open(NAZWA_PLIKU, "a") as f:
        f.write(nazwa + "\n")

def wygeneruj_nazwe(poczatek, istniejace_nazwy):
    znaki = string.ascii_lowercase + string.digits
    while True:
        losowa_czesc = ''.join(random.choices(znaki, k=DLUGOSC_LOSOWEJ_CZESCI))
        nazwa = poczatek + losowa_czesc
        if nazwa not in istniejace_nazwy:
            return nazwa

def main():
    poczatek = input("Podaj pierwsze dwa znaki nazwy użytkownika (np. 'ab'): ").strip().lower()
    if len(poczatek) != 2 or not poczatek.isalnum():
        print("Podaj dokładnie dwa znaki (litery lub cyfry).")
        return

    ilosc = int(input("Ile nazw chcesz wygenerować? "))
    istniejace = wczytaj_istniejace_nazwy()
    
    for _ in range(ilosc):
        nowa_nazwa = wygeneruj_nazwe(poczatek, istniejace)
        zapisz_nazwe(nowa_nazwa)
        istniejace.add(nowa_nazwa)
        print("Wygenerowano:", nowa_nazwa)

if __name__ == "__main__":
    main()
