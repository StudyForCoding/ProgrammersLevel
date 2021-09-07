#12953 N개의 최소공배수

def solution(arr):
    answer = 0
    max_num = 1
    for i in range(len(arr)):
        max_num *= arr[i]
    
    for a in range(2, max_num+1):
        for i in range(len(arr)):
            if a%arr[i] != 0:
                break
        else:
            answer = a
            break
    return answer