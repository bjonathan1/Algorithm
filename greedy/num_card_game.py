'''
제목 : 숫자 카드 게임
분류 : Greedy
난이도 : 하

설명 :
  N * M 의 카드들이 놓여있을때, 각 행 (N)의 가장 낮은 숫자 중 - 그 중 가장 큰 수를 뽑아야한다.

  입력값 :
    첫째 줄 : N, M
    둘째 줄 부터 : N개 줄에 걸쳐 각 카드 적힌 숫자 주어진다. (카드 수 : 1 이상 10,000 이하의 자연수)

Input:
3 3
3 1 2
4 1 4
2 2 2

Output:
2

'''
N, M = map(int, input().split())
cardList = list()
result = 0

for _ in range(N):
  data = list(map(int, input().split()))
  min_value = min(data)
  result = max(result, min_value)

print(result)