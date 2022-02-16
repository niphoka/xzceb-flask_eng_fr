import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

"""Used to call .env file into here"""

authenticator = IAMAuthenticator('aJpwgx5qg56TT7BCOdAqccV9t2-vl9lynFyOEZH9VURd')
lt = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

lt.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    """Translate from Enlish to French"""
    translation = lt.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """Translate from French to English"""
    translation = lt.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
