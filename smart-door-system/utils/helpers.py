import logging

# Configure logging
logging.basicConfig(
    filename='logs/system.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_message(message):
    logging.info(message)
