field=[['_','_','_'],
       ['_','_','_'],
       ['_','_','_']]
field=[['_']*3 for _ in range(3)]
print(field)

print(*field)
print(' 0 1 2')
for i in range(len(field)):
    print(str(i), *field[i])
def show_field(f):
    print(' 0 1 2')
    for i in range(len(field)):
        print(str(i)+' '+' '.join(field[i]))
show_field(field)

def users_input(f):
    while True:
        place=input('Сделай ход: ').split()
        if len(place)!=2:
            print('введи 2 координаты')
            continue
        x,y=map(int,place)
        if not(place[0].isdigit() and place[i].isdigit()):
            print('введите числа')
            continue
        x,y=map(int,place)
        if not(x>=0 and x<3 and y>=0 and y<3):
            print('Вышли из диапозона')
            continue
        if f[x][y]!='-':
            print('Клетка занята')
            continue
        break
        return x,y
users_input(field)

count=0
while True:
    if count%2==0:
        user='x'
    else:
        user='0'
    show_field(field)
    x,y=users_input(field)
    field[x][y]=user
    if count==9:
        print('ничья')
    if win_v1(field,user):
        print('выйграл {user}')
        show_field(field)
        break
    count+=1

def win_v1(f, user):
    def check_line(a1,a2,a3,user):
        if a1==user and a2==user and a3==user:
            return True
    for n in range(3):
        if check_line(f[n][0],f[n][1], f[n][2], user) or \
        check_line(f[0][n], f[1][n], f[2][n], user) or \
            check_line(f[0][0], f[1][1], f[2][2], user) or\
        check_line(f[2][0], f[1][1], f[0][2], user):
            return True
    return False
def win_v2(f, user):
    win_cord = (((0,0), (0,1), (0,2)),((1,0), (1,1), (1,2)),((2,0), (2,1), (2,2)),
                ((0,2),(1,1), (2,0)),((0,0), (1,1), (2,2)), ((0,0), (1,0), (2,0)),
                ((0,1), (1,1), (2,1)), ((0,2),(1,2), (2,2)))
    for cord in win_cord:
        symbols= []
        for c in cord:
            symbols.append(f[c[0]][c[1]])
        if symbols ==[user, user, user]:
            return True
    return False

def win_v2(f,user):
    f_list=[]
    for l in f:
        f_list+=1
    positions=[[0,1,2],[3,4,5],[6,7,8],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    indices= set([i for i, x in enumerate(f_list) if x== user])
    for p in positions:
        if len(indices.intersection(set(p)))==3:
            return True
    return False




