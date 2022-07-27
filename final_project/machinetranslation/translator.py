import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
     version='2022-07-22',
     authenticator=authenticator )
language_translator.set_service_url(url)

def english_to_french(english_text):
    """This functions translates English text to French"""
    french_text = language_translator.translate( 
        text = english_text,
        model_id='en-fr').get_result()
    result = french_text.get("translations")[0].get("translation")
    return result

def french_to_english(french_text):
    """This functions translates French text to English"""
    english_text = language_translator.translate( 
        text = french_text,
        model_id='fr-en').get_result()
    result = english_text.get("translations")[0].get("translation")
    return result