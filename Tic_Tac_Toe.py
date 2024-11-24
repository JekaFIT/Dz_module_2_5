def draw_area():
    for i in area:
        print(*i)
    print()
def check_winner():
    """
    Проверяет, есть ли победитель.
    Возвращает 'x', '0' или None.
    """
    for row in area:
        if row.count(row[0]) == 3 and row[0] != '*':
            return row[0]

    for col in range(3):
        if area[0][col] == area[1][col] == area[2][col] != '*':
            return area[0][col]

    if area[0][0] == area[1][1] == area[2][2] != '*':
        return area[0][0]
    if area[0][2] == area[1][1] == area[2][0] != '*':
        return area[0][2]

    return None
area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print('Добро пожаловать в крестики-нолики')
print("----------------------------------")
draw_area()
for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = '0'
        print('Ходят нолики ')
    else:
        turn_char = 'x'
        print('Ходят крестики ')
    row = int(input('Введите номер сторки(1,2,3) ')) - 1
    colum = int(input("Введите номер столбца (1,2,3) ")) - 1
    if area[row][colum] == '*':
         area[row][colum] = turn_char
    else:
        print('Ячейка занята и вы пропускаете ход')
        continue
    draw_area()
    winner = check_winner()
    if winner:
        print(f'Поздравляем! Победил {winner}!')
        break
else:
    print("Ничья!")



