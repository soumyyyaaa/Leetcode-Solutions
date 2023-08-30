def judgeCircle(moves):
    moves = list(moves)
    count_U = 0
    count_D = 0
    count_R = 0
    count_L = 0
    for move in moves:
        if move == "U":
            count_U += 1
        elif move == "D":
            count_D += 1
        elif move == "R":
            count_R += 1
        elif move == "L":
            count_L += 1
    if count_L == count_R and count_U == count_D:
        return True
    else: 
        return False
    
moves = "LLRRUUUDDD"
print(judgeCircle(moves))