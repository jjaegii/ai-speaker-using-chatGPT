# AI speaker using chatGPT

### 속도 측정

1. https://github.com/acheong08/ChatGPT vs 2. https://github.com/mmabrouk/chatgpt-wrapper(python) vs 3. https://github.com/mmabrouk/chatgpt-wrapper(shell)

~~총 실행 시간 측정 시 - 빠름 2 > 1 > 3 느림
텍스트 출력 시작 시간 측정 시 - 빠름 3 > 2 > 1 느림 -> 3이 실시간으로 텍스트 출력됨.(하지만, 한글로 사용 시 오류가 있어 영어로 사용하면 번역과 tts 사용에 어려움이 있어 2를 사용하기로 함)~~

-> open ai 공식 api 쓰니까 속도가 빠름

## how to run

~~https://github.com/mmabrouk/chatgpt-wrapper 참고하여 설치 후~~

~~1. python3 install.py install를 입력 후 브라우저를 통하여 openai.com 로그인~~

~~2. chatGPT shell 창에서 !session을 입력하여 세션 등록~~

~~3. shell 창 종료 후 python3 run.py로 실행~~

https://platform.openai.com/account/api-keys 에서 api 키를 발급 받은 후 chat.py My_OpenAI_key에 적용

### docker
docker run --device /dev/snd:/dev/snd -it ubuntu:ai-speaker-using-chatGPT python3 run.py

### just on device
1. pip install -r requirements.txt
2. python run.py
