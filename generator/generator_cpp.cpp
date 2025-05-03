#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>

int main() {
    std::ofstream fout("sequence_cpp.txt");
    srand(time(0));
    for (int i = 0; i < 1000000; ++i) {
        int bit = rand() % 2;
        fout << bit;
    }
    fout.close();
    return 0;
}