"""
Напишите программу, которая принимает на стандартный вход
список игр футбольных команд с результатом матча и
выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15

Sample Output:
Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
"""

n = int(input())
match_results = []
teams = set()
for i in range(n):
    match_results.append(input().split(';'))
    teams.add(match_results[i][0])
    teams.add(match_results[i][2])
championship_table = {team: [0, 0, 0, 0, 0] for team in teams}

# match_results = [['Спартак', '9', 'Зенит', '10'],
#                  ['Локомотив', '12', 'Зенит', '3'],
#                  ['Спартак', '8', 'Локомотив', '15']]
# teams = {'Зенит', 'Спартак', 'Локомотив'}
# championship_table = {team: [0, 0, 0, 0, 0] for team in teams}
# print(championship_table)

for match in match_results:
    championship_table[match[0]][0] += 1
    championship_table[match[2]][0] += 1
    if int(match[1]) == int(match[3]):
        championship_table[match[0]][2] += 1
        championship_table[match[0]][4] += 1
        championship_table[match[2]][2] += 1
        championship_table[match[2]][4] += 1
    elif int(match[1]) < int(match[3]):
        championship_table[match[0]][3] += 1
        championship_table[match[2]][1] += 1
        championship_table[match[2]][4] += 3
    else:
        championship_table[match[0]][1] += 1
        championship_table[match[0]][4] += 3
        championship_table[match[2]][3] += 1
# print(championship_table)

for team, result in championship_table.items():
    print(team, ':', sep='', end='')
    print(*result)
