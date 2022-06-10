# 순열 예시
# 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
# {'A','B','C'}에서 두 개를 선택하여 나열하는 경우 : 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'
from itertools import permutations


data = ['A', 'B', 'C']
result = list( permutations(data, 3))
print(result)

# 조합 예시
# 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
# {'A','B','C'}에서 순서를 고려하지 않고 두 개를 뽑는 경우 : ('A', 'B'), ('A', 'C'), ('B', 'C')
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)