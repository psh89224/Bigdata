from gtts import gTTS

default_str="""안녕하세요 나열심입니다"""

emotion_str="안녕하세요. 젠장 젠장"

def speaker(a):
    tts = gTTS(text=a, lang='ko')
    tts.save("google_vocal_test.mp3")

    open("google_vocal_test.mp3")

#speaker(default_str)
speaker(emotion_str)