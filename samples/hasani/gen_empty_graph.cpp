#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
    srand(stoi(argv[argc-1]));
    long int n = rand()%(99997)+3;;
    cout << n << ' ' << 0 << '\n';
}