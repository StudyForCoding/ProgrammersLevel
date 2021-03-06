// 자릿수 더하기

#include <vector>
#include <string>

using namespace std;
int solution(int n)
{
    int answer = 0;
    
    string intString = to_string(n);
    int Size = intString.size();
    const char* stringOneChar = intString.c_str();
    
    for(int i = 0; i < Size; i++){
        answer += (stringOneChar[i] - '0');
    }
    return answer;
}

/*
정확성  테스트
테스트 1 〉	통과 (0.01ms, 3.97MB)
테스트 2 〉	통과 (0.01ms, 3.97MB)
테스트 3 〉	통과 (0.02ms, 3.95MB)
테스트 4 〉	통과 (0.01ms, 3.95MB)
테스트 5 〉	통과 (0.02ms, 3.97MB)
테스트 6 〉	통과 (0.01ms, 3.95MB)
테스트 7 〉	통과 (0.02ms, 3.96MB)
테스트 8 〉	통과 (0.01ms, 3.95MB)
테스트 9 〉	통과 (0.01ms, 3.89MB)
테스트 10 〉	통과 (0.01ms, 3.88MB)
테스트 11 〉	통과 (0.02ms, 3.93MB)
테스트 12 〉	통과 (0.01ms, 3.96MB)
테스트 13 〉	통과 (0.01ms, 3.83MB)
테스트 14 〉	통과 (0.01ms, 3.93MB)
테스트 15 〉	통과 (0.02ms, 3.89MB)
테스트 16 〉	통과 (0.01ms, 3.97MB)
테스트 17 〉	통과 (0.01ms, 3.95MB)
테스트 18 〉	통과 (0.01ms, 3.97MB)
테스트 19 〉	통과 (0.02ms, 3.97MB)
테스트 20 〉	통과 (0.01ms, 3.93MB)
테스트 21 〉	통과 (0.02ms, 3.94MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
*/