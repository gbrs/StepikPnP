"""
Простейшая система проверки орфографии может быть основана на использовании
списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
На вход программе первой строкой передаётся количество d известных нам слов,
после чего на d строках указываются эти слова. Затем передаётся количество
l строк текста для проверки, после чего l строк текста.
Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта
регистра.

Sample Input:
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:
stepic
champignons
the
"""

orthographic_dictionary = set()
spelling_mistakes = set()
for _ in range(int(input())):
    orthographic_dictionary.add(input().lower())

for _ in range(int(input())):
    for word in input().lower().split():
        if word not in orthographic_dictionary:
            spelling_mistakes.add(word)

print(*spelling_mistakes, sep='\n')
