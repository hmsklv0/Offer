def count_people(n, k, t, a):
    people = sorted(zip(t, a))  # 按到达时间升序排序
    count = 0
    end_time = 0
    print(people)

    for i in range(n):
        ei = people[i][0] + k


        if end_time <= people[i][0]:
            count += 1
            end_time = ei if ei <= people[i][0] + people[i][1] else people[i][0] + people[i][1]
        elif end_time <= people[i][0] + people[i][1]:
            count += 1
            end_time = ei if ei <= end_time + (people[i][0] + people[i][1] - end_time) else end_time + (people[i][0] + people[i][1] - end_time)

    return count


def count_people2(n, k, t, a):
    people = sorted(zip(t, a))  # 按到达时间升序排序
    count = 0
    # 上一个人结束时间
    end_time = 0
    print(people)

    for i in range(n):
        ai = people[i][0] + people[i][1]

        if end_time <= people[i][0]:
            # 直接开始发放盲盒
            if people[i][0] + k <= ai:
                # 有机会
                if end_time + k <= ai:
                    # 实际可行
                    count += 1
                    if end_time <= people[i][0]:
                        end_time = people[i][0] + k
                    else:
                        end_time = end_time + k
                    continue

        elif end_time > people[i][0]:
            # 开始排队

            if people[i][0] + k <= ai:
                # 有机会
                if end_time + k <= ai:
                    # 实际可行
                    count += 1
                    if end_time <= people[i][0]:
                        end_time = people[i][0] + k
                    else:
                        end_time = end_time + k
                    continue




    return count
n = 5
k = 2
t = [1, 2, 3, 4, 5]
a = [5, 4, 3, 2, 1]
ans = count_people2(n, k, t, a)
print(ans)  # 输出 3
