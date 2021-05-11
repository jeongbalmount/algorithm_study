
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)

    while len(people) > 0:
        # 가장 큰수와 가장 작은 수를 더하고 비교하여 limit보다 크다면 가장 큰수만 보낸다.
        if len(people) > 1 and people[0] + people[-1] <= limit:
            people.pop(-1)  # 두개를 더했는데도 limit 보다 작다면 둘다 보내기
        people.pop(0)
        answer += 1
    return answer


