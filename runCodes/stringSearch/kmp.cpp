#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <string.h>

#define TAM 260010

using namespace std;


void kmpPreProcess(int *b, char *pat, int tam_pat){
	int i = 0, j = -1; b[0] = -1;

	while (i < tam_pat){
		while (j>=0 && pat[i] != pat[j]) { // eh diferente... Reseta j, usando b .
			j = b[j]; 
			//cout << "pat[i] = " << pat[i] << " pat[j] = "<< pat[j] << " j eh diferente = " << j << endl;
		}
			//j = -1;    
		i++; j++;
		b[i] = j;     // observe que b[i] so deixa de ser zero quando o padrao se repetir em pattern!
	}
}

void kpmSearch(int *b, char *pat, char *text, int tam_pat, int tam_t){
	int i = 0, j = 0;
	while (i < tam_t){     // tem texto para  consumir.....
		while (j >= 0 &&  text[i] != pat[j]) {
			j = b[j];
			//cout << "opa... j = b[j] " << j << " i = " << i << endl;
		}
		i++; j++;
		if (j == tam_pat) { // opa... teve matching !!!
			cout << "O padrao foi encontrado na posicao " << i - j << endl;
			j = b[j];        // prepara j para um provavel matching novo....
		}
	}
}

int main(){
	char text[TAM],pattern[1000];
	int b[1001];

	fgets(text, TAM, stdin);
	fgets(pattern, 1000, stdin);

	text[strlen(text)-1] = '\0';
	pattern[strlen(pattern)-1] = '\0';


	//cout << text << endl;
	//cout << pattern << endl;

	// busca pattern string na string

	int tam_t = strlen(text);
	int tam_pat = strlen(pattern);

	kmpPreProcess(b, pattern, tam_pat);  //para calcular o vetor de borda !!!

	// for (int i=0; i<=tam_pat+1; i++)
	// 	cout << b[i] << " ";
	// cout << endl;

	kpmSearch(b, pattern, text, tam_pat, tam_t);
}