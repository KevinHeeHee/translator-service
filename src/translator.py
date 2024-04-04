from vertexai.preview.language_models import ChatModel, InputOutputTextPair

# class to deal with .text issues with mocker return value
class Post:
    def __init__(self, text):
        self.text = text

# function whose return type is changed by mocking
def query_llm_basic(content):
    return Post(content)

def get_translation(chat_model, post: str) -> str:
    context = "Translating to english"
    parameters = {
        "temperature": 0.7,  
        "max_output_tokens": 256, 
    }
    chat = chat_model.start_chat(context=context)
    response = chat.send_message(post, **parameters)
    return response.text

def get_language(chat_model, post: str) -> str:
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
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    try:
        error_messages = ["I'm not able to help with that, as I'm only a language model", "I don't understand your request", "I can't translate"]
        language = get_language(chat_model, post).lower()
        if language == "english":
            return (True, post)
        elif language in error_messages:
            return(False, "We were unable to translate this post.")
        else:
            response = get_translation(chat_model, post)
            if response in error_messages or no_chars(response):
                return (False, "We were unable to translate this post.")
            else:
                return (False, response)
    except:
        return (False, "We were unable to translate this post.")
    #content = query_llm_basic(post).text mocker will go in and change content