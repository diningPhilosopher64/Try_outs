import pprint as pp

board = {'top-left': ' ', 'top-middle': ' ', 'top-right': ' ',
         'middle-left': ' ', 'middle-middle': ' ', 'middle-right': ' ',
         'bottom-left': ' ', 'bottom-middle': ' ', 'bottom-right': ' '
         }



def printboard(board):
    print(board['top-left'] + '|' + board['top-middle'] + '|' + board['top-right'])
    print('-+-+-')
    print(board['middle-left'] + '|' + board['middle-middle'] + '|' + board['middle-right'])
    print('-+-+-')
    print(board['bottom-left'] + '|' + board['bottom-middle'] + '|' + board['bottom-right'])


print('Preparing the board....')
print('The board is ready ..!')

printboard(board)

print('Press 1 to choose X or 2 to choose O')
l = input()
turn = ''

if l == '1':
    turn = 'X'
else:
    turn = 'O'


print('You chose ' + turn)

for i in range(9):
    printboard(board)
    print('Place '+turn+' at ?')
    move = input()
    board[move] = turn


    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'



printboard(board)
