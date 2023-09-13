from google.colab import drive
drive.mount('/content/drive')

# 5 A
money = 18853
f = "1,3,5,6,8,12,15"
coinsStr = f.split(",")
coins = len(coinsStr)*[0]
for i in range(len(coinsStr)):
    coins[i] = int(coinsStr[i])

print(coins)

def MinimumChange(money, coins):
    minnumcoins = (money + 1) * [0]
    print(minnumcoins)
    for m in range(1, money + 1):
        minnumcoins[m] = m + 1  # basically the same as Inf since coins can't be <= 0
        for coin in coins:
            if m >= coin:
                if minnumcoins[m - coin] + 1 < minnumcoins[m]:
                    minnumcoins[m] = minnumcoins[m - coin] + 1
    print(minnumcoins)
    return minnumcoins[money]

print(MinimumChange(money, coins))
