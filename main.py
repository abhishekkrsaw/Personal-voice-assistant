#from gtts import gTTS
import speech_recognition as sr       #requires internet to work
import os                      
import pyttsx3    #text to speech library which can work offline
import webbrowser
import time       # to specify the sleep time using time.sleep() command
from datetime import date
import sqlite3    # to handle database
from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk

            
speak=pyttsx3.init()        #reference to a pyttsx3.Engine instance
speak.setProperty('rate',170)
rec=sr.Recognizer()         #reference to speech recognition    

def google_search(text):
    try:
        search = text.lower().split()
        a = search.index("search")
        
        if 'youtube' in text:
            search = search[a+1:]
            b = search.index("youtube")
            if search[b-1] == 'in':
                del search[b-1:b+1]
            else:
                del search[b]

            webbrowser.open("https://www.youtube.com/results?search_query=" + '+'.join(search))

        elif 'wikipedia' in text:
            search = search[a+1:]
            b = search.index("wikipedia")
            if search[b-1] == 'in':
                del search[b-1:b+1]
            else:
                del search[b]
               
            webbrowser.open("https://en.wikipedia.org/wiki/" + '+'.join(search))
            
        else:
            webbrowser.open("https://www.google.com/search?q=" + '+'.join(search[a+1:]))
    except Exception as e:
        speak.say("Sorry, I am not able to understand, please try rephrasing your sentence")
        

def open_app(text):
    try:
        if "gmail" in text:
            speak.say("Opening Gmail!")
            webbrowser.open("https://www.gmail.com/")
        elif "youtube" in text:
            speak.say("Opening Youtube!")
            webbrowser.open("https://www.youtube.com/")    
        elif "chrome" in text:
            speak.say("Opening Google Chrome!")
            os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        elif "word" in text:
            speak.say("Opening Microsoft office word")
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Word 2007.lnk")
        elif "powerpoint" in text:
            speak.say("Opening Microsoft office powerpoint")
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office PowerPoint 2007.lnk")
        elif "excel" in text:
            speak.say("Opening Microsoft office powerpoint")
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Excel 2007.lnk")     
        else:
            speak.say("But this application is not installed on your device")
    except Exception as e:
        speak.say("Sorry, I am not able to get the path of this application")

def joke():
    speak.say("Here's a funny joke for u")
    speak.runAndWait()
    print()
    print("Santa - Oye! what R U doing?")
    speak.say("Santa - Oye! what R U doing?")
    speak.runAndWait()    
    print("Banta - Recording this baby's voice.")
    speak.say("Banta - Recording this baby's voice.")
    speak.runAndWait()
    print("Santa - Why?")
    speak.say("Santa - Why?")
    speak.runAndWait()
    print("Banta - When he grows up,\n\tI shall ask him what he meant by this...")
    speak.say("Banta - When he grows up, I shall ask him, what he meant by this...")
    speak.say("hahahahaha ha ha!")
    speak.runAndWait()

def play_(text):

    play=text.split()
    a = play.index("play")
    play = play[a+1:]
    if "youtube" in text:        
        b = play.index("youtube")
        if play[b-1] == 'in':
            del play[b-1:b+1]
        else:
            del play[b]        
    webbrowser.open("https://www.youtube.com/results?search_query=" + '+'.join(play))

def remind_input():
    details=[]
        
    return details

def month_val(month):
    month=month.lower()
    month=month.split()
    s=len(month)-1
    if month[s]=='january' or month[s]=='jan':
        return 1
    if month[s]=='february' or month[s]=='feb':
        return 2
    if month[s]=='march' or month[s]=='mar':
        return 3
    if month[s]=='april' or month[s]=='apr':
        return 4
    if month[s]=='may':
        return 5
    if month[s]=='june' or month[s]=='jun':
        return 6
    if month[s]=='july' or month[s]=='jul':
        return 7
    if month[s]=='august' or month[s]=='aug':
        return 8
    if month[s]=='september' or month[s]=='sep':
        return 9
    if month[s]=='october' or month[s]=='oct':
        return 10
    if month[s]=='november' or month[s]=='nov':
        return 11
    return 12

