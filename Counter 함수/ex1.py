# Counter 함수 예제
# Counter는 등장 횟수를 세는 기능을 제공

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['red'])
print(counter['green'])

print(dict(counter))