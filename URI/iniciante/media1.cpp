// https://www.urionlinejudge.com.br/judge/pt/problems/view/1005

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double A, B, MEDIA;
    cin >> A >> B;
    MEDIA = ((3.5 * A) + (7.5 * B))/11;
    cout << setiosflags (ios::fixed) << setprecision(5) << "MEDIA = " << MEDIA << endl;
 return 0;
}