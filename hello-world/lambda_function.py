import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    result = 9 + 9
    logger.info('Calculated result of %s', result)

    return {
        'statusCode': 200,
        'body': result
        }
        