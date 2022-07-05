def solution(bridge_length, weight, truck_weights):
    bridge = [0 for i in range(bridge_length)]
    cnt = 0
    while bridge:
        cnt += 1
        bridge.pop(0)
        if truck_weights:
            if len(bridge) <= bridge_length and sum(bridge) + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)
    return cnt
print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
# 아이디어
# 다리 위를 트럭이 지나갈 때 
# 다리 위에서 트럭이 머무는 시간이 2가 되면 pop해야 된다 생각해서
# 한 트럭이 머무는 시간을 따로 리스트로 만듦
# 그렇게 코딩하려다 보니 복잡해질 뿐만 아니라 못 품..

# 트럭이 다리 위를 한칸씩 지나가는 모습을 리스트로 형상화하면 쉬움
# 오른쪽에서 왼쪽으로 트럭이 움직이는 모습
# [0,0]
# [0,truck]
# [truck,0]
# [0,0]
# 큐의 개념이 이용됨
