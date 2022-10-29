def tic():
    print('\nWelcome to tic tac toe')
    print('the respective number corresponding to the position are as follows:')
    print('7|8|9')
    print('4|5|6')
    print('1|2|3')
    print('Player one will be given O')
    print('so choose wisely')
    print('Game begins')
    print()

    a = b = c = d = e = f = g = h = i = "_"
    v = 1
    l = "X"
    o = "O"
    global x
    x = 0

    # print(a, "|", b, "|", c)
    # print(d, "|", e, "|", f)
    # print(g, "|", h, "|", i)

    while x < 9:
        if v % 2 == 0:
            n = int(input('CHANCE OF PLAYER 2 '))

            if n == 1:
                if g == o:
                    pass
                else:
                    g = l
                    x += 1
                    v += 1
            if n == 2:
                if h == o:
                    pass
                else:
                    h = l
                    x += 1
                    v += 1
            if n == 3:
                if i == o:
                    pass
                else:
                    i = l
                    x += 1
                    v += 1
            if n == 4:
                if d == o:
                    pass
                else:
                    d = l
                    x += 1
                    v += 1
            if n == 5:
                if e == o:
                    pass
                else:
                    e = l
                    x += 1
                    v += 1
            if n == 6:
                if f == o:
                    pass
                else:
                    f = l
                    x += 1
                    v += 1
            if n == 7:
                if a == o:
                    pass
                else:
                    a = l
                    x += 1
                    v += 1
            if n == 8:
                if b == o:
                    pass
                else:
                    b = l
                    x += 1
                    v += 1
            if n == 9:
                if c == o:
                    pass
                else:
                    c = l
                    x += 1
                    v += 1
        else:
            n = int(input('CHANCE OF PLAYER 1 '))
            if n == 1:
                if g == l:
                    pass
                else:
                    g = o
                    x += 1
                    v += 1
            if n == 2:
                if h == l:
                    pass
                else:
                    h = o
                    x += 1
                    v += 1
            if n == 3:
                if i == l:
                    pass
                else:
                    i = o
                    x += 1
                    v += 1
            if n == 4:
                if d == l:
                    pass
                else:
                    d = o
                    x += 1
                    v += 1
            if n == 5:
                if e == l:
                    pass
                else:
                    e = o
                    x += 1
                    v += 1
            if n == 6:
                if f == l:
                    pass
                else:
                    f = o
                    x += 1
                    v += 1
            if n == 7:
                if a == l:
                    pass
                else:
                    a = o
                    x += 1
                    v += 1
            if n == 8:
                if b == l:
                    pass
                else:
                    b = o
                    x += 1
                    v += 1
            if n == 9:
                if c == l:
                    pass
                else:
                    c = o
                    x += 1
                    v += 1

        print(a, "|", b, "|", c)
        print(d, "|", e, "|", f)
        print(g, "|", h, "|", i)

        if a == b == c != "_" or d == e == f != "_" or g == h == i != "_" or a == d == g != "_" or b == e == h != "_" or c == f == i != "_" or a == e == i != "_" or c == e == g != "_":
            if v % 2 == 0:
                print('Player 1 is the winner')
            else:
                print('Player 2 is the winner')
            break


tic()
if x == 9:
    print("game is tie")

    ch = int(input("enter 1 to play again and 0 to stop playing"))
    if ch == 1:
        tic()
    else:
        exit()
else:

    ch = int(input("enter 1 to play again and 0 to stop playing"))
    if ch == 1:
        tic()
    else:
        exit()


