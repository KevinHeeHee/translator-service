from src.translator import translate_content, query_llm_basic
import vertexai
from mock import patch, Mock
from vertexai.preview.language_models import ChatModel, InputOutputTextPair

def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message."

def test_llm_normal_response():
    is_english, translated_content = translate_content("This is normal")
    assert is_english == True
    assert translated_content == "This is normal"

def test_llm_gibberish_response():
    is_english, translated_content = translate_content("asdfjbnlrjfbkjfjkbfdg.")
    assert is_english == True
    assert translated_content == "asdfjbnlrjfbkjfjkbfdg."

# Mocking testing
@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_unexpected_language(mocker):
    # Test 1: we mock the model's response to return standard error messages
    mocker.return_value.text = "I don't understand your request"
    assert translate_content("Random post") == (False, "We were unable to translate this post.")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_bad_types(mocker):
    # Test 2: we mock the model's response to return a one digit number
    mocker.return_value.text = "2"
    assert translate_content("Random post") == (False, "We were unable to translate this post.")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_null_checks(mocker):
    # Test 3: we mock the model's response to be None
    mocker.return_value.text = None
    assert translate_content("Random post") == (False, "We were unable to translate this post.")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_emoji_handling(mocker):
    #Test 4: We mock the model to return unexpected text (emojis)
    mocker.return_value.text = "💀💀💀"
    assert translate_content("Random post") == (False, "We were unable to translate this post.")