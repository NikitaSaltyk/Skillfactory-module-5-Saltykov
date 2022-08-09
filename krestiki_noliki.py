def greeting():
    print('___________________________________________________')
    print('                                                   ')
    print('    Предлагаем сыграть в игру Крестики-Нолики')
    print('___________________________________________________')
    print('Необходимо по очереди вводить координаты поля x, y,')
    print('где x - строка, y - столбец')
    print('___________________________________________________')


field = [[''] * 3 for i in range(3)]
def show():
    print(f'  0 1 2')
    for i in range(3):
        print(f'{i} {field[i][0]}  {field[i][1]}  {field[i][2]}')

def ask():
    while True:
        x,y= input('Ваш ход:').split()
        x, y = int(x), int(y)
        
        if 0>x or x>2 or 0>y or y>2:
            print('Ошибка интервала координат')
            continue
        if field[x][y] != '':
            print('Клетка уже занята')
            continue
        return x, y

def win():
    win_var = (((0, 0), (0, 1), (0, 2)), 
                ((1, 0), (1, 1), (1, 2)), 
                ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), 
                ((0, 0), (1, 1), (2, 2)), 
                ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), 
                ((0, 2), (1, 2), (2, 2)))
    for var in win_var:
        a = var[0]
        b = var[1]
        c = var[2]
        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] !='':
            print(f'победил {field[a[0]][a[1]]}')
            return True
    return False
    
greeting()
#порядок ходов
count = 0
while True:
    count+= 1
    show()
    
    if count % 2 == 1:
        print('Поставьте крестик')
    else:
        print('Поставьте нолик')
#ввод координат - функция ask    
    x, y = ask()
    
#выбор введенного значка
    if count % 2 ==1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if win():
        break

    if count == 9:
        print('Результат игры - ничья')
        break