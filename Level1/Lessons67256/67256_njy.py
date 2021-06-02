# 키패드 누르기

def solution(numbers, hand):
    answer = ''
    # 키 위치를 딕셔너리로 맵핑
    key = {1:[0,0], 2:[0,1], 3:[0,2],
            4:[1,0], 5:[1,1], 6:[1,2],
            7:[2,0], 8:[2,1], 9:[2,2],
            '*':[3,0], 0:[3,1], '#':[3,2]}
    
    # 현재 좌우 위치 초기화
    current_L = key['*']
    current_R = key['#']

    for number in numbers:
        # 1,4,7 -> 왼손 처리 및 위치 변경
        if number==1 or number==4 or number==7:
            answer += 'L'
            current_L = key[number]
        # 3,6,9 -> 오른손 처리 및 위치 변경
        elif number==3 or number==6 or number==9:
            answer += 'R'
            current_R = key[number]
        # 2,5,8,0 -> 거리 계산
        else:
            # 타겟 - 왼손 거리 계산
            distance_L = abs(key[number][0]-current_L[0])+abs(key[number][1]-current_L[1])
            # 타겟 - 오른손 거리 계산
            distance_R = abs(key[number][0]-current_R[0])+abs(key[number][1]-current_R[1])
            # 왼손 거리 > 오른손 거리 -> 오른손 처리 및 위치 변경
            if distance_L>distance_R:
                answer += 'R'
                current_R = key[number]
            # 왼손 거리 < 오른손 거리 -> 왼손 처리 및 위치 변경
            elif distance_L<distance_R:
                answer += 'L'
                current_L = key[number]
            # 왼손 거리 = 오른손 거리 -> 주손으로 처리 및 위치 변경
            else:
                if hand=='right':
                    answer += 'R'
                    current_R = key[number]
                else:
                    answer += 'L'
                    current_L = key[number]
    return answer

"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.4MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.04ms, 10.3MB)
테스트 12 〉	통과 (0.03ms, 10.3MB)
테스트 13 〉	통과 (0.05ms, 10.3MB)
테스트 14 〉	통과 (0.11ms, 10.3MB)
테스트 15 〉	통과 (0.31ms, 10.3MB)
테스트 16 〉	통과 (0.27ms, 10.3MB)
테스트 17 〉	통과 (0.60ms, 10.3MB)
테스트 18 〉	통과 (0.63ms, 10.2MB)
테스트 19 〉	통과 (0.60ms, 10.1MB)
테스트 20 〉	통과 (0.55ms, 10.3MB)
"""