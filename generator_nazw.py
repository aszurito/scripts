import random
import string
import os

NAZWA_PLIKU = "nazwy_uzytkownikow.txt"
DLUGOSC_LOSOWEJ_CZESCI = 6
prefiks = "ab"  # ← tutaj wpisz swój prefiks (2 znaki)
ilosc_do_wygenerowania = 10  # ← ile nazw chcesz wygenerować

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
    if len(prefiks) != 2 or not prefiks.isalnum():
        print("Prefiks musi mieć dokładnie dwa znaki (litery lub cyfry).")
        return

    istniejace = wczytaj_istniejace_nazwy()

    for _ in range(ilosc_do_wygenerowania):
        nowa_nazwa = wygeneruj_nazwe(prefiks, istniejace)
        zapisz_nazwe(nowa_nazwa)
        istniejace.add(nowa_nazwa)
        print("Wygenerowano:", nowa_nazwa)

if __name__ == "__main__":
    main()
