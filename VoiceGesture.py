import pyttsx3
import speech_recognition as sr  

class voice_gesture():
    def __init__(self):
        self.isrun = True

    def speak(self, text):
        s = pyttsx3.init()
        s.say(text)
        s.runAndWait()

    def reconize_voice(self):
        message = "rien" 
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                sayed = r.recognize_google(audio, language='fr-Fr')
                if self.isrun == False:
                    if sayed == 'bonjour':
                        message = sayed
                        self.isrun = True
                else: 
                    message = sayed
            except sr.RequestError as e:
                message = 'Le service Google API ne fonctione plus' + format(e) 
                    
        return message