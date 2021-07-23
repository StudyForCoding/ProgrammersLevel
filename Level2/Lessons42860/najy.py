# 조이스틱

def solution(name):
    answer = 0
    size = len(name)
    counter = [1]*size
    l, r = 0, 0   

    for idx,c in enumerate(name):
        if c == 'A':
            counter[idx] = 0
        else : 
            answer += min(ord(c)-ord('A'),ord('Z')-ord(c)+1)
    counter[0] = 0
    
    idx = 0
    while(sum(counter) != 0):
        for l in range(1,size):
            if counter[idx-l] == 1:
                break
        for r in range(1,size):
            if counter[idx+r] == 1:
                break
        if r > l:
            counter[idx-l] = 0
            answer += l
            idx -= l
        else :
            counter[idx+r] = 0
            answer += r
            idx += r
            
    return answer

'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
'''