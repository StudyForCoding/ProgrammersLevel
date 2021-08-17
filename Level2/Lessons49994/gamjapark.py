# 방문 길이
def solution(dirs):
    answer = 0
    cor_dict = {}

    for i in range(-5,5):
        for j in range(-5,5):
            cor_dict[(i,j)] = [False, False] # row(-), col(|)
        cor_dict[(i,5)] = [False, True] #j=5
        cor_dict[(5,i)] = [True, False] #i=5

    cur = (0, 0)
    dir_dict = {"U":(0,1), "D":(0,-1), "R":(1,0), "L":(-1,0)}
    for dir in dirs:
        a = cur[0] + dir_dict[dir][0]
        b = cur[1] + dir_dict[dir][1]
        if (a < -5 or a > 5) or (b < -5 or b > 5): #check range
            continue
        new_cur = (a, b)       # R, U: cur / L, D: new_cur 변경
        if dir == "R" and not cor_dict[cur][0]:
            cor_dict[cur][0] = True
            answer += 1
        elif dir == "U" and not cor_dict[cur][1]:
            cor_dict[cur][1] = True
            answer += 1
        elif dir == "L" and not cor_dict[new_cur][0]:
            cor_dict[new_cur][0] = True
            answer += 1
        elif dir == "D" and not cor_dict[new_cur][1]:
            cor_dict[new_cur][1] = True
            answer += 1
        cur = new_cur
    return answer

'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.08ms, 10.3MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.14ms, 10.3MB)
테스트 5 〉	통과 (0.14ms, 10.3MB)
테스트 6 〉	통과 (0.10ms, 10.2MB)
테스트 7 〉	통과 (0.06ms, 10.2MB)
테스트 8 〉	통과 (0.08ms, 10.3MB)
테스트 9 〉	통과 (0.08ms, 10.3MB)
테스트 10 〉	통과 (0.09ms, 10.3MB)
테스트 11 〉	통과 (0.08ms, 10.2MB)
테스트 12 〉	통과 (0.13ms, 10.3MB)
테스트 13 〉	통과 (0.12ms, 10.3MB)
테스트 14 〉	통과 (0.12ms, 10.2MB)
테스트 15 〉	통과 (0.12ms, 10.3MB)
테스트 16 〉	통과 (0.39ms, 10.3MB)
테스트 17 〉	통과 (0.38ms, 10.3MB)
테스트 18 〉	통과 (0.41ms, 10.3MB)
테스트 19 〉	통과 (0.41ms, 10.3MB)
테스트 20 〉	통과 (0.44ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''