//자연수 뒤집어 배열로 만들기

#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(long long n) {
    vector<int> answer;
    string intString = to_string(n);
    int Size = intString.size();
    const char* stringOneChar = intString.c_str();
    
    for(int i = Size - 1; i >= 0; i--){
        answer.push_back(stringOneChar[i] - '0');
    }
    return answer;
}

/*
정확성  테스트
테스트 1 〉	통과 (0.02ms, 3.95MB)
테스트 2 〉	통과 (0.02ms, 3.96MB)
테스트 3 〉	통과 (0.02ms, 3.93MB)
테스트 4 〉	통과 (0.02ms, 3.96MB)
테스트 5 〉	통과 (0.02ms, 3.96MB)
테스트 6 〉	통과 (0.02ms, 3.9MB)
테스트 7 〉	통과 (0.02ms, 3.96MB)
테스트 8 〉	통과 (0.02ms, 3.96MB)
테스트 9 〉	통과 (0.02ms, 3.95MB)
테스트 10 〉	통과 (0.02ms, 3.93MB)
테스트 11 〉	통과 (0.02ms, 3.82MB)
테스트 12 〉	통과 (0.02ms, 3.9MB)
테스트 13 〉	통과 (0.02ms, 3.96MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
*/