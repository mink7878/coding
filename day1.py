# bandage(붕대감기 기술) = [시전시간, 1초당 회복량, 추가 회복량] = [t, x, y]
# health(최대체력)
# attacks(몬스터 공격시간, 피해량) = [공격시간, 피해량] >>> 공격시간 기준 오름차순


def solution(bandage, health, attacks):
    succcnt = 1
    max_health = health
    attacks_idx = 0
    time = 0
    
    for i in range(0, attacks[-1][0] + 1):
        ## 공격 받음
        if (attacks_idx < len(attacks)) and (attacks[attacks_idx][0] == time):
            health -= attacks[attacks_idx][1]
            succcnt = 1
            attacks_idx += 1
            
            if health <= 0:
                return -1
        
        ## 공격 안 받음
        else:
            health = min(max_health, health+bandage[1])
            ## 체력 최대
            if succcnt == bandage[0]:
                health = min(max_health, health+bandage[2])
                succcnt = 1
            ## 정상
            else:
                succcnt += 1
            
        # print(i, health, succcnt)
        time += 1

    return health