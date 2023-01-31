from stt import listen
from chat import ask
from tts import speak

while True:
    data = listen()
    if len(data) == 0:
        print('들은게 없어')
        continue
    print(data)
    speak('찾아볼게요 잠시만 기다려주세요.')
    ask_message = data['alternative'][0]['transcript']
    response = ask(ask_message)
    print(response)
    speak(response)