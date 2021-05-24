#예산

#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> d, int budget) {

	sort(d.begin(), d.end(), greater<int>());	//내림차순 정렬
	int size = d.size();

	int count = 0;
	for (int i = 0; i < size; i++) {
		int me = d.back();
		if (me <= budget) {
		
			d.pop_back();
			++count;
			budget -= me;
		}
		else break;
	}
	return count;
}

'''
테스트 1 〉	통과 (0.01ms, 3.88MB)
테스트 2 〉	통과 (0.01ms, 3.96MB)
테스트 3 〉	통과 (0.01ms, 3.96MB)
테스트 4 〉	통과 (0.01ms, 3.94MB)
테스트 5 〉	통과 (0.01ms, 3.95MB)
테스트 6 〉	통과 (0.01ms, 3.93MB)
테스트 7 〉	통과 (0.01ms, 3.94MB)
테스트 8 〉	통과 (0.01ms, 3.87MB)
테스트 9 〉	통과 (0.01ms, 3.96MB)
테스트 10 〉	통과 (0.03ms, 3.96MB)
테스트 11 〉	통과 (0.01ms, 3.93MB)
테스트 12 〉	통과 (0.01ms, 3.97MB)
테스트 13 〉	통과 (0.01ms, 3.93MB)
테스트 14 〉	통과 (0.01ms, 3.89MB)
테스트 15 〉	통과 (0.01ms, 3.94MB)
테스트 16 〉	통과 (0.01ms, 3.96MB)
테스트 17 〉	통과 (0.01ms, 3.94MB)
테스트 18 〉	통과 (0.01ms, 3.9MB)
테스트 19 〉	통과 (0.01ms, 3.93MB)
테스트 20 〉	통과 (0.01ms, 3.95MB)
테스트 21 〉	통과 (0.01ms, 3.97MB)
테스트 22 〉	통과 (0.01ms, 3.89MB)
테스트 23 〉	통과 (0.01ms, 3.94MB)
'''