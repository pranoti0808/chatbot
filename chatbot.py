import pyttsx3                    #pip install pyttsx3
import speech_recognition as sr   #pip install speechRecognition
import datetime
import wikipedia                  #pip install wikipedia
import webbrowser
import os
import smtplib


print("Initialising voice assistant")
print("Time: ")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


#speak function will pronounce the string which is passed to it.
def speak(text):
    engine.say(text)
    engine.runAndWait()



#show the time and wish as per the time.
def greet():
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    second = int(datetime.datetime.now().second)
    print(hour ,":", minute,":", second) 

    if hour>=0 and hour<12:
        speak("Good morning")

    elif hour>12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")



#this function will take command from the microphone 
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say again..")
        query = None

    return query



#send the mails
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.sendmail("pranotigalgunde@gmail.com", to, content)
    server.close()

greet() 
speak("I am your voice assistant. How can i help you?")
query = command()



#searching for the webfor information based on the user queries.
if 'wikipedia' in query.lower():
    speak("According to wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    webbrowser.open('Youtube.com')


elif 'open google' in query.lower():
    webbrowser.open('google.com')

    
elif 'play music' in query.lower():
    songs = os.listdir("c:users\\pranoti\\downloads\\music")
    print(songs)



elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H %M %S")
    speak(f"the time is{strTime}")


elif "date" in query:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")














