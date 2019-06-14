// https://www.urionlinejudge.com.br/judge/pt/problems/view/1002

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double raio, pi = 3.14159, area;
    cin >> raio;
    area = raio*raio * pi;
    cout << "A=" << setiosflags (ios::fixed) << setprecision(4) << area << endl;
 return 0;
}
