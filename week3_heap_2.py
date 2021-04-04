import heapq


def solution(operations):
    operation_list = []
    for operation in operations:
        # Order부와 Value부를 order와 after로 나눠 문자열 추출
        order_data = operation[0:1]
        after_data = int(operation[2:])

        if order_data is 'D' and len(operation_list) is not 0:
            # 최대 원소를 뽑아낼때 힙정렬을 이용
            if after_data is 1:
                operation_list = heap_sort(operation_list)
                operation_list.pop()
            # 최소원소는 루트 원소를 뽑는다
            else:
                heapq.heappop(operation_list)
            # I일때는 heap에 원소추가
        elif order_data is 'I':
            heapq.heappush(operation_list, after_data)

    if len(operation_list) is 0:
        return [0, 0]

    # 힙정렬을 통해 가장 큰값, 작은값 뽑아내기
    sorted_list = heap_sort(operation_list)
    min_value = sorted_list[0]
    max_value = sorted_list.pop()
    answer = [max_value, min_value]
    return answer


# 힙정렬
def heap_sort(heap_list):
    sorted_list = []
    while heap_list:
        sorted_list.append(heapq.heappop(heap_list))
    return sorted_list


