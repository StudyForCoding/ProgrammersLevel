#n개의 최소공배수
def getGCD(a,b):
    if b>a:
        a,b = b,a
    r = a%b
    if r == 0:
        return b
    else:
        return getGCD(b,r)

def getLCM(a,b):
    return int(a*b/getGCD(a,b))
    
def solution(arr):
    answer = arr[0]
    for i in range(1,len(arr)):
        answer = getLCM(answer,arr[i])
    return answer

print(solution([2,6,8,14]))