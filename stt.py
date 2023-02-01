import speech_recognition as sr
from tts import speak

Recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("듣고 있습니다.")
        # phrase_time_limit = 음성 듣는 시간(초) 제한, timeout = x초 동안 음성이 들어오지 않으면 에러 리턴
        audio = Recognizer.listen(source, phrase_time_limit=3, timeout=0)
    try:
        data = Recognizer.recognize_google(audio, language="ko", show_all=True)
    except Exception as e:
        print("들은게 없어용")
        return []
    if data == []:
        return []

    if '야' in data['alternative'][0]['transcript']:
        speak('네, 말씀하세요.')
        with sr.Microphone() as source:
            print("듣고 있습니다.")
            # phrase_time_limit = 음성 듣는 시간(초) 제한, timeout = x초 동안 음성이 들어오지 않으면 에러 리턴
            audio = Recognizer.listen(source, phrase_time_limit=5)
        try:
            data = Recognizer.recognize_google(audio, language="ko", show_all=True)
        except Exception as e:
            return ["nospeak"]
        return data
    else:
        return []