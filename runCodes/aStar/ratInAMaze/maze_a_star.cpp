#include <cstring>
#include <cstdio>
#include <iostream>
#include <queue>
#include <cmath>

using namespace std;

#define MAX 30

#define WITH_DEPTH true
#define H_MANHATTAN true

typedef pair<int,int> pi;


struct state{
	pi p;
	int depth;
};


int n;
short int maze[MAX][MAX];
short int sol[MAX][MAX];
short int path[MAX][MAX];


int h_manhattan(state const& s){

	// manhattan distance
	return abs(s.p.first - (n-1)) + abs(s.p.second - (n-1));
}


int h_euclidiana(state const& s){

	// euclidean distance
	return sqrt(pow(((n-1) - s.p.first),2) + pow(((n-1) - s.p.second),2));
}


// this is an strucure which implements the operator overloading
struct CompareState {
    bool operator()(state const& s1, state const& s2)
    {
    	// g = distance from initial (depth if WITH_DEPTH == true else always 0)
    	int g1, g2, h1, h2, f1, f2;

    	if(WITH_DEPTH){
    		g1 = s1.depth;
    		g2 = s2.depth;
    	}
    	else{
    		g1 = 0;
    		g2 = 0;
    	}

    	// h = manhattan distance or euclidean distance
    	if(H_MANHATTAN){
    		h1 = h_manhattan(s1);
    		h2 = h_manhattan(s2);
    	}
    	else{
    		h1 = h_euclidiana(s1);
    		h2 = h_euclidiana(s2);
    	}

		// f = g + h
    	f1 = g1 + h1;
    	f2 = g2 + h2;

        return f1 > f2; 
    }
};


int moves[4][2] = {1,0,
                   0,1,
                  -1,0,
                   0,-1};


void printMat(short int mat[MAX][MAX]){

	cout << "------" << endl;
	for (int i = 0; i < n; ++i){
		for (int j = 0; j < n; ++j)
		{
			cout << mat[i][j] << " ";
		}
		cout << endl;
	}
	cout << "------" << endl;
}

int countMat(short int mat[MAX][MAX]){

	int sum = 0;
	for (int i = 0; i < n; ++i){
		for (int j = 0; j < n; ++j)
		{
			sum += mat[i][j];
		}
	}
	return sum;
}


bool valido(int x, int y){
	if (x < n && x >= 0 && y < n && y >= 0 && maze[x][y] == 1 && sol[x][y]==0)
		return true;
	return false;
}

bool achaCaminho(int x, int y){
	int nx, ny;
	priority_queue<state, vector<state>, CompareState> pq;

	state par;
	par.p = make_pair(x,y);
	par.depth = 0;

	pq.push(par);

	state new_state;

	sol[x][y] = 1;

	while (!pq.empty()){
		par = pq.top(); pq.pop();
		path[par.p.first][par.p.second] = 1;

		// se chegou ao fim...
		if (par.p.first == n-1 && par.p.second == n-1 && maze[par.p.first][par.p.second] == 1){
			return true;
		}

		//para todos os movimentos possiveis
		for (int i = 0; i < 4; ++i)
		{
			nx = par.p.first + moves[i][0];
			ny = par.p.second + moves[i][1];

			if (valido(nx,ny)){
				sol[nx][ny] = 1;
				new_state.p = make_pair(nx,ny);
				new_state.depth = par.depth+1;

				pq.push(new_state);
			}
		}
	}
	return false;
}


int main(int argc, char const *argv[])
{
	memset(sol, 0, sizeof sol);
	memset(path, 0, sizeof path);
	cin >> n;

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
		{
			cin >> maze[i][j];
		}
	// printMat(maze);
	
	if (achaCaminho(0,0))
		cout << "Encontrei um caminho" << endl;
	else cout << "Nao existe um caminho para este caso" << endl;

	// printMat(sol);

	// printMat(path);	

	cout << "Total de quadradinhos visitados: " << countMat(path) << endl;

	return 0;
}
