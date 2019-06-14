// https://www.urionlinejudge.com.br/judge/pt/problems/view/1008

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int f, h;
    double v, salario;
    cin >> f >> h >> v;
    salario = h * v;
    cout << "NUMBER = " << f << endl;
    cout << setiosflags (ios::fixed) << setprecision(2) << "SALARY = U$ " << salario << endl;

 return 0;
}