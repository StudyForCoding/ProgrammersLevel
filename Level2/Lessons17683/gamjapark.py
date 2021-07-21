# [3차] 방금그곡
def solution(m, musicinfos):
    answerlist = []
    idx = 0
    for one_music in musicinfos:
        infos = one_music.split(",")

        # 음악이 실행된 시간(분) 계산
        total_time = (int(infos[1].split(":")[0]) - int(infos[0].split(":")[0]))*60 + \
                    int(infos[1].split(":")[1]) - int(infos[0].split(":")[1])
            
        # 악보에 들어있는 음 리스트와 갯수
        sounds = []
        sound_count = 0         
        for sound in infos[3]:
            if sound != "#":
                sounds.append(sound)
                sound_count += 1
            else:
                sounds[sound_count-1] += "#"
                
        # 해당 시간에 실제 연주된 플레이악보 구하기
        if total_time > sound_count:       
            play = infos[3] * (total_time // sound_count)
            for i in range(total_time % sound_count):
                play += sounds[i]
        else:
            play = "".join(sounds[:total_time])

        # m이 연주된 악보에 들어있는데 마지막에 #으로 붙어 있는 경우의 수 제거
        where = play.find(m)
        if where > -1:
            if m[-1] == "#":
                answerlist.append([infos[2],total_time, idx])
                idx += 1
            else:
                where_idx = 0
                while where_idx < len(play):
                    where2 = play.find(m+"#", where_idx)
                    if where != where2:
                        answerlist.append([infos[2],total_time, idx])
                        idx += 1
                        break
                    where_idx += where + len(m)
                    where = play.find(m, where_idx)


    if len(answerlist) == 0:
        answer = "(None)"
    else:
        answerlist = sorted(answerlist, key=lambda x: (x[1], -x[2]))
        answer = answerlist[-1][0]
    return answer
'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.5MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (0.04ms, 10.4MB)
테스트 5 〉	통과 (0.05ms, 10.5MB)
테스트 6 〉	통과 (0.05ms, 10.5MB)
테스트 7 〉	통과 (0.13ms, 10.5MB)
테스트 8 〉	통과 (0.13ms, 10.4MB)
테스트 9 〉	통과 (0.14ms, 10.4MB)
테스트 10 〉	통과 (0.14ms, 10.4MB)
테스트 11 〉	통과 (0.14ms, 10.5MB)
테스트 12 〉	통과 (0.13ms, 10.4MB)
테스트 13 〉	통과 (0.13ms, 10.5MB)
테스트 14 〉	통과 (0.15ms, 10.3MB)
테스트 15 〉	통과 (0.13ms, 10.5MB)
테스트 16 〉	통과 (0.12ms, 10.4MB)
테스트 17 〉	통과 (0.13ms, 10.4MB)
테스트 18 〉	통과 (0.15ms, 10.4MB)
테스트 19 〉	통과 (0.14ms, 10.4MB)
테스트 20 〉	통과 (0.14ms, 10.4MB)
테스트 21 〉	통과 (0.13ms, 10.4MB)
테스트 22 〉	통과 (0.13ms, 10.4MB)
테스트 23 〉	통과 (0.14ms, 10.5MB)
테스트 24 〉	통과 (0.13ms, 10.5MB)
테스트 25 〉	통과 (0.04ms, 10.4MB)
테스트 26 〉	통과 (0.05ms, 10.4MB)
테스트 27 〉	통과 (0.05ms, 10.4MB)
테스트 28 〉	통과 (0.06ms, 10.5MB)
테스트 29 〉	통과 (4.30ms, 10.5MB)
테스트 30 〉	통과 (4.94ms, 10.5MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''