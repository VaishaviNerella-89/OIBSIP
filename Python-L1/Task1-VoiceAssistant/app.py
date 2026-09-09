import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import urllib.parse
import time
import threading
import requests
import re

from commands import execute_custom_command


# ==========================================
# ASSISTANT SETTINGS
# ==========================================

ASSISTANT_NAME = "Nova"

recognizer = sr.Recognizer()
engine = pyttsx3.init()


# ==========================================
# TEXT TO SPEECH
# ==========================================

def speak(text):

    print("Assistant:", text)

    engine.say(text)
    engine.runAndWait()


# ==========================================
# SPEECH INPUT
# ==========================================

def listen():

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=0.5
        )

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        except sr.WaitTimeoutError:

            speak("I did not hear anything.")

            return ""


    try:

        command = recognizer.recognize_google(audio)

        print("You:", command)

        return command.lower()


    except sr.UnknownValueError:

        speak(
            "Sorry, I could not understand you. "
            "Please repeat."
        )

        return ""


    except sr.RequestError:

        speak(
            "I cannot connect to the speech recognition service."
        )

        return ""


# ==========================================
# GREETING
# ==========================================

def greeting():

    hour = datetime.datetime.now().hour

    if hour < 12:

        speak("Good morning!")

    elif hour < 18:

        speak("Good afternoon!")

    else:

        speak("Good evening!")


    speak(
        f"I am {ASSISTANT_NAME}, "
        "your voice assistant."
    )

    speak("How can I help you?")


# ==========================================
# DATE
# ==========================================

def tell_date():

    today = datetime.datetime.now().strftime(
        "%A, %d %B %Y"
    )

    speak("Today is " + today)


# ==========================================
# TIME
# ==========================================

def tell_time():

    current_time = datetime.datetime.now().strftime(
        "%I:%M %p"
    )

    speak(
        "The current time is "
        + current_time
    )


# ==========================================
# WEB SEARCH
# ==========================================

def web_search(command):

    search_text = command

    search_text = search_text.replace(
        "search for",
        ""
    )

    search_text = search_text.replace(
        "search",
        ""
    )

    search_text = search_text.strip()


    if not search_text:

        speak(
            "What would you like me to search for?"
        )

        return


    speak(
        "Searching for "
        + search_text
    )


    url = (
        "https://www.google.com/search?q="
        + urllib.parse.quote(search_text)
    )

    webbrowser.open(url)


# ==========================================
# WEATHER
# ==========================================

def get_weather(city):

    # Demo endpoint using wttr.in
    # No API key required.

    try:

        url = (
            "https://wttr.in/"
            + urllib.parse.quote(city)
            + "?format=j1"
        )

        response = requests.get(
            url,
            timeout=10
        )

        if response.status_code != 200:

            speak(
                "I could not get the weather information."
            )

            return


        data = response.json()

        current = data["current_condition"][0]

        temperature = current["temp_C"]

        description = current[
            "weatherDesc"
        ][0]["value"]

        humidity = current["humidity"]


        speak(
            f"The temperature in {city} "
            f"is {temperature} degrees Celsius."
        )

        speak(
            f"The weather is {description}."
        )

        speak(
            f"Humidity is {humidity} percent."
        )


    except Exception:

        speak(
            "Sorry, I could not fetch the weather."
        )


# ==========================================
# TIMER
# ==========================================

def timer_thread(seconds):

    time.sleep(seconds)

    speak(
        "Your timer is finished."
    )


def set_timer(command):

    numbers = re.findall(
        r"\d+",
        command
    )


    if not numbers:

        speak(
            "Please tell me the number of seconds."
        )

        return


    seconds = int(numbers[0])


    speak(
        f"Timer set for {seconds} seconds."
    )


    thread = threading.Thread(
        target=timer_thread,
        args=(seconds,),
        daemon=True
    )

    thread.start()


# ==========================================
# GENERAL KNOWLEDGE
# ==========================================

knowledge_base = {

    "artificial intelligence":
        "Artificial Intelligence is the field of creating machines that can perform tasks that normally require human intelligence.",

    "machine learning":
        "Machine Learning is a branch of artificial intelligence where computers learn patterns from data.",

    "python":
        "Python is a popular high level programming language known for its simple syntax and wide range of libraries.",

    "iot":
        "Internet of Things refers to physical devices connected to the internet that can collect and exchange data.",

    "database":
        "A database is an organized collection of information that can be stored, managed and retrieved electronically.",

    "cloud computing":
        "Cloud computing provides computing resources such as storage and servers over the internet."
}


def answer_question(command):

    for topic, answer in knowledge_base.items():

        if topic in command:

            speak(answer)

            return True


    return False


# ==========================================
# NATURAL LANGUAGE INTENT
# ==========================================

def understand_command(command):

    # Greeting

    if any(
        word in command
        for word in [
            "hello",
            "hi",
            "hey"
        ]
    ):

        speak(
            "Hello! How can I help you?"
        )

        return True


    # Time

    if (
        "what time" in command
        or "current time" in command
        or "time now" in command
    ):

        tell_time()

        return True


    # Date

    if (
        "today's date" in command
        or "what is the date" in command
        or "current date" in command
    ):

        tell_date()

        return True


    # Weather

    if (
        "weather" in command
        or "temperature" in command
    ):

        city = "Hyderabad"

        words = command.split()

        if "in" in words:

            index = words.index("in")

            if index + 1 < len(words):

                city = " ".join(
                    words[index + 1:]
                )


        speak(
            f"Checking the weather in {city}."
        )

        get_weather(city)

        return True


    # Search

    if (
        command.startswith("search")
        or "search for" in command
    ):

        web_search(command)

        return True


    # Timer

    if (
        "timer" in command
        or "reminder" in command
    ):

        set_timer(command)

        return True


    # Knowledge

    if answer_question(command):

        return True


    # Custom commands

    if execute_custom_command(command):

        speak(
            "Opening your requested website."
        )

        return True


    # Website commands

    if "open youtube" in command:

        webbrowser.open(
            "https://www.youtube.com"
        )

        speak("Opening YouTube.")

        return True


    if "open google" in command:

        webbrowser.open(
            "https://www.google.com"
        )

        speak("Opening Google.")

        return True


    # Exit

    if any(
        word in command
        for word in [
            "goodbye",
            "exit",
            "quit",
            "stop"
        ]
    ):

        speak(
            "Goodbye! Have a great day."
        )

        return False


    # Unknown command

    speak(
        "Sorry, I do not understand that command. "
        "Please try again."
    )

    return True


# ==========================================
# MAIN
# ==========================================

def main():

    greeting()

    running = True


    while running:

        command = listen()

        if command:

            running = understand_command(
                command
            )


# ==========================================
# START PROGRAM
# ==========================================

if __name__ == "__main__":

    main() 