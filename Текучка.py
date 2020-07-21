"""
abcd
*d%#
abacabadaba
#*%*d*%

*d*%*d*#*d*
dacabac
"""

key1 = input()
key2 = input()

scrambler = dict(zip(key1, key2))
decoder = dict(zip(key2, key1))

for chart in input():
    print(scrambler[chart], end='')
print()
for chart in input():
    print(decoder[chart], end='')
