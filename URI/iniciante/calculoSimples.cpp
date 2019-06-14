// https://www.urionlinejudge.com.br/judge/pt/problems/view/1010

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int cod1, n1, cod2, n2;
    double v1, v2, total;
    cin >> cod1 >> n1 >> v1;
    cin >> cod2 >> n2 >> v2;
    total = n1 * v1 + n2 * v2;
    cout << setiosflags (ios::fixed) << setprecision(2) << "VALOR A PAGAR: R$ " << total << endl;

 return 0;
}