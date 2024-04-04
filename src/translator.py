from google.auth.credentials import Credentials
from google.oauth2 import service_account
from google.cloud import aiplatform
from vertexai.preview.language_models import ChatModel, InputOutputTextPair

credentials = service_account.Credentials.from_service_account_info({
    "type": "service_account",
    "project_id": "nodebb-417216",
    "private_key_id": "936f2dcd04c16d6b13125dbf9c508a50e2104966",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCwT12kByGsCulK\n02rqVzmT4y6RbxmnU/yS6QV2P2Fjo4NvXlKnKhpsdUpWshn8QmTs14uB4LTCYtvr\nAN70MiZvFkX5lqb0bwognR0jHE58Ds5u472vrd/waw8TFhjxF1N0cIxJyr6HEQdR\n5Mn2/Wbk7VabStr21C9MQcapGxvCln1JMkP0MM1Qd2TyI1rxl45O3NypWTZg4vf0\nSAq+2cJJwI0hgNwvHDeoUnbZSiOKVg9bTQ8IsTpMaGdUSWw5JTyDDak83JUbaNdU\nGWkAMwaPy+FI9c4eP684VGiGpAGrTWBJbgfoBBNPMAOc77bMgJsI5kTwNtpd+C/I\nNI0hv2FvAgMBAAECggEACdmtTCQ/29pSNWWBdC1CYMJREDwKTWByXIzbSsN4v/Xb\nOoYlDQTbrBKTgCt8Ky1UcS0LtMpmnvOiAMuwKSmCHzO53htuIXrwsGjGv3bt5Z14\nKBbeOqn2uHpqwbC63QFmHrvJArhqk6Y+Z/Nl20BGFuUxsQRqHl81c0e7fyguEV16\nDjRObFDyI4sod4u6Fur+vZz8Vc7OVbDB2+AS/182RYb3OP0vozqrNt2IuCrwloH1\nEF77TQLErv0y89/FPXtEDsa8ig9Wv7dsOrDrUca6S0tgTc0dzmaf18WCRDZVl1M7\nlTjBt/v08uZl8EdnlhVPWiwOvwbYEjYXmSrSmBmX9QKBgQD1maH1HPj0dEq/7rJy\nlNWhFvubDv03Z9U6zPVLsuH3NgnINNDxtFuxP9rLbbs546YFS1PFOCAEDTn+nxTV\ne62l7BkmhCmNA+7xrARjIqjivV0zK6hM7EF4wOEWP0xZQR1Q8vLr8SjmilOMVh8z\ni/uujcPLJaaxQ/uyGOAxO/fh7QKBgQC3xpxlB9q4oRLzD6m0nSUXpm/1uQr8zkIa\nYNWasZ70PcCTN4oVB5zfGFNXinw6IQD2f2r1/DC/i5LQP9WrPjfkMbrpg2V47vKK\nyrcotIe5DsIwUmj5c2eqQYUlwuDQL64FcqIyZATQoPg78J5AhHNYHndlMeTJskDh\n/0joyP7VSwKBgGbLRLQ4yiJWwiqPF3VJwhhIbEq7/VPBS8funQRv/I/huDppkMJ5\ngJ8xYLwgU2qpU4WHv6oeEZhgiNN/ddLcjxORO/2Y92MkMFBKdROhIBq2s1mFfk2j\n3MtTv2H2YFhDHqgQ54fFSh8j6lAkg66pek/W2goe2iP7lk82hi9VMC0JAoGBAKTg\n7gO+rj8jVEr57Hn82wCC9MPyxqbVrnzYEAx/+2qJ1LLAC4SeleGag3tw5c+JOMHu\nw1n6bwoLAScRfnPqmF6FN3q1xl5fkv9urDE69uHTGeocpc3X+lPIANtGIkjl3i1J\nEbhAAAnlwZCVaoXbz1hpzRjfULKc2JVqYlFnsypNAoGAc19Y/Eb4DMQFwPwnMArS\nLPEs57YS04+LaGqkMJykJIWR9vDqWepggFY5bjzIV0inlf74zBbcS9AdiEnyoUm+\nouV0eAaTMSGICmje8FFMuHcWAjAoHTb0W5HG3GNEORhsjfSQeXoD9zA3CoHzCaBo\nf+Ih1n1NhoDDpGeqyXzh7WA=\n-----END PRIVATE KEY-----\n",
    "client_email": "775539919798-compute@developer.gserviceaccount.com",
    "client_id": "116636156891775337889",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/775539919798-compute%40developer.gserviceaccount.com",
    "universe_domain": "googleapis.com"
})
aiplatform.init(project="nodebb-417216", credentials=credentials)

# function whose return type is changed by mocking
def query_llm_basic(content):
    return content

chat_model = ChatModel.from_pretrained("chat-bison@001")

def get_translation(post: str) -> str:
    context = "Translating to english"
    parameters = {
        "temperature": 0.7,  
        "max_output_tokens": 256, 
    }
    chat = chat_model.start_chat(context=context)
    response = chat.send_message(post, **parameters)
    return response.text

def get_language(post: str) -> str:
    context = "Classify the text language"
    parameters = {
        "temperature": 0.7,  
        "max_output_tokens": 256
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
    #content = query_llm_basic(post).text mocker will go in and change content