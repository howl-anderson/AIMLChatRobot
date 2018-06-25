#!/usr/bin/env python

import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("main.xml")
kernel.respond("load aiml")

# Press CTRL-C to break this loop
while True:
    print(kernel.respond(input("Enter your message >> ")))