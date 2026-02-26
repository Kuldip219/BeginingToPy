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
    print("OK")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Adjusting...")
                recognizer.adjust_for_ambient_noise(source, duration=1)

                print("Listening...")
                audio = r.listen(source)

                print("Recognizing...")
                word = r.recognize_google(audio)
                print(word)

        except Exception as e:
            print("Error; {0}".format(e))        