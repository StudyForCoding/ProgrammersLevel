#67256 키패드 누르기

def solution(numbers, hand):
    answer = ''
    last_L = 10
    last_R = 12
    for n in numbers:
        if n in [1,4,7]:
            answer += 'L'
            last_L = n
        elif n in [3,6,9]:
            answer += 'R'
            last_R = n
        
        else:
            if n == 0:
                n = 11
            
            dist_L = abs(n-last_L) // 3 + abs(n-last_L) % 3
            dist_R = abs(n-last_R) // 3 + abs(n-last_R) % 3
            
            if dist_L > dist_R:
                answer += 'R'
                last_R = n
            elif dist_L < dist_R:
                answer += 'L'
                last_L = n
            else:
                if hand == 'left':
                    answer += 'L'
                    last_L = n
                else:
                    answer += 'R'
                    last_R = n
            
    return answer