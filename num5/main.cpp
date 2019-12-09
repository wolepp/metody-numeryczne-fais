#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <array>

const int N = 100;
const int ITERATION_LIMIT = 10000;
const double PRECISION = 10e-12;

const char * FILENAME_JACOBI = "jacobi.data";
const char * FILENAME_GAUSS_SEIDEL = "gauss-seidel.data";

using std::array;

double a(int i, int j) {
    if (i == j) return 3.0;
    if (std::abs(i - j) == 1) return 1.0;
    if (std::abs(i - j) == 2) return 0.2;
    return 0.0;
}

double b(int i) {
    return double(i+1);
}

bool is_converged(array<double, N> a, array<double, N> b, double precision) {
    for (int i = 0; i < N; i++) {
        if (std::fabs(a[i] - b[i]) > precision) return false;
    }
    return true;
}

int main() {

    /* TODO:
    * zapisywać do pliku z większą precyzją! sprintf?
    */

    // Jacobi
    array<double, N> x = {0};
    array<double, N> x_new = {0};
    std::ofstream outfile;
    outfile.open(FILENAME_JACOBI, std::ios::trunc);
    for (int iteration = 0; iteration < ITERATION_LIMIT; iteration++) {
        x_new[0] = 1/a(0, 0) * (b(0) - a(0, 1)*x[1] - a(0, 2)*x[2]);
        x_new[1] = 1/a(1, 1) * (b(1) - a(1, 0)*x[0] - a(1, 2)*x[2] - a(1, 3)*x[3]);
        for (int i = 2; i < N-2; i++) {
            double s1 = a(i, i-2)*x[i-2] + a(i, i-1)*x[i-1];
            double s2 = a(i, i+1)*x[i+1] + a(i, i+2)*x[i+2];
            x_new[i] = 1/a(i, i) * (b(i) - s1 - s2);
        }
        x_new[N-2] = 1/a(N-2, N-2) * (b(N-2) - a(N-2, N-4)*x[N-4] - a(N-2, N-3)*x[N-3] - a(N-2, N-1)*x[N-1]);
        x_new[N-1] = 1/a(N-1, N-1) * (b(N-1) - a(N-1, N-3)*x[N-3] - a(N-1, N-2)*x[N-2]);

        // Zapisanie wartości x z danej iteracji do jednej linijki, wartości oddzielone spacją.
        for (double xi: x_new) {
            outfile << xi << ' ';
        }
        outfile << std::endl;

        if (is_converged(x_new, x, PRECISION)) break;

        x = x_new;
    }
    outfile.close();

    // Gauss-Seidel
    x = {0};
    outfile.open(FILENAME_GAUSS_SEIDEL, std::ios::trunc);
    for (int iteration = 0; iteration < ITERATION_LIMIT; iteration++) {
        array<double, N> x_old = x;
        x[0] = 1/a(0, 0) * (b(0) - a(0, 1)*x[1] - a(0, 2)*x[2]);
        x[1] = 1/a(1, 1) * (b(1) - a(1, 0)*x[0] - a(1, 2)*x[2] - a(1, 3)*x[3]);
        for (int i = 2; i < N-2; i++) {
            double s1 = a(i, i-2)*x[i-2] + a(i, i-1)*x[i-1];
            double s2 = a(i, i+1)*x[i+1] + a(i, i+2)*x[i+2];
            x[i] = 1/a(i, i) * (b(i) - s1 - s2);
        }
        x[N-2] = 1/a(N-2, N-2) * (b(N-2) - a(N-2, N-4)*x[N-4] - a(N-2, N-3)*x[N-3] - a(N-2, N-1)*x[N-1]);
        x[N-1] = 1/a(N-1, N-1) * (b(N-1) - a(N-1, N-3)*x[N-3] - a(N-1, N-2)*x[N-2]);

        // Zapisanie wartości x z danej iteracji do jednej linijki, wartości oddzielone spacją.
        for (double xi: x) {
            outfile << xi << ' ';
        }
        outfile << std::endl;

        if (is_converged(x, x_old, PRECISION)) break;
    }
    outfile.close();


    return 0;
}