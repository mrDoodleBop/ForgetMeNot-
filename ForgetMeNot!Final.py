'''
Created on: January 25, 2021
Created by: Michael Cates
Created for: Reminder App(ForgetMeNot!)
'''
import webbrowser
import smtplib
from email.message import EmailMessage
from tkinter import *

root = Tk()
root.title("ForgetMeNot!")
#List for saving info:
infoList = []
#Key for finding all the values in infoList:
'''
infoList[0] = userName
infoList[1] = loginTime
infoList[2] = URL choice
infoList[3] = user phone number
infoList[4] = user email address
'''

#Function Definitions:

def email_Alert(subject, body, to):#This one sends the success message
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "Mikeyhc31922@gmail.com"
    msg['from'] = user
    password = "itovzxhpralnmrca"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

def email_Alert2(subject, body, to): #This one send the assignment alert statement
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "Mikeyhc31922@gmail.com"
    msg['from'] = user
    password = "itovzxhpralnmrca"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    from datetime import datetime
    now = datetime.now()
    basic = (str(now.hour) + ":" + str(now.minute))
    loginTime = (hourText.get() + ":" + minuteText.get())
    while basic != loginTime:
        now = datetime.now()
        basic = (str(now.hour) + ":" + str(now.minute))
    server.send_message(msg) #This part is da belle of da ball#


    server.quit()

def send_Mail_Alert():
    userService = carrierText.get()
    userService = userService.lower().capitalize()
    #Checking the service providers:

    if "Cricket" in userService:
        userService = "@mms.cricketwireless.net"
    elif "Boost" in userService:
        userService = "@sms.myboostmobile.com"
    elif "At&t" in userService:
        userService = "@txt.att.net"
    elif "Google" in userService:
        userService = "@msg.fi.google.com"
    elif "Republic" in userService:
        userService = "@text.republicwireless.com"
    elif "Sprint" in userService:
        userService = "@messaging.sprintpcs.com"
    elif "Straight" in userService:
        userService = "@vtext.com"
    elif "mobile" in userService:
        userService = "@tmomail.net"
    elif "Ting" in userService:
        userService = "@message.ting.com"
    elif "Cellular" in userService:
        userService = "@email.uscc.net"
    elif "Verizon" in userService:
        userService = "@vtext.com"
    elif "Virgin" in userService:
        userService = "@vmobl.com"

    userNum = numText.get() + userService
    userName = nameText.get().lower().capitalize()
    loginTime = hourText.get() + ':' + minuteText.get() + ':' + '0'
    website = urlText.get()
    userMail = mailText.get()
#Success Message/ add info to list:
    infoList.append(userName)
    infoList.append(loginTime)
    infoList.append(website)
    infoList.append(userNum)
    infoList.append(userMail)
    print(infoList)
    email_Alert("Hey " + userName + "!", "Your reminder was successfuly set up!", userMail)
    email_Alert("Hey " + userName + "!",  "Your reminder was successfuly set up!", userNum)
    from datetime import datetime
    now = datetime.now()
    basic = (str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))


#Open URL:
    now = datetime.now()
    basic = (str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
    loginTime = (hourText.get() + ":" + minuteText.get() + ":0")
    while basic != loginTime:
        now = datetime.now()
        basic = (str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
        if now.hour >= 12:
            print("It is " + basic + " pm!")
        elif now.hour < 12:
            print("It is " + basic + " am!")
    webbrowser.open(website, 1)
    if now.hour >= 12:
        print("Final alert was sent at " + basic + " pm!")
    if now.hour < 12:
        print("Final alert was sent at " + basic + " am!")
#Alert Message:
    email_Alert2("ALERT!",userName.upper() + ", THIS IS YOUR REMINDER! YOUR URL IS OPEN ON YOUR COMPUTER NOW! GO BE PRODUCTIVEEEEEE!!!!!", userMail)
    email_Alert2("ALERT!", userName.upper() + ", THIS IS YOUR REMINDER! YOUR URL IS OPEN ON YOUR COMPUTER NOW! GO BE PRODUCTIVEEEEEE!!!!!", userNum)


#ForgetMeNot! Front-End:

#Getting the username:
nameLabel = Label(root, text='Please enter your name: ')
nameLabel.grid(row=0, column=0, padx=5, pady=5)

nameText = Entry(root, width=50)
nameText.grid(row=0, column=1, padx=5, pady=5)


#Time Choice: Hour and Minute Separate:

hourLabel = Label(root, text='Please enter the hour you would like to be reminded(in 24 hour time): ')
hourLabel.grid(row=2, column=0, padx=5, pady=5)

hourText = Entry(root, width=50)
hourText.grid(row=2, column=1, padx=5, pady=5)

minuteLabel = Label(root, text='Please enter the minute you would like to be reminded: ')
minuteLabel.grid(row=3, column=0, padx=5, pady=5)

minuteText = Entry(root, width=50)
minuteText.grid(row=3, column=1, padx=5, pady=5)


#Website URL identification:

urlLabel = Label(root, text='What is the full URL you would like to open' + '?')
urlLabel.grid(row=5, column=0, padx=5, pady=5)

urlText = Entry(root, width=50)
urlText.grid(row=5, column=1, padx=5, pady=5)


#Phone Number and Service Carrier Identification:

userNum = Label(root, text='What is the number I can remind you at? ')
userNum.grid(row=7, column=0, padx=5, pady=5)

numText = Entry(root, width=50)
numText.grid(row=7, column=1, padx=5, pady=5)

userCarrier = Label(root, text='Please enter your phone carrier: ')
userCarrier.grid(row=9, column=0, padx=5, pady=5)

carrierText = Entry(root, width=50)
carrierText.grid(row=9, column=1, padx=5, pady=5)


#User email identification:

userMail = Label(root, text='Please enter a valid email address: ')
userMail.grid(row=11, column=0, padx=5, pady=5)

mailText = Entry(root, width=50)
mailText.grid(row=11, column=1, padx=5, pady=5)

#Set Reminder Button:
setBtn = Button(root, text='Set Reminder', command=send_Mail_Alert)
setBtn.grid(row=13, column=1, padx=5, pady=5)


root.mainloop()
