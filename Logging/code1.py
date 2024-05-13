import logging
logging.basicConfig(filename='code1.log', level=logging.INFO, format='%(levelname)s - %(asctime)s - %(message)s, %(name)s')

logging.debug('This is a debug message')
logging.info('This is informational message')
logging.error('This is an error message')