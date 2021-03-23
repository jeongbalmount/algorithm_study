

def solution(prices):

    price_not_down = []

    for i in range(0, len(prices)):
        is_price_not_down = 0
        low_value_found = False
        k = i + 1
        # 다음 주식 가격이 비교 가격보다 낮지 않고 다음 가격이 전체 가격 리스트 길이보다 길지 않을때
        while low_value_found is False and k <= len(prices) - 1:
            is_price_not_down += 1 # 값이 내려가지 않는다 -> 1초 추가
            if prices[i] > prices[k]:
                low_value_found = True # 만약 값이 내려 갔다면 while문 중단 시킨다.
            k += 1

        price_not_down.append(is_price_not_down) # 언제 값이 내려갔는지 기록하는 리스트 업데이트

    answer = price_not_down
    return answer

answer = solution([1, 2, 3, 2, 3, 1])

print(answer)

# 정말 오랜만에 알고리즘 문제를 푸니 어려웠었다. 일단 첫번째 문제에서 문제가 무엇을 말하는지부터 이해를 하지 못하고
# 헤멨던것 같다. 일단 처음에 문제를 제대로 이해하고 어떤 메소드, 변수가 필요하고 어떤식으로 조합해야하는지를 정확히
# 인지하고 문제 풀이를 들어가야겠다.. 두번째 문제는 문제 자체가 무슨말인지 몰랐다가 나중에 사람들이 적어 놓은 힌트를 보고
# 겨우 문제를 풀수 있었다;;