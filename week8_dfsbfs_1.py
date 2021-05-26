from collections import deque


def solution(n, computers):
    visit = list()

    for index, computer in enumerate(computers):
        queue = deque(computer)
        for queue_index, link_com in enumerate(queue):
            if queue_index != index and link_com == 1:
                if [index, queue_index] not in visit:
                    visit.append([index, queue_index])
                    visit.append([queue_index, index])
                    n -= 1

    answer = n
    return answer