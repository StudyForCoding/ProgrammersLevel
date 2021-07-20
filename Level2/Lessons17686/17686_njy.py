#파일명 정렬
def solution(files):
    answer=[]
    str=[]

    for file in files:
        HEAD=''

        for char in file:
            if char.isdigit():
                break
            HEAD+=char

        NUM=''        
        for char in file[len(HEAD):]:
            if not char.isdigit():
                break
            NUM+=char

        str.append([HEAD.lower(),int(NUM),file]) # 대소문자 구분 안하기 + 숫자로 비교 + 원래 파일명

    file_list = sorted(str, key=lambda x:(x[0],x[1])) # HEAD와 NUM 기준으로 정렬

    for i in file_list:
        answer.append(i[2]) # 파일명만 반환
    return answer
    """
    테스트 1 〉	통과 (0.04ms, 10.4MB)
    테스트 2 〉	통과 (0.04ms, 10.4MB)
    테스트 3 〉	통과 (2.34ms, 10.7MB)
    테스트 4 〉	통과 (2.26ms, 10.6MB)
    테스트 5 〉	통과 (2.14ms, 10.7MB)
    테스트 6 〉	통과 (2.48ms, 10.7MB)
    테스트 7 〉	통과 (2.15ms, 10.7MB)
    테스트 8 〉	통과 (2.31ms, 10.6MB)
    테스트 9 〉	통과 (2.03ms, 10.7MB)
    테스트 10 〉	통과 (4.43ms, 10.8MB)
    테스트 11 〉	통과 (2.04ms, 10.5MB)
    테스트 12 〉	통과 (2.20ms, 10.8MB)
    테스트 13 〉	통과 (1.83ms, 10.8MB)
    테스트 14 〉	통과 (2.15ms, 10.8MB)
    테스트 15 〉	통과 (2.05ms, 10.8MB)
    테스트 16 〉	통과 (4.34ms, 10.8MB)
    테스트 17 〉	통과 (1.81ms, 10.8MB)
    테스트 18 〉	통과 (1.73ms, 10.7MB)
    테스트 19 〉	통과 (2.26ms, 10.8MB)
    테스트 20 〉	통과 (1.96ms, 10.8MB)
    """