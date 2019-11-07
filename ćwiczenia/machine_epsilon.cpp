#include <iostream>

float machine_epsilon() {
    float eps = 0.0;
    float tmp = 0.0;
    while (tmp) {
        eps = tmp;
        tmp = tmp / 2;
    }
    return eps;
}

int main() {

}