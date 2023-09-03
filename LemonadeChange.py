def lemonadeChange(bills):
    # is_there_5 = False
    # is_there_10 = False
    # change = []
    # for i in range(0, len(bills)):
    #     if bills[i] == 5:
    #         change.append(bills[i])
    #     elif bills[i] == 10:
    #         change.append(bills[i])
    #         for j in range(0, len(change)):
    #             if change[j] == 5:
    #                 change[j] = 0
    #                 is_there_5 = True
    #                 break
    #             else:
    #                 is_there_5 = False
    #         if not is_there_5:
    #             return False
    #     elif bills[i] == 20:
    #         change.append(bills[i])
    #         for j in range(0, len(change)):
    #             if change[j] == 5:
    #                 change[j] = 0
    #                 is_there_5 = True
    #                 break
    #             else:
    #                 is_there_5 = False
    #         for j in range(0, len(change)):
    #             if change[j] == 10:
    #                 change[j] = 0
    #                 is_there_10 = True
    #                 break
    #             else:
    #                 is_there_10 = False
    #         if is_there_5 and is_there_10:
    #             continue
    #         else:
    #             return False
    # return True
    change = []
    for i in range(0, len(bills)):
        if bills[i] == 5:
            change.append(bills[i])
        elif bills[i] == 10:
            change.append(bills[i])
            if change.count(5) >= 1:
                change[change.index(5)] = 0
            else:
                return False
        elif bills[i] == 20:
            if change.count(5) >= 1 and change.count(10) >= 1:
                change[change.index(5)] = 0
                change[change.index(10)] = 0
            elif change.count(5) >= 3:
                for k in range(0, 3):
                    change[change.index(5)] = 0
            else: 
                return False
    return True
        
bills = [5,5,10,10,20]
print(lemonadeChange(bills))

                    