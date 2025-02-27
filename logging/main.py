import logging

# logging.basicConfig(
#     # level=logging.INFO,
#     # format='%(asctime)s %(message)s'
# )

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

logger.info(logger.propagate)
logger.warning('Watch out!')  # will print a message to the console
logger.info('I told you so')  # will not print anything
