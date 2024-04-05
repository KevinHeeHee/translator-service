from google.auth.credentials import Credentials
from google.oauth2 import service_account
from google.cloud import aiplatform
from vertexai.preview.language_models import ChatModel, InputOutputTextPair
import os

if os.environ.get('PRIVATE_KEY') != None:
    os.environ['GOOGLE_CLOUD_PROJECT'] = "llm-project-419400"
    os.environ['PRIVATE_KEY'] = os.environ['PRIVATE_KEY'].replace('\\n', '\n')
    creds = {
        "type": "service_account",
        "project_id": "llm-project-419400",
        "private_key_id": str(os.environ['PRIVATE_KEY_ID']),
        "private_key": str(os.environ['PRIVATE_KEY']),
        "client_email": "561147812575-compute@developer.gserviceaccount.com",
        "client_id": "111582157382499883679",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/561147812575-compute%40developer.gserviceaccount.com",
        "universe_domain": "googleapis.com"
        }
    credentials = service_account.Credentials.from_service_account_info(creds)
    aiplatform.init(project="llm-project-419400", credentials=credentials)


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
            if response in error_messages:
                return (False, "We were unable to translate this post.")
            else:
                return (False, response)
    except:
        return (False, "We were unable to translate this post.")