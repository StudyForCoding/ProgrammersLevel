def solution(array, commands):
    answer = []
    for command in commands:
        New_array = []
        New_array += array[command[0]-1:command[1]]
        New_array.sort()
        answer.append(New_array[command[2]-1])
    return answer

# array를 command의 [0]~[1]로 자르기
# array 정렬 (array.sort())
# 정렬한 array의 k 번째 수 출력하기

