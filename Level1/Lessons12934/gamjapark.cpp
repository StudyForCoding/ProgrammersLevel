// 정수 제곱근 판별

#include <string>
#include <vector>

using namespace std;

long long solution(long long n) {
    long long answer = -1;
    for(long long i = 1; i * i <= n; i++){
        if( i * i == n ){
            answer = (i + 1) * (i + 1);
            break;
        }
    }
    return answer;
}

/*

정확성  테스트
테스트 1 〉	통과 (0.01ms, 3.95MB)
테스트 2 〉	통과 (2.81ms, 3.91MB)
테스트 3 〉	통과 (0.01ms, 3.96MB)
테스트 4 〉	통과 (0.47ms, 3.93MB)
테스트 5 〉	통과 (0.02ms, 3.91MB)
테스트 6 〉	통과 (0.01ms, 3.96MB)
테스트 7 〉	통과 (0.03ms, 3.96MB)
테스트 8 〉	통과 (0.01ms, 3.96MB)
테스트 9 〉	통과 (0.02ms, 3.98MB)
테스트 10 〉	통과 (0.03ms, 3.97MB)
테스트 11 〉	통과 (0.04ms, 3.84MB)
테스트 12 〉	통과 (0.04ms, 3.89MB)
테스트 13 〉	통과 (0.01ms, 3.96MB)
테스트 14 〉	통과 (0.03ms, 3.97MB)
테스트 15 〉	통과 (0.01ms, 3.97MB)
테스트 16 〉	통과 (0.01ms, 3.78MB)
테스트 17 〉	통과 (0.01ms, 3.97MB)
테스트 18 〉	통과 (0.01ms, 3.96MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0

*/