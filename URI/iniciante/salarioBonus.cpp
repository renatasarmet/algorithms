// https://www.urionlinejudge.com.br/judge/pt/problems/view/1009

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    string nome;
    double salfix, vendas, com, total;
    cin >> nome >> salfix >> vendas;
    com = 0.15 * vendas;
    total = salfix + com;
    cout << setiosflags (ios::fixed) << setprecision(2) << "TOTAL = R$ " << total << endl;

 return 0;
}
