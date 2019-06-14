// https://www.urionlinejudge.com.br/judge/pt/problems/view/1006

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double A, B, C, MEDIA;
    cin >> A >> B >> C;
    MEDIA = ((2 * A) + (3 * B) + (5 * C))/10;
    cout << setiosflags (ios::fixed) << setprecision(1) << "MEDIA = " << MEDIA << endl;
 return 0;
}