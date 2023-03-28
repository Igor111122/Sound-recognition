import speech_recognition as sr

# створення об'єкту Recognizer
r = sr.Recognizer()

# зчитування аудіозапису з мікрофону
with sr.Microphone() as source:
    print("say something:")
    audio = r.listen(source)

# розпізнавання тексту
try:
    text = r.recognize_google(audio, language='uk-UA')
    print("you said: " + text)
except sr.UnknownValueError:
    print("Voice not recognized")
except sr.RequestError as e:
    print("Google Speech Recognition service error; {0}".format(e))































