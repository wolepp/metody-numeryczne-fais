#include <iostream>

float machine_epsilon() {
    float eps;
    float tmp = 1.0;
    while (tmp) {
        eps = tmp;
        tmp = tmp / 2;
    }
    return eps;
}

int main() {

    std::cout << machine_epsilon() << std::endl;

    return 0;
}