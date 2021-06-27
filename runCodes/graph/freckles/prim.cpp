#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <math.h>


using namespace std;

// par de inteiro e double: guarda o vertice v e o peso da aresta
typedef pair<int,double> id;

// par de double e inteiro: guarda o peso da aresta e o vertice v
typedef pair<double,int> di;

// par de double: guarda as coordenadas dos pontos
typedef pair<double,double> dd;

// todos os vertices v adjacentes a u 
typedef vector<id> vid;

// todos os pontos
typedef vector<dd> vdd;


typedef vector<int> vi;

int V; 
vi visitado;

// void printAdjList(int nv, vector<vid> AdjList){
// 	for (int u = 0; u < nv; ++u){ // para todo vertice u
// 		printf("%d -> ", u);
// 		for (int i = 0; i < (int)AdjList[u].size(); ++i) { // para todo adjacente v de u
// 			id v = AdjList[u][i];
// 			printf("(%d, %f) -> ", v.first, v.second);
// 		}
// 		printf("\n");
// 	}
// }

// void printPoints(int nv, vdd points){
// 	for (int u = 0; u < nv; ++u){ // para todo vertice u
// 		printf("%d -> ", u);

// 		printf("(%f, %f)", points[u].first, points[u].second);
// 		printf("\n");
// 	}
// }

void process(int u, priority_queue<di> &pq, vector<vid> AdjList){
	visitado[u] = 1;
	// para todo v adjacente a u
	for (int i = 0; i < (int)AdjList[u].size(); ++i){
		id v = AdjList[u][i];
		if (!visitado[v.first]){
			// lembre-se de que PQ em C++ é MAX HEAP
			pq.push(make_pair(-v.second, -v.first));
		}
	}

}

int  main(int argc, char const *argv[])
{
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i){

		// lista de adjacencia para todo vertice u do meu grafo..
		vector<vid> AdjList(100);

		vdd points;

		cin >> V;
		double x, y; 

		// le as coordenadas de cada vertice
		for (int i = 0; i < V; ++i){
			cin >> x >> y;
			points.push_back(make_pair(x, y));
		}

		// printPoints(V, points);

		// cria a lista de arestas, o peso é o list.first ( iremos calculá-lo)
		for (int u = 0; u < V; ++u){
			for (int v = u+1; v < V; ++v){
				// calcula a distancia entre os dois pontos
				double w = sqrt(pow(abs(points[u].first - points[v].first), 2) + pow(abs(points[u].second - points[v].second), 2));

				// salva na lista de arestas
				AdjList[u].push_back(make_pair(v, w));
				AdjList[v].push_back(make_pair(u, w));
			}
		}

		// printAdjList(V, AdjList);

		double custo = 0;

		priority_queue<di> pq;

		visitado.assign(V,0);
		process(0, pq, AdjList);  // comece por um vertice arbitrario do grafo

		while(!pq.empty()){
			di el = pq.top(); pq.pop();
			
			// printf("(%f,%d) *** ", el.first, el.second);
			double w = -el.first;
			int u = -el.second;

			// evite ciclos...
			if (!visitado[u]){
				custo+= w; // atualiza o custo
				process(u, pq, AdjList);
			}
		}

		printf("%.2f\n", custo);

		if (i < n-1)
			printf("\n");
	}

	return 0;
}