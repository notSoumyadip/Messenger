#You should log in to whats app web firsthand, and you just have to do one thing after the program finishes execution i.e. press enter to send the message!

import pywhatkit as kit

phone_number = "+917607727261"

message = "Hello, this is a test message from Python!"

hour = int(input("Enter Hour: "))    #in 24hr format like 00 to 24
min = int(input("Enter Minutes: "))    # normal 0-59

kit.sendwhatmsg(phone_number, message, hour,min)