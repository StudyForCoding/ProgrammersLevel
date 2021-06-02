// 정수 내림차순으로 배치하기

#include <vector>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

long long solution(long long n) {
	long long answer = 0;
	string CheckString = to_string(n);
	int Size = CheckString.size();
	char * OneText = new char[Size];
	strcpy(OneText, CheckString.c_str());

	vector<int> SortArray;
    //문자열 숫자로 변환하여 벡터에 저장
	for (int i = 0; i < Size; i++) 
		SortArray.push_back((OneText[i] - '0'));
	sort(SortArray.begin(), SortArray.end()); //정렬


	for (int i = 0; i < Size; i++) {    //벡터 to 문자열          
		OneText[i] = SortArray.back();
		SortArray.pop_back();
	}
	for (int i = Size - 1; i >= 0; i--) //문자열 to 숫자
		answer += OneText[(Size - 1 - i)] * pow(10, i);

	return answer;
}

/*
정확성  테스트
테스트 1 〉	통과 (0.03ms, 3.97MB)
테스트 2 〉	통과 (0.03ms, 3.96MB)
테스트 3 〉	통과 (0.04ms, 3.97MB)
테스트 4 〉	통과 (0.03ms, 3.93MB)
테스트 5 〉	통과 (0.03ms, 3.96MB)
테스트 6 〉	통과 (0.03ms, 3.97MB)
테스트 7 〉	통과 (0.03ms, 3.95MB)
테스트 8 〉	통과 (0.03ms, 3.95MB)
테스트 9 〉	통과 (0.04ms, 3.96MB)
테스트 10 〉	통과 (0.04ms, 3.96MB)
테스트 11 〉	통과 (0.03ms, 3.94MB)
테스트 12 〉	통과 (0.03ms, 3.9MB)
테스트 13 〉	통과 (0.03ms, 3.96MB)
테스트 14 〉	통과 (0.04ms, 3.95MB)
테스트 15 〉	통과 (0.03ms, 3.97MB)
테스트 16 〉	통과 (0.03ms, 3.98MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
*/