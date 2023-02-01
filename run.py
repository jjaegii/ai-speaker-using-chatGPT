from stt import listen
from chat import ask
from tts import speak

while True:
    data = listen()
    if data == []:
        continue
    print(data)
    ask_message = data['alternative'][0]['transcript']
    response = ask(ask_message)
    print(response)
    speak(response)