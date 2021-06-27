#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <queue>


#define SEMCOR -1

using namespace std;

// usando STL para representar grafos

// o par.first -> vértice u, par.second -> peso da aresta
typedef pair<int, int> ii;   

// um vetor de pares
typedef vector<ii> vii;

// vetor apenas. uso genérico... marcar visitados, etc..
typedef vector<int> vi;


// um vetor de vértices
vi cor;


// void printAdjList(int n, vector<vii> AdjList){
// 	for (int i = 0; i < n; ++i) // para todos os vértices
// 	{
// 		printf("%d -> ", i);
// 		for (int j = 0; j < AdjList[i].size(); ++j)
// 		{	if (j < AdjList[i].size()-1)
// 				printf("(%d,%d) > ", AdjList[i][j].first, AdjList[i][j].second);
// 			else 	printf("(%d,%d)", AdjList[i][j].first, AdjList[i][j].second);
// 		}
// 		printf("\n");
// 	}
// }

bool bipartite(int u, int n, vector<vii> AdjList){
	queue<int> q;

	cor[u] = 0; // comecaremos com a cor 0
	q.push(u);  // coloca u na fila.....

	while (!q.empty()) {

		int k = q.front(); q.pop(); // retira o vertice da fila...

		for (int i = 0; i < (int)AdjList[k].size(); ++i) // para todos adj v de k
		{
			ii v = AdjList[k][i]; // aqui v é um par...
			if (cor[v.first] == SEMCOR){
				cor[v.first] = 1-cor[k];
				q.push(v.first);
			}
			else if (cor[v.first] == cor[k])
				return false;
		}
	}
	return true;
}


int main(int argc, char const *argv[])
{

	int n, l, u, v;
	cin >> n; 

	while(n != 0){
		// a lista de adjacencia é um vetor de vetor de pares
		// seja um vertice (u,v)
		// first representa v, e second o peso da aresta !!
		// u é cada item do vetor AdjList !! 
		vector<vii> AdjList(100);

		cor.assign(n, SEMCOR);  // inicio vetor de visitados livre...

		cin >> l; 

		// agora le as arestas e coloca na lista e adjacencia
		for (int i = 0; i < l; ++i){// o grafo é NAO direcionado e as arestas nao tem peso!
			cin >> u >> v;
			AdjList[u].push_back(make_pair(v,0));
			AdjList[v].push_back(make_pair(u,0));
		}

		// printAdjList(n, AdjList);
		
		if (bipartite(0, n, AdjList))
			printf("BICOLORABLE.");
		else	
			printf("NOT BICOLORABLE.");

		cin >> n;
		if (n!=0)
			printf("\n");
	}
	 
	return 0;
}