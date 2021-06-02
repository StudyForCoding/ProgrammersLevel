# 키패드 누르기

import re
def distance(t, cur_pos, left_pos, right_pos):
    distanceL = (cur_pos[1] - left_pos[1]) + abs(cur_pos[0] - left_pos[0])
    distanceR = (right_pos[1] - cur_pos[1]) + abs(cur_pos[0] - right_pos[0]) 
    if distanceL < distanceR:
        return "L"
    elif distanceL > distanceR:
        return "R"
    else:
        return t
    
def solution(numbers, hand):
    posL, posR = (0,0), (0,2)
    answer = ""
    for num in numbers:
        tmp = "L" if hand == "left" else "R"
        if num == 0:
            i, j = 0, 1
            tmp = distance(tmp, (i, j), posL, posR)
        else:
            i =  3 - ((num - 1) // 3)
            j = (num - 1) % 3
            if j == 0:
                tmp = "L"
            elif j == 2:
                tmp = "R"
            else:
                tmp = distance(tmp, (i, j), posL, posR)
                
        if tmp == "L":
            posL = (i,j)
        else:
            posR = (i,j)
        answer += tmp
    return answer


'''
테스트 1 〉	통과 (0.00ms, 10.4MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.04ms, 10.4MB)
테스트 12 〉	통과 (0.03ms, 10.3MB)
테스트 13 〉	통과 (0.06ms, 10.4MB)
테스트 14 〉	통과 (0.13ms, 10.3MB)
테스트 15 〉	통과 (0.34ms, 10.3MB)
테스트 16 〉	통과 (0.33ms, 10.3MB)
테스트 17 〉	통과 (0.74ms, 10.3MB)
테스트 18 〉	통과 (0.68ms, 10.3MB)
테스트 19 〉	통과 (0.81ms, 10.2MB)
테스트 20 〉	통과 (0.43ms, 10.2MB)
'''