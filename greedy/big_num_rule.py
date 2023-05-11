'''
제목 : 큰 수의 법칙
분류 : Greedy
난이도 : 하

설명 :
  배열(크기:N)을 입력 값으로 받아 주어진 수를 M 번 이용해서 가장 큰 수를 만드는 것이다. 단 하나의 수를 연속해서 K번을 초과하여 더할 수 없다.
  입력값 :
    첫째 줄 : N, M, K
    둘째 줄 : 1 이상 10000 이하인 자연수 배열

Input:
5 8 3
2 4 5 4 6

Output:
46
'''

N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
biggest = data[-1]
sec_biggest = data[-2]

count = M // (K + 1)

result = 0
result += sec_biggest * count
result += biggest * (M-count)
print(result)