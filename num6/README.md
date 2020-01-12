# NUM6

Wyszukiwanie wielomianów interpolacyjnych Lagrange'a.

## Kompilacja i uruchamianie

Do uruchomienia potrzebny jest matplotlib oraz numpy.

W części `__main__` można zmienić zestawy N na jeden wykres, można zmienić
funkcje, dla których liczone są znane wartości punktów oraz same funkcje,
które zwracają listy z węzłami.

## Wyświetlanie wykresów zamiast zapisu

Aby zamiast zapisywać wykres do pliku `.pgf` wyświetlić go za pomocą matplotlib
wystarczy za-/odkomentować zaznaczone przy pomocy `#!` linijki.
Np.

```Python
    #!
        filename = 'plots/' + '_'.join(
            ['plot', fw.str, f.str, 'nr', str(nr_zestawu+1)])
        plt.savefig(filename + '.pgf')
        plt.clf()
    #!  
        #! plt.show()
```

należy zmienić na

```Python
    #!
        # filename = 'plots/' + '_'.join(
            # ['plot', fw.str, f.str, 'nr', str(nr_zestawu+1)])
        # plt.savefig(filename + '.pgf')
        # plt.clf()
    #!  
        plt.show()
```
