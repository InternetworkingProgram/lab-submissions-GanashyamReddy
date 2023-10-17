import logging
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')

logging.basicConfig(format='%(asctime)s - %(message)s',
level=logging.INFO)
logging.info('Admin logged in')

logging.basicConfig(format='%(asctime)s - %(message)s',
datefmt='%d-%b-%y %H:%M:%S')
logging.warning('Admin logged out')