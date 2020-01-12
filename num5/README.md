# NUM5

Rozwiązywanie układów równań metodami iteracyjnymi Jacobiego i Gaussa-Seidela.

## Kompilacja i uruchamianie

Polecenie `make run` kompiluje kod `main.cpp` z optymalizowaniem i uruchamia program `NUM5.out`. Wyniki kolejnych iteracji są zapisane do plików `gauss-seidel.csv` i `jacobi.csv`.

Kompilacja bez optymalizacji `-O2`: polecenie `make` a następnie `make run`.

### Wartości przybliżeń kolejnych iteracji

Wartości przybliżeń obliczane są w programie Mathematica w notebooku `NUM5.nb`. Do poprawnego działania potrzebne jest wcześniejsze uruchomienie `NUM5.out`.

Wyniki są zapisane do plików `przyblizenia-gauss.csv` i `przyblizenia-jacobi.csv`.

## Czyszczenie katalogu

Polecenie `make clean` czyści folder z plików *.csv, *.o i *.out
