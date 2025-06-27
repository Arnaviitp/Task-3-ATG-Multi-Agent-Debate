import logging

logging.basicConfig(
    filename='debate_log.txt',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

logger = logging.getLogger(__name__)
