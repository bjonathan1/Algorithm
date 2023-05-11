'''
제목 : 1이 될 때까지
분류 : Greedy
난이도 : 하

설명 :
  입력값 N이 1이 될 때 까지 두 가지 옵션 (N에서 1을 뺀다, N을 K로 나눈다)를 수행하여 최소횟수로 1을 만들기.

  입력값 :
    첫째 줄 : N (2 <= N <= 100,000), K (2 <= K <= 100,000)

Input:
25 5

Output:
2

'''
N, K = map(int, input().split())
count = 0

while N > 1:
  if N % K == 0 :
    N = N // K
    count += 1
  else:
    N -= 1
    count += 1

print(count)