import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
VERSION = "0.1.0"

def lambda_handler(event: dict, context) -> dict:
    logger.info('queryStringParameters: %s', event['queryStringParameters'])
    event=event['queryStringParameters']
    unsubscribe(event['user'])
    html = get_html("thankyou.html")
    return {
        'statusCode': 200,
        'body': html,
        'headers': {
            'Content-Type': 'text/html'
        }
    }

def unsubscribe(user: str):
    logger.info('unsubscribing: %s', user)


def get_html(template: str) -> str:
    with open('templates/{}'.format(template)) as f:
        content = f.read()
    return content