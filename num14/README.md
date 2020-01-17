# NUM14

Wyznaczanie wartości własnych macierzy algorytmem QR i metodą potęgową.

## Uruchamianie

Uruchamianie z poziomu terminala uruchomionego w folderze z NUM14.py:

```bash
python3 NUM14.py
```

Wyniki działania programu wyświetlają się na ekranie terminala.

## Zmiana dokładności obliczeń

W 6. i 7. linii kodu NUM14 zdefiniowane są wielkości `RTOL` i `ATOL`
Odpowiadają one za określenie czy dwa wektory są wystarczająco zbliżone.
Wektory a i b porównywane są jak poniżej (każdy z odpowiadających sobie
elementów osobno):
absolute(a - b) <= (ATOL + RTOL * absolute(b))
