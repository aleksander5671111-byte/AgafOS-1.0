import time

print("starting AgafOS")
time.sleep(3)
print("Loading...")
time.sleep(5)
print("Type 'help' to enter list of commands")
time.sleep(3)
print("Alpha v1.0")
print("Aleksan Corporation")
print("If you want to support the project you can donate:https://www.donationalerts.com/r/sasgha_2323")
while True:
    command1 = input("C:")
    if command1 == "systeminfo":
        print("Version 1.0 Uknown Copy")
    if command1 == "help":
        print("systeminfo - shows properties of your system, calculator, consent, version, information. ")
    if command1 == "calculator":
        print(eval(input('>>>')))
    if command1 == "consent":
        print("You agree to the use of AgafOS 1 Yes  2 No")
    if command1 == "information":
        print("AgafOS is a console operating system that runs on python.")
    if command1 == "version":
        print("Alpha 1.0 - 1.3 Beta: 1.4 - 1.7 release 1.8 - now version")