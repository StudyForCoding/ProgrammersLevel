def solution(n):
    answer = 0
    binarys = []
    binary =''
    #1. 10진법 수 -> 3진법 수
    while n>0:
        div = n//3 #n을 3으로 나눈 몫
        mod = n%3  #n을 3으로 나눈 나머지, binary에 저장하기
        n = div #n의 값 = div => div가 0일 때 까지 반복
        binarys += str(mod) #나머지 순서가 반대로 나와서, 앞뒤 반전 진행할 필요가 없음
    for i in range(len(binarys)):
        binary+=binarys[i]
    

    #2. 3진법 수 -> 10진법 수
    answer = int(binary,3)
    return answer