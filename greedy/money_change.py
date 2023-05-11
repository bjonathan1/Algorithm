'''
그리디 알고리즘의 기본 
거스름 돌려주기 500, 100, 50, 10
'''
N = int(input()) #거스름돈 입력값
count = 0 # 동전 개수

coin_types = [500, 100, 50, 10] #동전 종류
for coin in coin_types: 
  count += N // coin
  N %= coin

print(count)