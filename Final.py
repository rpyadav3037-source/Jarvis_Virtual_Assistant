import pyttsx3
import webbrowser
import speech_recognition as sr
import time
import MusicLibrary
import os
from folder_paths import movie_paths

# Initilize the recognizer and engine
recognizer=sr.Recognizer()
engine = pyttsx3.init()

# Set voice and rate
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use a valid voice index


# speak function
def speak(text):
    print(f"Jarvis :{text}")
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.3)

# Command processor
def processcommand(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
        print("Opening Google")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        print("Opening YouTube")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        print("Opening Facebook")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
        print("Opening LinkedIn")
    elif command.lower().startswith("play"):    # say play before the song name to play desired song
        song=command.lower().split(" ")[1]
        link=MusicLibrary.music[song]
        webbrowser.open(link)
        print("Playing song...")

    elif command.lower().strip().startswith("start"):  # Say start before the movie name to play desired movie
        movie=command.lower().split(" ")[1]
        file=movie_paths.get(movie)    
        if file:
            os.startfile(file)
            print("Playing movie...")
        else:
            print(f"Movie '{movie}' not found in folder paths.")
        
    
    elif "stop" in command:
        print("Goodbye!")
        exit()
    else:
        print(f"Searching Google for: {command}")
        webbrowser.open(f"https://www.google.com/search?q={command}")  

# Listen helper
def listen_for_command(timeout=5, phrase_time_limit=5):
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        return recognizer.recognize_google(audio)        

# Main logic
if __name__ == "__main__":
    speak("Initializing Jarvis...., Say jarvis to activate")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        # r = sr.Recognizer()
         
        print("recognizing...")
        try:
            word = listen_for_command(timeout=5, phrase_time_limit=4)
            print("Heard:", word)

            if "jarvis" in word.lower():
                print("Jarvis activated, I am listening now.")
                while True:
                    try:
                        command = listen_for_command()
                        print("Command:", command)
                        command=command.lower().strip()
                        processcommand(command)

                    except Exception as e:
                        print("Eror;{0}".format(e))    


        except Exception as e:
            print("Error; {0}".format(e))

            
