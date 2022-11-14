# tweepy-bots/bots/config.py
import tweepy
import logging


logger = logging.getLogger()

def create_api():
    consumer_key = "XXXXXXXXXXXXXXXXX"
    consumer_secret = "XXXXXXXXXXXXXX"
    access_token = "XXXXXXXXXXXXXXXXX"
    access_token_secret = "XXXXXXXXXX"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    try:
        if api.verify_credentials():
            print("Authentication Successful")
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api

