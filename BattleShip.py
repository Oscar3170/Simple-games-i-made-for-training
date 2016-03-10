from random import randint
from colorama import Fore, Back, Style

print('')
modo = int(input('Esse é um jogo de batalha naval, se quiser jogar um modo simples digite "0", se quiser jogar um modo customizavel digite "1"! '))

if modo == 0:
    board = []
    for x in range(5):
        board.append(["O"] * 5)

    def print_board(board):
        for row in board:
            print (Fore.BLUE + ' '.join(row))
        print(Style.RESET_ALL)

    def random_row(board):
        return randint(0, len(board) - 1)
        
    def random_col(board):
        return randint(0, len(board[0]) - 1)

    def random_row2(board):
        return randint(0, len(board) - 1)
        if naviu2 == 0:
            naviu2 = (str(naviu2), str(randint(1, naviu2)))
        elif naviu2 == 4:
            naviu2 = (str(naviu2), str(randint(3, naviu2)))
        else:
            naviu2 = (str(naviu2), str(randint(naviu2 - 1, naviu2 + 1)))
        return naviu2

    def random_col2(board):
        navio2 = randint(0, len(board[0]) - 1)
        if navio2 == 0:
            navio2 = (str(navio2), str(randint(1, navio2)))
        elif navio2 == 4:
            navio2 = (str(navio2), str(randint(3, navio2)))
        else:
            navio2 = (str(navio2), str(randint(navio2 - 1, navio2 + 1)))
        return navio2

    print (' ')
    print ('Você tem 4 turnos para acertar o navio!')
    print ('Escolha dois numeros entre 1 e 5!')
    ship_row = random_row(board)
    ship_col = random_col(board)
    ship_col2 = random_col2(board)
    ship_row2 = random_row2(board)
    #print (ship_row)
    #print (ship_col)
    print (ship_row2)
    print (ship_col2)
    guess_row = ''
    guess_col = ''
    turn = 1
    guess = (guess_row, guess_col)
    right_guess = (ship_row, ship_col)
    print (int(right_guess[0]) + 1, int(right_guess[1]) + 1) 
    while guess != right_guess and turn < 5:

        print (' ')
        print (' ')
        print (('Turn: ') + str(turn))
        print (' ')
        guess_row = int(input("Advinhe a fileira: "))-1
        guess_col = int(input("Advinhe a coluna: "))-1
        guess = (guess_row, guess_col)
        print (' ')

        if  guess_row == ship_row and guess_col == ship_col:
            print ("Parabéns! Você afundou o navio!")
            print (' ')

        elif guess_row not in range(5) or guess_col not in range(5):
            if turn != 5:
                print ("Isso não é nem no oceano.")
                print (' ')
                print (print_board(board))

        elif board[guess_row][guess_col] == (Fore.RED + 'X' + Fore.BLUE):
            if turn != 5:
                print ("Você já acertou esse lugar!.")
                print (' ')
                print (print_board(board))

        else:
            if turn != 5:
                print ("Você errou o navio!")
                print (' ')
                board[guess_row][guess_col] = (Fore.RED + 'X' + Fore.BLUE)
                print (print_board(board))
                turn += 1

    if turn == 5:
        print (' ')
        print ('You lost!')
        print (' ')
        
elif modo == 1:
    print(' ')
    board_size = str(input("Quanto por quanto você quer que seja o seu tabuleiro?(use 4X4 por exemplo, e menor que 10x10) ")) + 'l'
    while 'x' in board_size[2:].lower() or board_size[3] != 'l' or board_size[1].lower() != 'x':
        board_size = str(input("Menor que 10X10! "))
        board_size += 'l'
    board = []
    turns = int(input('Quantos turnos você quer ter? '))

    for x in range(int(board_size[0])):
        board.append(["O"] * int(board_size[2]))

    def print_board(board):
        for row in board:
            print(Fore.BLUE + ' '.join(row))
        print(Style.RESET_ALL)
    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    print(' ')
    print_board(board)
    print (' ')
    print ('Você tem ' + str(turns) + ' turnos para fundar um navio!')
    print ('Escolha as cordenadas onde você pensa que esta o navio!')
    ship_row = random_row(board)
    ship_col = random_col(board)
    #print (ship_row)
    #print (ship_col)
    guess_row = ''
    guess_col = ''
    turn = 0
    guess = (guess_row, guess_col)
    right_guess = (ship_row, ship_col)
    #print(' ')
    #print (int(right_guess[0]) + 1, int(right_guess[1]) + 1) 

    while guess != right_guess and turn < turns:
        print (' ')
        print (' ')
        print (('Turno: ') + str(turn + 1))
        print (' ')
        guess_row = int(input("Advinhe a fileira: "))-1
        guess_col = int(input("Advinhe a coluna: "))-1
        guess = (guess_row, guess_col)
        print (' ')

        if  guess == right_guess:
            print ("Parabéns! Você afundou o navio!")
            print (' ')

        elif guess_row not in range(int(board_size[0])) or guess_col not in range(int(board_size[2])):
            if turn != 5:
                print ("Isso não é nem no oceano.")
                print (' ')
                print_board(board)

        elif board[guess_row][guess_col] == (Fore.RED + 'X' + Fore.BLUE):
            if turn != turns:
                print ("Você já acertou esse lugar!")
                print (' ')
                print_board(board)

        else:
            if turn != turns:
                print ("Você errou o navio!")
                print (' ')
                board[guess_row][guess_col] = (Fore.RED + 'X' + Fore.BLUE)
                print_board(board)
                turn += 1

    if turn == turns:
        print (' ')
        print ('Você perdeu!')
        print (' ') 

