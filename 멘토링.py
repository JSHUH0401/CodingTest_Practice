'''
1. 스케쥴에서 기준시간 가져와
2. 타임로그에서 걔에 해당하는 출근시간들 가져와.
3. 주말인 애들 빼. 5이면 2,3번째. 4이면 3,4번째
3. 기준시간과 비교해서 +10분 이하로 들어온 애들 숫자 세.
4. 숫자가 4개라면 리절트 하나 추가해.
'''

def solution(schedules, timelogs, startday):
    answer = 0
    #가져오기
    for i in range(len(schedules)):
        schedule = schedules[i]
        limit_time = schedule + 10
        if limit_time % 100 >= 60:
            limit_time += 40

        is_elig = True

        for j in (range(7)):
            current_day = (j + startday) % 7

            if current_day == 6 or current_day == 0:
                continue
            if timelogs[i][j] > limit_time:
                is_elig = False
                break
        
        if is_elig:
            answer =+ 1
        #print(result)
    return answer

print(solution([730, 855, 700, 720], [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]],1))