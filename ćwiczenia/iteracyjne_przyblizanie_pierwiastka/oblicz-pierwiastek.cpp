#include <iostream>

float pierwiastek(float x, int ilosc_wyrazow = 100, float start = 1.0) {
    float y0 = start;
    float y1;
    for (int i = 0; i < ilosc_wyrazow; i++) {
        y1 = 0.5 * (y0 + (x / y0));
        if (y0 == y1)
            break;
        y0 = y1;
    }
    return y1;
}

int main() {

    float liczba = 3.0;
    for (int i = 0; i < 20; i++) {
        printf("%d.sqrt(%f) = %.8f\n", i, liczba, pierwiastek(liczba, i, 1000.0F));
    }

    return 0;
}