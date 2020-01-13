# NUM7

Wyszukiwanie wielomianów interpolacyjnych Lagrange'a.

## Kompilacja i uruchamianie

Do uruchomienia potrzebny jest numpy oraz scipy.
Do tworzenia wykresów dodatkowo potrzebny jest matplotlib.

Na początku pliku ustawiana jest wartość N. Aby znaleźć splajny o większej
dokładności należy zwiększyć tę wartość.

## Wyświetlanie wykresów zamiast zapisu

Aby zamiast zapisywać wykres do pliku `.pgf` wyświetlić go za pomocą matplotlib
wystarczy za-/odkomentować zaznaczone przy pomocy `#!` linijki.
Np.

Domyślnie program zapisuje wykres do pliku w formacie `.pgf`. Aby wyświetlić
wykres od razu należy odkomentować linię jak poniżej

```Python
    # plt.show()
    filename = '_'.join(['spline', 'N', str(N)])
    plt.savefig(filename + '.pgf')
```

należy zmienić na

```Python
    plt.show()
    # filename = '_'.join(['spline', 'N', str(N)])
    # plt.savefig(filename + '.pgf')
```
