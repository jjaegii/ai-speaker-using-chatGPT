# # https://github.com/acheong08/ChatGPT readme 1번
# from revChatGPT.ChatGPT import Chatbot

# chatbot = Chatbot({
#   "session_token": "<<YOUR_SESSION_ID>>"
# }, conversation_id=None, parent_id=None)

# def ask(prompt):
#   response = chatbot.ask(prompt, conversation_id=None, parent_id=None)
#   return response['message']

# import time

# start = time.time()
# print('시작')
# response = ask('how to make potato salad?')
# print(response)
# end = time.time()
# print(end - start)

# https://github.com/mmabrouk/chatgpt-wrapper readme 2번
from chatgpt_wrapper import ChatGPT
from googletrans import Translator

bot = ChatGPT()
translator = Translator()

def ask(prompt):
    response = bot.ask(translator.translate(prompt, src='ko', dest='en').text)
    return translator.translate(response, src='en', dest='ko').text

# # 시스템 명령어로 실행 readme 3번
# import os

# prompt = '감자 샐러드는 어떻게 만들어? 한글로 말해줘'

# import time

# def run():
#   print('시작')
#   start = time.time()
#   os.system('chatgpt ' + prompt + " | espeak -v ko")
#   print('chatgpt 명령어 완료')
#   print(time.time() - start)

# run()