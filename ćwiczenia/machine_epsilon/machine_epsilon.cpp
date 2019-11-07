#include <iostream>

float float_machine_epsilon(float n) {
    float eps;
    while (n) {
        eps = n;
        n = n / 2;
    }
    return eps;
}

double double_machine_epsilon(double n) {
    double eps;
    while (n) {
        eps = n;
        n = n / 2;
    }
    return eps;
}


int main() {

    std::cout << "float: " << float_machine_epsilon(1) << std::endl;
    std::cout << "double " << double_machine_epsilon(1) << std::endl;

    return 0;
}