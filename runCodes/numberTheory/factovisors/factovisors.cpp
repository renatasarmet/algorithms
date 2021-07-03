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



int is_divisor(map <unsigned int, unsigned char> &d, unsigned int n){

	unsigned int i, aux;
	unsigned long term;

	map <unsigned int, unsigned char>::reverse_iterator it;

	for(it=d.rbegin(); it != d.rend(); it++){
		i = 0;
		term = it->first;
		printf("it->first = %u ****** it->second = %u\n", it->first, it->second);
		while((i < it->second) && (term <= n)){
			aux = term;
			while((aux > 0) && (aux % it->first == 0)){
				aux /= it->first;
				i++;
			}
			term += it->first;
		}
		if(i < it->second)
			return 0;
	}
	return 1;
}



int main(int argc, char const *argv[])
{

	map <unsigned int, unsigned char> d;
	unsigned m, n;

	while(scanf("%u", &n) != EOF){
		scanf("%u", &m);
		if(m == 0)
			printf("%u does not divide %u!\n", m, n);
		else {
			if (m <= n)
				printf("%u divides %u!\n", m, n);
			else{
				d.clear();
				prime_factorization(d, m);
				if(is_divisor(d, n))
					printf("%u divides %u!\n", m, n);
				else
					printf("%u does not divide %u!\n", m, n);
			}
		}
	}
	return 0;
}
