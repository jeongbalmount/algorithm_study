

def solution(bridge_length, weight, truck_weights):
    now_trucks = [] # 현재 다리에 올라와 았는 트럭들의 리스트
    now_truck_time = [] # 각 트럭이 다리를 다 지나면 몇초가 되어있는지 확인하는 변
    sum_time = bridge_length # 걸린 시간을 모아놓은 변수

    for index, truck_weight in enumerate(truck_weights):
        # 현재 다리에 있는 트럭들의 무게 합을 구하는 부분
        now_weight_sum = 0
        check_plus_truck = 0

        if index is 0:
            check_plus_truck += truck_weight
        else:
            for i in now_trucks:
                now_weight_sum += i
                # 다리에 새로운 트럭이 진입해도 되는지 확인하는 부분
                check_plus_truck = now_weight_sum + truck_weight

        if check_plus_truck <= weight:
            # 전체 다리 길이 보다 더 많은 트럭이 들어오지 못하도록 막는 코드
            if bridge_length <= len(now_trucks):
                # 다리 맨 앞에 있는 트럭을 빼고 시간 계산한다.
                # finish_trucks.append(now_trucks.pop(index))
                sum_time += now_truck_time.pop(0) - sum_time  # sum_time을 빼야 정확한 시간이 수정된다.

            # 새로운 트럭을 다리에 넣고 시간도 추가한다.
            now_trucks.append(truck_weight) #다리에 트럭을 넣는다
            sum_time += 1
            now_truck_time.append(sum_time) #전체 소요 시간에서 1초를 더한 값을 넣는다

        elif check_plus_truck > weight:
            # 다리 트럭의 합과 더할 트럭의 무게 를 더했을때 weight보다 무거울때
            pop_value = 0
            while check_plus_truck > weight:
                pop_value = now_trucks.pop(0) # 다리위에 있는 트럭 하나 뺀다
                check_plus_truck -= pop_value # 트럭을 빼고 전체 무게에서도 트럭 무게를 뺀다
                pop_value = now_truck_time.pop(0) # 트럭 시간을 뺀다

            leftover = pop_value #이값은 트럭이 다리에 진입하고 난 후 소요된 시간을 나타냄
            now_trucks.append(truck_weight)
            sum_time = leftover + bridge_length # 들어올 트럭이 다리를 나갔을때 걸릴시간 계산해 전체 소요시간 업데이트
            now_truck_time.append(sum_time)

    sum_time = now_truck_time.pop()

    answer = sum_time
    return answer


returnValue = solution(2, 10, [7,4,5,6])

print(returnValue)