def date_time():
    window=Tk()
    window.geometry("300x300")
    window.title("Reminder")
    label1=Label(window,text="Please enter the details",bg="yellow",font="arial 11 bold")
    label1.place(width=300)
    label2=Label(window,text="Event Name",bg="black",fg="white",font="arial 9 bold")
    label2.place(x=5,y=50,width=80)

    event = StringVar()
    ev_date = StringVar()
    hrs = StringVar()
    min1 = StringVar()
    am = StringVar()

    entry1 = Entry(window,textvariable=event,font="arial 9 bold")
    entry1.place(x=130,y=51,width=160)

    label3=Label(window,text="Date",bg="black",fg="white",font="arial 9 bold")
    label3.place(x=5,y=100,width=80)
    cal = DateEntry(window,textvariable=ev_date,date_pattern='yyyy-mm-dd')
    cal.place(x=130,y=100)

    label4=Label(window,text="Time",bg="#123456",fg="white",font="arial 9 bold")
    label4.place(x=5,y=150,width=80)
    hr=ttk.Combobox(window,textvariable=hrs)
    hr['values']=('01','02','03','04','05','06','07','08','09','10','11','12')
    hr.current(11)
    hr.place(x=131,y=150,width=40)
    sp2=Spinbox(window,from_=0,to=59,textvariable=min1)
    sp2.place(x=181,y=150,width=40)
    lb=ttk.Combobox(window,textvariable=am)
    lb['values']=('a.m.','p.m.')
    lb.place(x=231,y=150,width=40)
    lb.current(1)
    
    window.event1=0
    window.event_date=0
    window.event_time=0
    def pick():
        window.event1 = event.get()
        window.event_date = ev_date.get()
        hrs1 = hrs.get()
        m1 = min1.get()
        am1 = am.get()
        window.event_time = hrs1+':'+m1+' '+am1
        window.destroy()
    bn = Button(window,bg="blue",fg="white",font="arial 11 bold",text="Done",command=pick)
    bn.place(x=100,y=200,width=100)
    speak.say("Please enter the event details in the reminder window that appears in front of you.")    
    speak.runAndWait()
    window.mainloop()
    a = [window.event1,window.event_date,window.event_time]
    return a

    
def reminder():

    connection = sqlite3.connect("reminder.db")
    db = connection.cursor()
    try:
        db.execute("create table event(Event varchar(100), Date date, Time varchar(20))")
    except:
        pass
    speak.say("Please tell me the event name.")
    speak.runAndWait()
    print("\nSpeak...\n")
    audio1 = rec.listen(source,phrase_time_limit=5)
    event1 = rec.recognize_google(audio1)
    print(event1)
    
    speak.say("Ok! now I want to know the event date.")
    speak.runAndWait()
    speak.say("Please tell me the month")
    speak.runAndWait()
    print("\nSpeak...\n")
    audio1 = rec.listen(source,phrase_time_limit=5)
    month = rec.recognize_google(audio1)
    print(month)    
    speak.say("now please tell me the date of event")
    speak.runAndWait()
    print("\nSpeak...\n")
    audio1 = rec.listen(source,phrase_time_limit=5)
    date1 = rec.recognize_google(audio1)
    print(date1)
    month=month_val(month)
    today_date= date.today()
    ev_date = str(today_date.year)+'-'+str(month)+'-'+str(date1)

    speak.say("Okay! now please tell me the event time.")
    speak.runAndWait()
    print("\nSpeak...\n")
    audio1 = rec.listen(source,phrase_time_limit=5)
    time1 = rec.recognize_google(audio1)
    print(time1)
    
    speak.say("OK! your event is "+str(event1)+"on date"+str(date1)+" "+str(month)+"at time"+str(time1))
    print("\n Event: "+str(event1),"\n","Date: "+str(ev_date),"\n","Time: "+str(time1))
    speak.runAndWait()
    speak.say("Please tell me, is all the information correct?")
    speak.runAndWait()
    print("\nSpeak...\n")
    audio1 = rec.listen(source,phrase_time_limit=5)
    ack = rec.recognize_google(audio1)
    ack = ack.lower()
    print(ack)
    event1=str(event1)
    if any(x in ack for x in ["y","yes","yeah","yup","yo","correct"]):
        db.execute("insert into event values(?,?,?)",(event1,ev_date,time1))
        connection.commit()
        speak.say("OK! your event has been set.")
        speak.runAndWait()
    else:
        speak.say("I am so sorry for that.")
        dt=[]
        dt=date_time()
        print(dt)
        a=dt[0]
        b=dt[1]
        c=dt[2]
        db.execute("insert into event values(?,?,?)",(a,b,c))
        connection.commit()
        speak.say("Your event has now been set.")
        speak.runAndWait()
    
        

