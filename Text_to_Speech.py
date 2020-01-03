
# TEXT TO SPEECH
import pyttsx3
import datetime
text_to_speech = pyttsx3.init()

text_to_speech.say("ENTER YOUR NAME")
text_to_speech.runAndWait()

Name = input("Enter Your Name:")
text_to_speech.say("Hello " +Name )
text_to_speech.runAndWait()

text_to_speech.say("ENTER YOUR Birthday Month")
text_to_speech.runAndWait()

Bday_Month = input("Enter your Birthday Month:")
get = datetime.datetime.now()
get_current_month = get.strftime("%B")
print(get_current_month)


if(Bday_Month == get_current_month):
    print("Happy Birthday Wish You all Success in Upcoming Years" +Name)
    text_to_speech.say("Happy Birthday Wish You all Success in Upcoming Years" +Name)
    text_to_speech.runAndWait()
else:
    print("Its Not Your birthday month")
    text_to_speech.say("Its Not Your birthday month")
    text_to_speech.runAndWait()

















