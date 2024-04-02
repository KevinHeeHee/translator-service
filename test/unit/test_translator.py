from src.translator import translate_content, query_llm_basic
from mock import patch, Mock

def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message"

def test_llm_normal_response():
    is_english, translated_content = translate_content("This is normal")
    assert is_english == True
    assert translated_content == "This is normal"
    is_english, translated_content = translate_content("Qual é o trabalho e a extensão do algoritmo de Dijkstra?")
    assert is_english == False
    assert translated_content == "What is the work and span of Dijkstra's Algorithm?"

def test_llm_gibberish_response():
    is_english, translated_content = translate_content("as;lkhr;weqonfsjd")
    assert is_english == False
    assert translated_content == "This is gibberish"

# Mocking testing
@patch('src.translator.query_llm_basic')
def test_unexpected_language(mocker):
    # Test 1: we mock the model's response to return standard error messages
    mocker.return_value.text = "I don't understand your request"
    assert translate_content("Random post") == (False, "We were unable to translate this post.")
    mocker.return_value.text = "I'm not able to help with that, as I'm only a language model"
    assert translate_content("Random post") == (False, "We were unable to translate this post.")
    mocker.return_value.text = "I can't translate"
    assert translate_content("Random post") == (False, "We were unable to translate this post.")

@patch('src.translator.query_llm_basic')
def test_bad_types(mocker):
    # Test 2: we mock the model's response to return a one digit number
    mocker.return_value.text = "2"
    assert translate_content("Random post") == (False, "We cannot translate because you inputed a number")

@patch('src.translator.query_llm_basic')
def test_null_checks(mocker):
    # Test 3: we mock the model's response to be None
    mocker.return_value.text = None
    assert translate_content("Random post") == (False, "We were unable to translate because of null value")

@patch('src.translator.query_llm_basic')
def test_emoji_handling(mocker):
    #Test 4: We mock the model to return unexpected text (emojis)
    mocker.return_value.text = "💀💀💀"
    assert translate_content("Random post") == (False, "We were unable to translate this post.")