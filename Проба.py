genome = 'ATTG'
print(*[i for i in genome], sep='\n')
[print(c) for c in genome]
print([c for c in genome])

'''
В темплейты lgg
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.disabled = False
logging.debug(f'')
дом

'''

"""
В темплейты tmt100
import timeit

NOT_REPITED_CODE = '''
$NOT_REPITED_CODE$
'''

TESTED_CODE = ''' 
$TESTED_CODE$
'''

# вывод на печать результатов измерений number = 100 повторов
print(timeit.repeat(stmt=MyCode, setup=MySetup, number=100))

дом

"""

"""
ii => int(input())

дом

"""