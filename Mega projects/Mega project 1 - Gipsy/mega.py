import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello! I am Gipsy, your personal assistant.")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                command = r.recognize_google(audio).lower()
            if(command == "Gipsy"):
                speak("Yes, how can I assist you?")
        
        except Exception as e:
            print("Error; {0}".format(e))