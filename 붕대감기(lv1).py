#공격이 기술보다 먼저들어감. 공격을 먼저 때려.
#1.일단 몇 초동안 하는지 가져와. 이건 attack의 마지막 원소 첫번째 원소에 있어. 그리고 그만큼 for문 돌려. 연공 변수 넣어서 +1
#2. 1에서의 for 문을 돌리면서 지금 초와 attakcs의 각 원소의 첫 원소를 가져와서 같다면 공격시전해. 그리고 연공 변수를 0으로 초기화
#3. 1에서의 for 문 안에서 매초 피 힐을 해야해. 
#3. 1에서의 for문 안에서는 지금 체력과 공격당한 피 중 더 작은 걸 가져오게 해.

def solution(bandage, health, attacks):
    #총 턴 횟수
    dead = False
    length = attacks[-1][0]
    max_health = health
    con_att = 0 #연공 변수
    att_timing = []
    
    for n in attacks:
        att_timing.append(n[0])
    for i in range(length+1):
        #만약 공격을 당하는 경우
#        for k in attacks:
        if i in att_timing:
            for k in attacks:
                if i == k[0]:
                    damage = k[1]
                    con_att = 0
                    health -= damage
                    if health <= 0:
                        dead = True
        else:
            con_att += 1
            health += bandage[1]
            if con_att == bandage[0]:
                health += bandage[2]
                con_att = 0
            health = min(health,max_health)
    if dead == True:
        health = -1
    return health