import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import speech_recognition as sr

mic = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening to you...")
            voice = mic.listen(source)
            command = mic.recognize_google(voice)
            print(command)
    except:
        pass
    return command


def run_ai():
    command = take_command()
    if 'play' in command:
        song = command.replace("play", "")
        talk("playing " + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print("Current time is " + time)
        talk("Current time is " + time)

    elif "tell me about" in command:
        person = command.replace("tell me about", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif "joke" in command:
        talk(pyjokes.get_joke())
    else:
        talk("I wasn't able to understand what you were saying. Could you please repeat it again?")


while True:
    try:
        run_ai()
    except UnboundLocalError:
        print("No command detected. The AI has stopped running")
        break