def work(text):    
    if "open" in text:
        speak.say("Okay!")
        open_app(text)
    elif "search" in text:
        google_search(text)
    elif "play" in text:
        play_(text)
    elif "joke" in text:
        joke()
    elif any(x in text for x in ["remind","reminder","event","meeting","reminders","events"]):
        if any(y in text for y in ["list","lists","show","tell"]):
            speak.say("Here is the list of all the events and reminders")
            conn = sqlite3.connect("reminder.db")
            db = conn.cursor()
            try:
                t=0
                eve = db.execute("select * from event")
                eve = eve.fetchall()
                print("\n      Events".ljust(35," "),"      Date".ljust(20," "),"      Time")
                for q in eve:
                    t+=1
                    print(str(t)+".",q[0].ljust(35," "),q[1].ljust(20," "),q[2])
            except:
                speak.say("There is no such event yet. You can tell me to add one.")
        else:
            speak.say("Okay! Tarra is going to set a reminder for you.")
            speak.runAndWait()
            reminder()
    else:
        text = text.split()
        webbrowser.open("https://www.google.com/search?q=" + '+'.join(text))            

           
def wait(text):
    speak.say("Ok! for how many seconds I should wait for you?")
    speak.runAndWait()
    print("\nSpeak")
    audio1 = rec.listen(source,phrase_time_limit=5)
    text1 = rec.recognize_google(audio1)
    print("\n"+text1)
    wait_time = 0
    text2 = [x for x in text1.split() if x.isdigit()]
    if len(text2)!=0:
        wait_time = int(text2[0])
    speak.say("Tarra is going to rest for"+str(wait_time)+"seconds")
    speak.runAndWait()
    time.sleep(wait_time)
    speak.setProperty('rate',70)
    speak.say("Hmmmmm...! Wow...! what a sleep.")
    speak.setProperty('rate',110)
    speak.say("Now I am here for you")
    speak.runAndWait()
    speak.setProperty('rate',170)
    
    
if __name__ == "__main__":
    
    speak.say("hey there! I am Taara, your personal assistant. What should I call you")
    speak.runAndWait()    #for giving the command to speak
    print("Speak...")

    try:
        with sr.Microphone() as source:                            # Microphone() requires pyaudio package to work
            rec.adjust_for_ambient_noise(source, duration=0.2)     # it will automatically adjust the threshold of voice
            audio=rec.listen(source, phrase_time_limit = 5)        # it will listen the voice till 5 seconds     
            text1 = rec.recognize_google(audio)                     
            text1 = text1.lower()                                        
            """speak1=gTTS(text="hello"+text1+"glad to see you")
            speak1.save("wish2.mp3")
            print(text1)
            os.system("wish2.mp3")"""
            print("\n"+text1)
            speak.say("hello"+text1+"!glad to see you.")
            speak.runAndWait()
        
            while(1):
                speak.say("Tell me, what should I do for you?")
                speak.runAndWait()
                print("\nSpeak...")
                rec.adjust_for_ambient_noise(source, duration=0.3)
                audio=rec.listen(source,phrase_time_limit=5)
                text=rec.recognize_google(audio)
                text=text.lower()
                print("\n"+text)
                close=["exit","stop","quiet","nothing","shut up","shutup"]
                if any(x in text for x in close):
                    speak.say("OK then! nice talking to you, Good Bye!")
                    speak.runAndWait()
                    break
            
                elif "wait" in text:
                    wait(text)
                
                else:
                    work(text)
                    time.sleep(2)

    except sr.RequestError as e:           # this exception will be thrown when there is no internet connection    
         # print("Could not request results; {0}".format(e))
         speak.say("Please check your internet connection. I am not able to recognize your voice.")
         speak.runAndWait()
     
          
    except sr.UnknownValueError:           # this exception will be thrown when recognizer did not recognize any audio
    
         # print("unknown error occured")
         speak.say("Looks like you don't wanna talk to me. OK! no problem, see you soon")
         speak.runAndWait()
         



