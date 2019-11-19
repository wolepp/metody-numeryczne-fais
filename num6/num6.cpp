#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

double y(double x) {
    return 1. / (1. + 25. * (x * x));
}

double y_prim(double x) {
    return 1. / (1. + (x * x));
}

vector<double> xn_jednorodne(int n) {
    vector<double> xs;
    for (int i = 0; i < n; i++) {
        xs.push_back(-1. + ((2.*i) / (n+1.)));
    }
    return xs;
}

vector<double> xn_cos(int n){
    vector<double> xs;
    for (int i = 0; i < n; i++) {
        xs.push_back(cos( ((2.*i+1.) / (2.*(n+1.))) * M_PI ));
    }
    return xs;
}

int main() {

    vector<double> x10 = xn_jednorodne(10);
    vector<double> x20 = xn_jednorodne(20);
    vector<double> x40 = xn_jednorodne(40);
    vector<double> x80 = xn_jednorodne(80);
    vector<double> x160 = xn_jednorodne(160);
    vector<double> x320 = xn_jednorodne(320);
    
    vector<double> x10_cos = xn_cos(10);
    vector<double> x20_cos = xn_cos(20);
    vector<double> x40_cos = xn_cos(40);
    vector<double> x80_cos = xn_cos(80);
    vector<double> x160_cos = xn_cos(160);
    vector<double> x320_cos = xn_cos(320);

    return 0;
}