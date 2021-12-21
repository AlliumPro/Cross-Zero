print("~~~~~~Cross-Zero~~~~~~")
print("<<To put a cross or zero, type 2 numbers: line and row. Crossers are the first!>>")
field = [["|?(11)|", "|?(12)|", "|?(13)|"], ["|?(21)|", "|?(22)|", "|?(23)|"], ["|?(31)|", "|?(32)|", "|?(33)|"]]
used = []
for i in range(9):
    used.append([0] * 2)
s = 0
while used.count([0,0])!=0:
        for i in field:
            print(*i)
        print("What's your next move?")
        if s%2==0:
            print("Where'd you like to put 'X'?")
        else:
            print("Where'd you like to put '0'?")
        w=str(input()).replace(' ', '')
        while len(w)!=2:
            print('Type only 2 numbers (without any other symbols)')
            w = str(input()).replace(' ', '')
        while w.isdigit()!=True:
            print('Type only numbers')
            w = str(input()).replace(' ', '')

        i=int(w[0])
        j=int(w[1])
        if i>3 or j>3:
            print("There's no such place on the field :(")
        else:
            u = [i, j]
            if used.count(u) == 0:
                if s % 2 == 1:
                    field[i - 1][j - 1] = "|   0   |"
                    used[s] = u
                    s += 1
                else:
                    field[i - 1][j - 1] = "|   X   |"
                    used[s] = u
                    s += 1
            else:
                print("It's already used!")
            if (field[0][0]==field[0][1] and field[0][1]==field[0][2]) or (field[1][0]==field[1][1] and field[1][1]==field[1][2]) or (field[2][0]==field[2][1] and field[2][1]==field[2][2]) or (field[0][0]==field[1][0] and field[1][0]==field[2][0]) or (field[0][1]==field[1][1] and field[1][1]==field[2][1]) or (field[0][2]==field[1][2] and field[1][2]==field[2][2]) or (field[0][0]==field[1][1] and field[1][1]==field[2][2]) or (field[0][2]==field[1][1] and field[1][1]==field[2][0]):
                if s % 2 == 0:
                    print("The game is over! Zero wins!")
                    for i in field:
                        print(*i)
                    break
                else:
                    print("The game is over! Cross wins!")
                    for i in field:
                        print(*i)
                    break
