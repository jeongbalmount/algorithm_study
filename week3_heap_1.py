import heapq


def solution(scoville, K):
    operation = 0   # K값을 넘을 스코빌값을 찾는 작업 횟수

    heapq.heapify(scoville) # heapify가 되지 않은 상태의 리스트를 받을수도 있기 때문에 heapify

    # K값을 넘을 스코빌값 찾는 While 문
    while len(scoville) > 1:
        # heap에서 가장 작은 값(루트값) 지우기
        min1 = heapq.heappop(scoville)  # 가장 작은 값 빼기
        min2 = heapq.heappop(scoville)  # 두번째 작은 값 빼기
        more_than_K_value = min1 + (min2 * 2)   # 더한 값 변수에 넣기
        # 루트자리에 more_tahn_K_value 넣고 다시 힙정렬
        heapq.heappush(scoville, more_than_K_value) # heap에 넣기
        operation += 1

        if scoville[0] > K:
            return operation    # 리스트에서 가장 값이 작은 값보다 K가 작으면 return

    return -1   # K값 이상의 수가 힙에 없을때 -1 리턴

