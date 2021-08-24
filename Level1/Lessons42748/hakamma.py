k번째 수
def solution(array, commands):
    answer = []
    
    for x in commands:
        i = x[0]
        j = x[1]
        k = x[2]
        A = array[i-1:j] // i번째에서 k번째까지 자르는 순서
        A.sort() // 
        answer.append(A[k-1]) // index의 첫번째는 0이므로 -1을 진행
    return answer