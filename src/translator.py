from google.auth.credentials import Credentials
from google.oauth2 import service_account
from google.cloud import aiplatform
from vertexai.preview.language_models import ChatModel, InputOutputTextPair
import os

creds = {
  "type": "service_account",
  "project_id": "project-419321",
  "private_key_id": "3bf784d7d09e06b26e54d5ee05e2762f227c6adf",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDJvmhdjcU8/6sK\nYB9EgegBoR/cR439JTd2X/dLsBeUDmdQfwAzahlCcVKcR2D/AHR+NVoEJFATwMWC\nZHn4DmWXG5Zb7V4TccZSueSqiieWHJ9STxGTcqmPEHgdcOcnMblZIwCwWulG7UZ1\n0JZV4ZXqQOS+vX3QuHwkmaqiYXosLA3UtbMNfwFFyBwfu+4D6qdM/q0GeK0vgFzj\nBxUT5sftuxTKoapjAXXyXLz/JS3SfWBRuL8KhGccPxspBENaSROI3jFCfxokFk2F\n/la5l//6dDHNqtir+d2+Gn8dAgcZn9I/E0O+/uZd1mJlDPY2eJb8a6J558eRHqXu\nzm1ldkBpAgMBAAECggEAGtAb8l0qiwAm9SbP2QzT702BHMeE01GMNMct6KkThSnB\n6PSsK+ksyMQjeOJSvamLkg+Ysma6Htn21izw+fs93M69leOvJnHvbCTJQ7I/byfI\nNAoOubRaXUmQ0UblbfPhoLtydr3qdbMI85UgufLUuDDeRgyMyX4Pf9TNlS3T7UVD\n/wqgIovDG76AvrA6DwB/FTgVk1CYTuPUNn11E+NVc7M6ujU7RHskfctD8agZmU4r\nIYZuc+yY87SlA8wrZhCCbU3skUQY2tf3ATmbOah9xOM1s1S3y5iAonlPCM+Zc3bC\ntiyJD2Oxc/2lqyJu0NPEZ827sjnEN+ZFy3Nlv7UJ9QKBgQD4SgMlY3PGcrUXI9OL\n5LWuuDhyi505UwyBJPGqS6Xq+ZHZFc/v4SRVHnOy5X3ly3q1JXQhR1Ky65B8nLjF\nVvvD0oUf81aJBOdV7Rm6o26AS58wnzlRio2TV1TUfHWQbJCGss8CIVmlS1rYQgcH\n3a23xySQr2ualikv6JdzzcdeFQKBgQDQAlfgxMU1l8DZ0XYL3kgFYb1o8TGXzm3f\n1UhXf8k0J6QNNG1nfLN13xuixbR/6L6wnoPZ1XlCUmPuYdHpeRSWcGUqZztflAgF\ni3zTTcjwGTKNcJbse31ByIjT3bbM68mzQTmaSEP7qwgnj0I2dsD5oNQjJ5pl9sN5\n/EZp9RBCBQKBgDwxNTILOjYR+PTzKoXvnFwPLSAX2LXc/FsSqcOvMzoT5tfKAe8V\nlclM6J+mIy9idQ0VV2H5+IKHuS98jw7IV6DRmJR2WbQ+DBc4s9Qbat6PdrhC4ZJz\nFH9z3Izm31lz+FWvY6AQlbsM2akz2KB/jW3QSX0KCfwgCzwiFxVr/blBAoGAMHgL\nUBWpulY1GsxDDHrsH0zqHNTu8GeqlJiXNcRR9vQxtt37jDyzeIjXYLNe3ts16+PT\n52Nl0P1vybFDf3q2QGPKPvo1DI1q3RfmqzoZ01CbxfdxQ4N26Wg38d5c5R0gL8PI\nD1o9dRwiV017aUN8re464EIvKQk5/We6ZKA0/J0CgYA4OM8D5XTEZOVoVbgk6tXs\n/e2R6pa6nIFi7ifOPdE/ppFrkWrrJnZXVoC+NcAaGKKpyNSdTKvLzw32zqWboQhX\n257JCgWzAv/WGNG+EFNYtPSJ1bJwJnTKzWKav594tsj7ouwMsfOV0Nu2I/vkpvQ/\n3uNqhaTVevqKfPXoVP3wfQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "133740138345-compute@developer.gserviceaccount.com",
  "client_id": "114442368978777371563",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/133740138345-compute%40developer.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

credentials = service_account.Credentials.from_service_account_info(creds)
aiplatform.init(project="project-419321", credentials=credentials)

# function whose return type is changed by mocking
def query_llm_basic(content):
    return content

chat_model = ChatModel.from_pretrained("chat-bison@001")

def get_language(post: str) -> str:
    context = "Classify the text language"
    parameters = {
        "temperature": 0.7,  
        "max_output_tokens": 256
    }
    chat = chat_model.start_chat(context=context)
    response = chat.send_message(post, **parameters)
    return response.text

def get_translation(post: str) -> str:
    context = "Translating to english"
    parameters = {
        "temperature": 0.7,  
        "max_output_tokens": 256, 
    }
    chat = chat_model.start_chat(context=context)
    response = chat.send_message(post, **parameters)
    return response.text

def no_chars(post:str) -> bool:
  no_chars = True
  for i in "abcdefghijklmnopqrstuvwxyz":
    if i in post:
      no_chars = False
  return no_chars

def translate_content(post:str):
    try:
        error_messages = ["I'm not able to help with that, as I'm only a language model", "I don't understand your request", "I can't translate"]
        language = get_language(post).lower()
        if language == "english":
            return (True, post)
        elif language in error_messages:
            return(False, "We were unable to translate this post.")
        else:
            response = get_translation(post)
            if response in error_messages or no_chars(response):
                return (False, "We were unable to translate this post.")
            else:
                return (False, response)
    except:
        return (False, "We were unable to translate this post.")