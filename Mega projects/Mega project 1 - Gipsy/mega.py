import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    print(c)


if __name__ == "__main__":
    speak("Hello! I am Gipsy, your personal assistant.")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Adjusting...")
                recognizer.adjust_for_ambient_noise(source, duration=1)

                print("Listening...")
                audio = r.listen(source)
                word = r.recognize_google(audio)
                if(word.lower() == "Gipsy".lower()):
                    speak("Yes, how can I help you?")
                    print("Listening...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)

        except Exception as e:
            print("Error; {0}".format(e))        