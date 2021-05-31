# 자연수 뒤집어 배열로 만들기
def solution(n):
    answer = []
    n = str(n) # string type casting
    
    for i in reversed(range(len(n))):
        answer.append(int(n[i]))
        
    return answer

'''
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.4MB)
테스트 9 〉	통과 (0.02ms, 10.4MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.03ms, 10.4MB)
테스트 13 〉	통과 (0.02ms, 10.3MB)
'''