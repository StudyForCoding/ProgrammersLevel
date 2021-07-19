# [3차] 파일명 정렬

def solution(files):
    ans = [[file,'',''] for file in files] # filename, head, number
    for f in ans:
        filename = f[0]
        for i in range(len(filename)):
            if (not filename[i].isdigit()) and (filename[i+1].isdigit()):
                f[1] = filename[:i+1].lower()
                idx = i+1
            if i+1 == len(filename) or (filename[i].isdigit()) and (not filename[i+1].isdigit()):
                f[2] = int(filename[idx:i+1])
                break
    
    ans.sort(key = lambda f:(f[1],f[2]))
    return [f[0] for f in ans]

'''
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (4.44ms, 10.8MB)
테스트 4 〉	통과 (4.11ms, 10.7MB)
테스트 5 〉	통과 (4.24ms, 10.9MB)
테스트 6 〉	통과 (4.06ms, 10.6MB)
테스트 7 〉	통과 (3.92ms, 10.7MB)
테스트 8 〉	통과 (3.35ms, 10.7MB)
테스트 9 〉	통과 (4.01ms, 10.7MB)
테스트 10 〉	통과 (4.13ms, 10.7MB)
테스트 11 〉	통과 (3.67ms, 10.7MB)
테스트 12 〉	통과 (3.66ms, 10.7MB)
테스트 13 〉	통과 (3.88ms, 10.5MB)
테스트 14 〉	통과 (4.17ms, 10.8MB)
테스트 15 〉	통과 (4.92ms, 10.8MB)
테스트 16 〉	통과 (3.69ms, 10.7MB)
테스트 17 〉	통과 (3.03ms, 10.5MB)
테스트 18 〉	통과 (3.67ms, 10.7MB)
테스트 19 〉	통과 (5.77ms, 10.7MB)
테스트 20 〉	통과 (4.14ms, 10.8MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
