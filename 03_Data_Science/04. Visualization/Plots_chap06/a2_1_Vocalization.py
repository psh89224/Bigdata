import urllib.request
client_id="KgrtTY9lTHlN5_3DkPhM"
client_secret="QK96HgEGoD"
default_str="""오늘의 뉴스를 알려드리겠습니다 홍준표 대표는 류여해 의원의 성추행 고소 관련하여 말도안된다며"""

emotion_str = "안녕하세요. 안녕하세요? 안녕하세요!"
encText = urllib.parse.quote(default_str)
data = "speaker=jinho&speed=0&text="+ encText;
url = "https://openapi.naver.com/v1/voice/tts.bin"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode('utf-8'))
rescode = response.getcode()
if(rescode==200):
    print("TTS mp3 저장")
    response_body = response.read()
    with open('naver_vocal_test.mp3', 'wb') as f:
        f.writable(response_body)
else:
    print("Error Code:" + rescode)