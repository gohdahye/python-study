# 100 이하의 숫자는 입력받은 숫자가 등차수열이어서
# 100이상부터 for문 돌게 하기

# 기록 이유:
# num = 100일때 num_list = [1, 0, 0] 이런 표기를 하고 싶을때


def hansu(num):
    hansu = 99
    if num < 100:
        return num
    else:
        for i in range(100, num+1):
            num_list = list(map(int, str(i)))
            if (num_list[0]-num_list[1]) == (num_list[1]-num_list[2]):
                hansu += 1  # x의 각 자리가 등차수열이면 한수
        return hansu

num = int(input())
print(hansu(num))