def nyrleikur():
    current_tile = 1.1
    s = 'You can travel: '
    coin = 0
    while current_tile != 3.1:
        if current_tile == 1.1:
            print(s + '(N)orth.')
            direction = ''
            while direction != 'N':
                direction = str(input("Direction: ")).upper()
                if direction == 'N':
                    current_tile = 1.2
                else:
                    print('Not a valid direction!')

        if current_tile == 1.2:
            k = input('Pull a lever (y/n): ')
            if k =='y':
                coin += 1
                print('You received 1 coins, your total is now ' + str(coin) + '.')
            print(s + '(N)orth or (E)ast or (S)outh.')
            direction = 'W'
            while direction != 'N' and direction != 'S' and direction != 'E':
                direction = str(input("Direction: ")).upper()
                if direction == 'N':
                    current_tile = 1.3
                elif direction == 'E':
                    current_tile = 2.2
                elif direction == 'S':
                    current_tile = 1.1
                else:
                    print('Not a valid direction!')

        if current_tile == 1.3:
            print(s + '(E)ast or (S)outh.')
            direction = ''
            while direction != 'E' and direction != 'S':
                direction = str(input("Direction: ")).upper()
                if direction == 'E':
                    current_tile = 2.3
                elif direction == 'S':
                    current_tile = 1.2
                else:
                    print('Not a valid direction!')

        if current_tile == 2.1:
            print(s + '(N)orth.')
            direction = ''
            while direction != 'N':
                direction = str(input("Direction: ")).upper()
                if direction == 'N':
                    current_tile = 2.2
                else:
                    print('Not a valid direction!')

        if current_tile == 2.2:
            k = input('Pull a lever (y/n): ')
            if k =='y':
                coin += 1
                print(' You received 1 coins, your total is now '+str(coin)+'.')
            print(s + '(S)outh or (W)est.')
            direction = ''
            while direction != 'W' and direction != 'S':
                direction = str(input("Direction: ")).upper()
                if direction == 'S':
                    current_tile = 2.1
                elif direction == 'W':
                    current_tile = 1.2
                else:
                    print('Not a valid direction!')

        if current_tile == 2.3:
            k = input('Pull a lever (y/n): ')
            if k =='y':
                coin += 1
                print('You received 1 coins, your total is now '+str(coin)+'.')
            print(s + '(E)ast or (W)est.')
            direction = ''
            while direction != 'E' and direction != 'W':
                direction = str(input("Direction: ")).upper()
                if direction == 'E':
                    current_tile = 3.3
                elif direction == 'W':
                    current_tile = 1.3
                else:
                    print('Not a valid direction!')

        if current_tile == 3.2:
            k = input('Pull a lever (y/n): ')
            if k =='y':
                coin += 1
                print('You received 1 coins, your total is now '+str(coin)+'.')
            print(s + '(N)orth or (S)outh.')
            direction = ''
            while direction != 'N' and direction != 'S':
                direction = str(input("Direction: ")).upper()
                if direction == 'N':
                    current_tile = 3.3
                elif direction == 'S':
                    current_tile = 3.1
                    print('Victory!')
                else:
                    print('Not a valid direction!')
        
        if current_tile == 3.3:
            print(s + '(S)outh or (W)est.')
            direction = ''
            while direction != 'S' and direction != 'W':
                direction = str(input("Direction: ")).upper()
                if direction == 'S':
                    current_tile = 3.2
                elif direction == 'W':
                    current_tile = 2.3
                else:
                    print('Not a valid direction!')

g = 'y'
while g == 'y':
    nyrleikur()
    g = input('Play again (y/n): ')