#!env/bin/python

import logging
import os
import shopify


logger = logging.getLogger()
logger.setLevel(logging.INFO)
VERSION = "0.1.0"
SHOP_URL = "https://{}:{}@{}.myshopify.com/admin".format(os.environ['SHOP_API_KEY'], os.environ['SHOP_PASSWORD'], os.environ['SHOP_NAME'])


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
    shopify.ShopifyResource.set_site(SHOP_URL)
    try:
        customer = shopify.customer.Customer.find(email=user)
    except:
        return
    if len(customer) > 1:
        logger.error("too many results when looking for customer: %s", user)
        return
    if len(customer) == 0:
        logger.error("No customer found: %s", user)
        return
    logger.info('unsubscribing: %s', user)
    customer[0].accepts_marketing = False
    try:
        customer[0].save()
    except:
        logger.error("unable to unsubscribe user: %s", user)
        return
    


def get_html(template: str) -> str:
    with open('templates/{}'.format(template)) as f:
        content = f.read()
    return content