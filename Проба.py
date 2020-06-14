import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.disabled = True

x = 0
y = 1000
for i in range(10):
    x += i
    y -= i
    logging.debug(f'{x} и {y}')
print(x, y)

'''
В темплейты lgg
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.disabled = False
logging.debug(f'')

'''