def maximumWealth(accounts):
    sumMoney  = 0
    for account in accounts:
        if sumMoney < sum(account):
            sumMoney = sum(account)
    
    return sumMoney

accounts = [[1,5],[7,3],[3,5]]
print(maximumWealth(accounts))