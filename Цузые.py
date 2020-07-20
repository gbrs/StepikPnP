import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.disabled = False
logging.debug(f'')

with open('Text.txt', 'r', encoding='utf-8') as txt_file:
    s_in = txt_file.readlines()
logging.debug(s_in)
# Формируем матрицу оценок
s = []
for i in range(len(s_in)):
    s.append(list(map(int, s_in[i].strip('\n').split(';')[1:])))
logging.debug(s)


with open('Out.txt', 'w') as txt_file:
    # Пишем среднюю оценку каждого абитуриента
    for i in s:
        txt_file.write(str(sum(i) / len(i)) + '\n')
    #

    # Пишем средние баллы по всем абитуриентам
    for i in range(len(s[0])):
        score = 0
        for j in range(len(s)):
            score += s[j][i]
        txt_file.write(str(score / len(s)) + ' ')
    #
