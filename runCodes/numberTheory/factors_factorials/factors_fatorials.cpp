#include<math.h>
#include<stdio.h>
#include<map>
#include<set>

using namespace std;


void prime_factorization(map <unsigned int, unsigned char> &m, unsigned int x){
	unsigned int i;
	unsigned int c;
	double src;

	c = x;

	while ((c % 2) == 0){
		m[2]++;
		c /= 2;
	}

	i = 3;
	src = sqrt(c)+1;
	while (i <= src){
		if ((c % i) == 0){
			m[i]++;
			c /= i;
			src = sqrt(c)+1;
		}
		else
			i += 2;
	}
	if (c > 1){
		m[c]++;
	}
}


void print_factors(unsigned int n, map <unsigned int, unsigned char> &d){
	map <unsigned int, unsigned char>::iterator it;

	printf("%u! =", n);
	for(it=d.begin(); it != d.end(); it++)
		printf(" %u", it->second);

	printf("\n");
}


int main(int argc, char const *argv[])
{

	map <unsigned int, unsigned char> d;
	set <unsigned int> p;
	unsigned n;

	scanf("%u", &n);
	while(n != 0){
		d.clear();
		for (unsigned int i = 2; i <= n; i++)
			prime_factorization(d, i);

		print_factors(n, d);

		scanf("%u", &n);
	}
	return 0;
}
