import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
    
speak("Your Text ")
user_input = str(input("Your Text : "))

engine.save_to_file(user_input,'speech.mp3')
engine.runAndWait() 
 