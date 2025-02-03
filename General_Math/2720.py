#세탁소 사장 동혁

def CountCoin(coin,cent):
    count=cent//coin
    cent%=coin
    arr.append(count)
    return cent

T=int(input())
coins= [25, 10, 5, 1]

for i in range(T):
    arr=[]
    cent=int(input())

    for coin in coins:
        cent=CountCoin(coin,cent)

    print(' '.join(map(str,arr)))

