#12906 같은 숫자는 싫어 

def solution(arr):
    answer = []
    for i in range(0,len(arr)):
        if i == 0:
            answer.append(arr[i])
        else:
            if arr[i] == arr[i-1]:
                continue
            else:
                answer.append(arr[i])
    return answer