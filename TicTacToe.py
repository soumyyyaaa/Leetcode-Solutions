def tictactoe(moves):
    board = [['','',''],['','',''],['','','']]
    for i in range(0, len(moves)):
        r = moves[i][0]
        c = moves[i][1]
        board[r][c] = 'X' if i % 2 == 0 else 'O'
        
    if (board[0][0] == board[0][1] == board[0][2] == 'X') or \
       (board[1][0] == board[1][1] == board[1][2] == 'X') or \
       (board[2][0] == board[2][1] == board[2][2] == 'X') or \
       \
       (board[0][0] == board[1][0] == board[2][0] == 'X') or \
       (board[0][1] == board[1][1] == board[2][1] == 'X') or \
       (board[0][2] == board[1][2] == board[2][2] == 'X') or \
       \
       (board[0][0] == board[1][1] == board[2][2] == 'X') or \
       (board[2][0] == board[1][1] == board[0][2] == 'X'):
        return 'A'
    elif (board[0][0] == board[0][1] == board[0][2] == 'O') or \
       (board[1][0] == board[1][1] == board[1][2] == 'O') or \
       (board[2][0] == board[2][1] == board[2][2] == 'O') or \
       \
       (board[0][0] == board[1][0] == board[2][0] == 'O') or \
       (board[0][1] == board[1][1] == board[2][1] == 'O') or \
       (board[0][2] == board[1][2] == board[2][2] == 'O') or \
       \
       (board[0][0] == board[1][1] == board[2][2] == 'O') or \
       (board[2][0] == board[1][1] == board[0][2] == 'O'):
        return 'B'
    elif len(moves) < 9:
        return 'Pending'
    else:
        return 'Draw'

moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1]]
print(tictactoe(moves))
