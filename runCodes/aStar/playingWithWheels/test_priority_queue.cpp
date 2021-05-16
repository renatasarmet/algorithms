#include <stdio.h>
#include <queue>
#include <iostream>

using namespace std;

struct state{
	int digit[4];
	int depth;
};

state initial, final;


int h(state const& s1){
	int sum = 0;
	int min_opt, min_digit, max_digit, opt1, opt2;

	for(int i=0; i<4; i++){
		min_digit = min(s1.digit[i], final.digit[i]);
		max_digit = max(s1.digit[i], final.digit[i]);

		opt1 = max_digit - min_digit;
		opt2 = min_digit + 10-max_digit;

		min_opt = min(opt1,opt2);
		sum += min_opt;
	}
	return sum;
}

// this is an strucure which implements the
// operator overloading
struct CompareState {
    bool operator()(state const& s1, state const& s2)
    {
    	
    	// g = depth
    	int g1 = s1.depth;
    	int g2 = s2.depth;

    	// h = distance from final
    	int h1 = h(s1);
    	int h2 = h(s2);

		// f = g + h
    	int f1 = g1 + h1;
    	int f2 = g2 + h2;

        // return "true" if "s1" is ordered before "s2", for example:
        return f1 > f2; 
    }
};



int main (){
	priority_queue<state, vector<state>, CompareState> pq;


	final.digit[0] = 0;
	final.digit[1] = 0;
	final.digit[2] = 0;
	final.digit[3] = 0;


	initial.digit[0] = 1;
	initial.digit[1] = 0;
	initial.digit[2] = 0;
	initial.digit[3] = 8;
	initial.depth = 1;

	state initial2; 

	initial2.digit[0] = 3;
	initial2.digit[1] = 0;
	initial2.digit[2] = 0;
	initial2.digit[3] = 1;
	initial2.depth = 1;

	pq.push(initial);
	pq.push(initial2);

	state top = pq.top();

	cout << top.digit[0] << endl;		

	return 0;
}
