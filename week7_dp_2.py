def dp_function(dp_list, now_m, now_n, puddles):
    puddle_compare_list = [now_m, now_n]
    if puddle_compare_list in puddles:
        return dp_list
    else:
        if now_n == 0:
            dp_list[0][now_m] = 1
        elif now_m == 0:
            dp_list[now_n][0] = 1
        else:
            dp_list[now_n][now_m] = dp_list[now_n - 1][now_m] + dp_list[now_n][now_m - 1]

        return dp_list


puddles = [[2, 2]]
dp_list = []
for i in range(3):
    list = []
    for j in range(4):
        list.append(0)
    dp_list.append(list)

for i in range(3):
    for j in range(4):
        dp_list = dp_function(dp_list, j, i, puddles)

