

def solution(n, times):
    sorted_times = sorted(times)
    waiting_list = list()
    length = len(sorted_times)
    for index in range(0, length):
        waiting_list.append(0)

    for i in range(0, n):
        temp_list = [0, 1000000001]
        for index, time in enumerate(sorted_times):
            temp_value = waiting_list[index] + time
            if temp_list[1] > temp_value:
                temp_list[0] = index
                temp_list[1] = temp_value
        waiting_list[temp_list[0]] = temp_list[1]

    answer = max(waiting_list)
    return answer


if __name__ == '__main__':
    answer = solution(6, [7, 10])
    print(answer)

