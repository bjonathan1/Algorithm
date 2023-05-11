import sys

'''
자료
'''
# 지수 표현식
a = 1e9
print(a)

# 소수 자리 주
a = 0.3 + 0.6
print(round(a, 4))

#Lambda Expression으로 사용한 함수
print((lambda a, b: a + b)(3, 7))

'''
리스트
'''
# m * n 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

# 리스트 컴프리헨션
array = [i for i in range(20) if i % 2 == 1]

'''
입출력 관리
'''
# 띄워쓰기로 Input 받을 때
#input : 65 90 75 34 99
data = list(map(int, input().split()))

#input : 3 5 7
n, m, k = map(int, input().split()) # 각 변수에 넣음

#문자열 입력받기
data = sys.stdin.readline().rstrip()

# 변수 문자열 출력
answer = 7
print("정답은 " + str(answer) + "입니다.")
print(f"정답은 {answer}입니다.") # f-string 문법 (파이썬 3.6 이상 부터)

'''
파이썬 라이브러리 활용 
'''
# 내장 함수
result = sum([1, 2, 3, 4, 5])
result = min([7, 3, 5, 2])
result = max([7, 3, 5, 2])
result = eval("(3 + 5) * 7") # 문자열 수식 계산
result = sorted([9, 1, 8, 5, 4], reverse=True)
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse=True) # 튜플의 두번째 원소로 정렬

data = [9, 1, 8, 5, 4]
data.sort() #그냥 sort는 이렇게

#itertools
from itertools import permutations #순열
from itertools import combinations # 조합
from itertools import product # 순열 중복 허용
from itertools import combinations_with_replacement #조합 중복 허용
data = ['A', 'B', 'C']
result = list(permutations(data, 3))                # 모든 순열 구하기 (r = 3)
result = list(combinations(data, 2))                # 모든 조합 구하기 (r = 2)
result = list(product(data, repeat=2))              # 두개 뽑는 모든 순열 구하기 (중복허용)
result = list(combinations_with_replacement(data, 2)) # 두개 뽑는 모든 조합 구하기 (중복허용)

# Heap Queue
import heapq
h = []
answer = []
for value in [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]:
    heapq.heappush(h, value)
for _ in range(len(h)):
    answer.append(heapq.heappop(h))
print(answer)

# Bisect 배열의 특정 원서 위치 찾을 때 사용
from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))


#튜플 만들기
a = (1, 2, 3, 4) #값 변경 불가
print(a)

#Dictionary
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
if '사과' in data:
    print('사과')
print(data)

#집합(SET) 자료형
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

data = {1, 1, 2, 3, 4, 4, 5} #두 개의 집합으로 합집합, 교집합, 차집합 만들 수 있음
data.add(4)
data.update([5, 6])
data.remove(3)
print(data)