#numbers : 정수 배열
#서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 '모든 수' 를 배열에 오름차순으로 담아 return
#1. 입력 : A=list[int,input().split()]
#2. if i!=j  i,j==A의 인덱스 -> A[i]+A[j]
#3. array(list)에 담기 -> array=[] -> array.append(A[i]+A[j])
#4. array를 오름차순으로 만들기,중복 없애기 -> sort() , set()
#5. return
def solution(numbers):
    array=[]
    for i in numbers:
        for j in numbers:
            if i!=j:
                array.append(numbers[i]+numbers[j])
    #array.sort()
    #answer=list(set(array))    #이렇게 썼더니 테스트 4, 5 에서 실패 떠서 아랫줄 코드로 바꿈

​												  #array.sort() 가 아니라 answer.sort() 여야하고, set으로 중복을 지운 이후에 오름차순/내림차순을 정렬해야해. 두개의 순서가 바뀌면 정렬 후 다시 랜덤으로 된다ㅠㅠ

   return sorted(list(set(array))) 

numbers=[2,1,3,4,1]

