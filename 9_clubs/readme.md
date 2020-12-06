This one is simple ascii telnet server which gives you 3 menu options which take user input. Tried to fuzz it. Fuzzed from 0-7000 on option 1, 0-2500 on option 2 and 0-2500 on option 3 and didnt get any except the snippet below.

b'Thanks for your feedback!\n': 508
b"Thanks for your feedback!\n\nWelcome to the '9 of Clubs' service.\n-------------------------------\nPlease choose an option:\n1. Send contact info\n2. Greetings\n3. Send feedback\n0. Exit\n\x00": 509
b"Thanks for your feedback!\n\nWelcome to the '9 of Clubs' service.\n-------------------------------\nPlease choose an option:\n1. Send contact info\n2. Greetings\n3. Send feedback\n0. Exit\n\x00": 510

b'Unknown option.\n': 786
b"Thanks for your feedback!\n\nWelcome to the '9 of Clubs' service.\n-------------------------------\nPlease choose an option:\n1. Send contact info\n2. Greetings\n3. Send feedback\n0. Exit\n\x00": 787


No obvious crashes. All the input anomalies can be explained via the IO buffering
