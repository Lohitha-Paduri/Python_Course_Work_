#Install these commands in terminal
#pip install SpeechRecognition
#pip install pyttsx3
#pip install wikipedia

# Install these commands in terminal
# pip install SpeechRecognition
# pip install pyttsx3
# pip install wikipedia

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

# -----------------------
# SPEAK FUNCTION
# -----------------------

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


# -----------------------
# LISTEN FUNCTION
# -----------------------

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening......")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        print("Audio Done")

    try:
        command = recognizer.recognize_google(
            audio,
            language="en-in"
        )
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""

    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""


# -------------------------
# PROCESS COMMAND
# -------------------------

speak("Hello, I'm your Voice Assistant. How can I help you?")

while True:

    command = listen()

    if "time" in command:

        current_time = datetime.datetime.now().strftime(
            "%I:%M %p"
        )

        speak(
            f"The current time is {current_time}"
        )

    elif "date" in command:

        today = datetime.datetime.now().strftime(
            "%d %B %Y"
        )

        speak(
            f"Today's date is {today}"
        )

    elif "open google" in command:

        speak("Opening Google")

        webbrowser.open(
            "https://www.google.com"
        )

    elif "open youtube" in command:

        speak("Opening YouTube")

        webbrowser.open(
            "https://www.youtube.com"
        )

    elif "open gmail" in command:

        speak("Opening Gmail")

        webbrowser.open(
            "https://mail.google.com"
        )

    elif "open chat g p t" in command or "open chatgpt" in command:

        speak("Opening ChatGPT")

        webbrowser.open(
            "https://chatgpt.com"
        )

        speak(
            "Hello. How can I help you today?"
        )

    elif "who created you" in command:

        speak(
            "I was created using Python"
        )

    elif "open maps" in command:

        speak("Which place do you want to search?")

        city = listen()

        webbrowser.open(
            f"https://www.google.com/maps/search/{city}"
        )

    elif "bye" in command or "exit" in command:

        speak(
            "Goodbye. Have a great day."
        )

        break

    else:

        speak(
            "Sorry. I do not know that command yet."
        )