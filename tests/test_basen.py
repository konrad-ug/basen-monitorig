from monitor import decyzja, sprawdz_basen


def test_duzy_basen_jest_w_normie():
    wynik = sprawdz_basen("duzy")
    assert wynik["akcja"] == "OK"


def test_dzieciecy_basen_jest_w_normie():
    wynik = sprawdz_basen("dzieciecy")
    assert wynik["akcja"] == "OK"
    
    
# TODO (Twoje zadanie): dopisz analogiczne testy dla pozostałych basenów:
#   - jacuzzi (w normie, akcja "OK")
#   - zimny (jest za ciepły, więc oczekiwana akcja to "SCHLODZ")


def test_decyzja_temperatura_w_normie():
    # norma 26-28 °C
    assert decyzja(27, 26, 28) == "OK"


def test_decyzja_za_zimno_trzeba_podgrzac():
    assert decyzja(24, 26, 28) == "PODGRZEJ"


def test_decyzja_za_cieplo_trzeba_schlodzic():
    assert decyzja(30, 26, 28) == "SCHLODZ"



