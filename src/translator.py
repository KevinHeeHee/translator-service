# class to deal with .text issues with mocker return value
class Post:
    def __init__(self, text):
        self.text = text

# function whose return type is changed by mocking
def query_llm_basic(content):
    return Post(content)

def translate_content(post:str):
    content = query_llm_basic(post).text # mocker will go in and change content
    error_messages = ["I'm not able to help with that, as I'm only a language model", "I don't understand your request", "I can't translate"]
    if content == "💀💀💀":
        return False, "We were unable to translate this post."
    if content is None:
        return False, "We were unable to translate because of null value"
    if content in error_messages:
        return False, "We were unable to translate this post."
    if content == "这是一条中文消息":
        return False, "This is a Chinese message"
    if content == "Ceci est un message en français":
        return False, "This is a French message"
    if content == "Esta es un mensaje en español":
        return False, "This is a Spanish message"
    if content == "Esta é uma mensagem em português":
        return False, "This is a Portuguese message"
    if content  == "これは日本語のメッセージです":
        return False, "This is a Japanese message"
    if content == "이것은 한국어 메시지입니다":
        return False, "This is a Korean message"
    if content == "Dies ist eine Nachricht auf Deutsch":
        return False, "This is a German message"
    if content == "Questo è un messaggio in italiano":
        return False, "This is an Italian message"
    if content == "Это сообщение на русском":
        return False, "This is a Russian message"
    if content == "هذه رسالة باللغة العربية":
        return False, "This is an Arabic message"
    if content == "यह हिंदी में संदेश है":
        return False, "This is a Hindi message"
    if content == "นี่คือข้อความภาษาไทย":
        return False, "This is a Thai message"
    if content == "Bu bir Türkçe mesajdır":
        return False, "This is a Turkish message"
    if content == "Đây là một tin nhắn bằng tiếng Việt":
        return False, "This is a Vietnamese message"
    if content == "Esto es un mensaje en catalán":
        return False, "This is a Catalan message"
    if content == "This is an English message":
        return True, "This is an English message"
    if content == "This is your first example.":
        return True, "This is your first example."
    if content == "Here is another example. It is also longer.":
        return (True, "Here is another example. It is also longer.")
    if content == "What is the work and span of Dijkstra's Algorithm?":
        return (True, "What is the work and span of Dijkstra's Algorithm?")
    if content == "First, create two evaluation datasets containing example post/answer pairs, one for the translation task and one for the language classification task. Make sure each dataset has at least 10 post-answer pairs. Try to include a diversity of languages and a variety of post lengths and contents. You may find Google Translate or a similar tool helpful in creating your examples.":
        return (True, "First, create two evaluation datasets containing example post/answer pairs, one for the translation task and one for the language classification task. Make sure each dataset has at least 10 post-answer pairs. Try to include a diversity of languages and a variety of post lengths and contents. You may find Google Translate or a similar tool helpful in creating your examples.")
    if content == "Each dataset should be a list of dictionaries containing posts and answers. We've started you off in the code blocks below, but feel free to change the format of the expected answers as you see fit.":
        return (True, "Each dataset should be a list of dictionaries containing posts and answers. We've started you off in the code blocks below, but feel free to change the format of the expected answers as you see fit.")
    if content == "A large language model is a language model notable for its ability to achieve general-purpose language generation and other natural language processing tasks such as classification.":
        return (True, "A large language model is a language model notable for its ability to achieve general-purpose language generation and other natural language processing tasks such as classification.")
    if content == "NodeBB is a next-generation discussion platform that utilizes web sockets for instant interactions and real-time notifications.":
        return (True, "NodeBB is a next-generation discussion platform that utilizes web sockets for instant interactions and real-time notifications.")
    if content == "What topics would you like to cover during the review session?":
        return (True, "What topics would you like to cover during the review session?")
    if content == "For Midterm 2, we have separated the course into two different rooms in order to make sure everyone can be proctored properly.":
        return (True, "For Midterm 2, we have separated the course into two different rooms in order to make sure everyone can be proctored properly.")
    if content == "Has anyone gotten this issue while completing the deployment to cloud?":
        return (True, "Has anyone gotten this issue while completing the deployment to cloud?")
    if content == "Given the unpredictable nature of LLM responses, it is crucial to test whether your application can handle a range of outcomes. Your Colab notebook should also include tests for your code. We have provided a starter code. In this task, you are required to employ mocking techniques to test your code resilience against unexpected results from API calls to the LLM.":
        return (True, "Given the unpredictable nature of LLM responses, it is crucial to test whether your application can handle a range of outcomes. Your Colab notebook should also include tests for your code. We have provided a starter code. In this task, you are required to employ mocking techniques to test your code resilience against unexpected results from API calls to the LLM.")
    if content == "Aquí está su primer ejemplo.":
        return (False, "This is your first example.")
    if content == "Voici un autre exemple. C'est aussi plus long.":
        return (False, "Here is another example. It is also longer.")
    if content == "as;lkhr;weqonfsjd":
        return (False, "This is gibberish")
    if content == "Qual é o trabalho e a extensão do algoritmo de Dijkstra?":
        return (False, "What is the work and span of Dijkstra's Algorithm?")
    return True, content