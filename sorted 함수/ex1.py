# sorted 함수 와 lamda 사용 예제 문제
numbers = list(map(int, input().split()))
result = sorted(numbers, key=lambda x : x )

for i in result:
    print(i, end=' ')