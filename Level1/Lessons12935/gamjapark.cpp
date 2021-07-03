//제일 작은 수 제거하기

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    int Min = arr[0];
    int MinNum;
 
    for(int i = 1; i < arr.size(); i++){
        if(arr[i] < Min) {
            Min = arr[i];
            MinNum = i;
        }
    }
    vector<int>::iterator iter = arr.begin() + MinNum;
    arr.erase(iter);
    if(arr.size() == 0) arr.push_back(-1);
    return arr;
}

/*
정확성  테스트
테스트 1 〉	통과 (11.16ms, 13.4MB)
테스트 2 〉	통과 (0.09ms, 3.89MB)
테스트 3 〉	통과 (0.12ms, 3.96MB)
테스트 4 〉	통과 (0.07ms, 3.96MB)
테스트 5 〉	통과 (0.03ms, 3.94MB)
테스트 6 〉	통과 (0.14ms, 3.95MB)
테스트 7 〉	통과 (0.19ms, 3.94MB)
테스트 8 〉	통과 (0.01ms, 3.96MB)
테스트 9 〉	통과 (0.05ms, 3.58MB)
테스트 10 〉	통과 (0.01ms, 3.97MB)
테스트 11 〉	통과 (0.01ms, 3.96MB)
테스트 12 〉	통과 (0.02ms, 3.96MB)
테스트 13 〉	통과 (0.03ms, 3.91MB)
테스트 14 〉	통과 (0.15ms, 3.98MB)
테스트 15 〉	통과 (0.08ms, 3.97MB)
테스트 16 〉	통과 (0.16ms, 3.94MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
*/