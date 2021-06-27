#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

#define INF 1000000

// estruturas uteis para representacao de grafos...
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

int main(){
	
	int N; // nro de casos de teste
	int A;  // nro de Arestas
	int V; // nro de Vertices
	int u,v,w;
	int s; // vertice source....   
	int t;  // vertice target...
 
	scanf("%d", &N);

	for (int n=0; n<N; n++) { 
		vector<vii> adjList(100);    // uma lista de adjacencia: para cada vertice v, tem-se um conjunto de tuplas (u,w)

		scanf("%d %d %d %d", &V, &A, &s, &t);


		for (int i=0; i<A; i++) {
			scanf("%d %d %d", &u, &v, &w);
			adjList[u].push_back(make_pair(v,w));
			adjList[v].push_back(make_pair(u,w));
		}

		// o vetor de distancia a partir de um vertice quqlquer tem inicialmente distancia INFINITA
		vi dist(V, INF); 
		vi parent(V);   // grava a trilha, guardando o pai  de cada vertice..

		dist[s] = 0;  // a distancia de s para s eh zero !!!

		// percorra a lista de adjacencia V-1 vezes...
		// Vimos que para um grafo sem ciclos negativos, o caminho mínimo 
		// só é conseguido se itermos V-1 vezes !!!!!!!
		// se ao iterarmos mais, houver mais relaxamento, então o grafo tem ciclo negativo!
		for (int i=0; i< V-1; i++)               // Ordem (V)
			// agora visite todas as arestas...
			for (int u=0; u< V; u++)                    // para todas as arestas (E)
				// para todos os adjacentes de u
				for(int j=0; j<(int)adjList[u].size(); j++){
					ii v = adjList[u][j];
					if (dist[u] + v.second < dist[v.first]){
						dist[v.first] = dist[u]+ v.second; //vai acumulando a distancia..
						parent[v.first] = u;
					}
				}

		if(dist[t]== INF)
			printf("Case #%d: unreachable\n", n+1);
		else printf("Case #%d: %d\n", n+1, dist[t]);
	}
	
	return 0;
}