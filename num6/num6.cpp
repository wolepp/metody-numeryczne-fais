#include <iostream>
#include <cmath>
#include <vector>
#include <map>

int ILOSC_WEZLOW = 1024;

using namespace std;

double y(double x) {
    return 1. / (1. + 25. * (x * x));
}

double y_prim(double x) {
    return 1. / (1. + (x * x));
}

vector<double> xn_jednorodne(int n) {
    vector<double> xs;
    for (int i = 0; i <= n; i++) {
        xs.push_back(-1. + ((2.*i) / (n+1.)));
    }
    return xs;
}

vector<double> xn_cos(int n){
    vector<double> xs;
    for (int i = 0; i <= n; i++) {
        xs.push_back(cos( ((2.*i+1.) / (2.*(n+1.))) * M_PI ));
    }
    return xs;
}

int main() {

    // Wygenerować jednorodne węzły interpolacji oraz te z cosinusem, np. 1024
    vector<double> x_jednorodne = xn_jednorodne(ILOSC_WEZLOW);
    vector<double> x_cosinus = xn_cos(ILOSC_WEZLOW);

    // Dla tych węzłów obliczyć dokładny wynik funkcji y oraz y_prim
    vector<double> y_jednorodne;
    vector<double> y_cosinus;
    vector<double> y_prim_jednorodne;
    vector<double> y_prim_cosinus;

    for (double x: x_jednorodne) {
        y_jednorodne.push_back(y(x));
        y_prim_jednorodne.push_back(y_prim(x));
    }
    for (double x: x_cosinus) {
        y_cosinus.push_back(y(x));
        y_prim_cosinus.push_back(y_prim(x));
    }

    // Znaleźć wielomiany różnych stopni, np. 4, 6, 8, 10, 16, 32, ..., 1024
    // a następnie je wykreślić - skoro wykreślić to znaleźć ich wartości w wielu
    // punktach?

    return 0;
}