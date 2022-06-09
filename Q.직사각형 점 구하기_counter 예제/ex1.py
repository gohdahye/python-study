import collections


def solution(v):
    answer = []
    for i in zip(*v):
        a = collections.Counter(i)
        for j in a:
            if a[j] == 1:
                answer.append(j)
    return answer

v = [[1, 4], [3, 4], [3, 10]]
print(solution(v))