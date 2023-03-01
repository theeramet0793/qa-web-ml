# from pythaiasr import asr

# file = "sound/sound3.wav"
# print(asr(file))

import speech_recognition as sr

file = "sound/sound2.wav"
hellow=sr.AudioFile(file)
r = sr.Recognizer()

with hellow as source:
    audio = r.record(source)

try:
    s = r.recognize_google(audio_data=audio, language="th-TH", show_all=True)
    alternativeList = s['alternative']
    transcript0 = alternativeList[0]
    transcript0Value = transcript0['transcript']
    print(transcript0Value)
    
    f = open("movieText/test.txt", "w", encoding="utf-8")
    f.write(transcript0Value)
    f.close()
except Exception as e:
    print("Exception: "+str(e))