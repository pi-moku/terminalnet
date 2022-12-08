# terminalnet
# domain Examples
# ttt.a.com
# ttt.b.com
import os
import sys
import re

print("terminalnet")
while True:
    cmd = input("cmd > ")
    if cmd == "see":
        while True:
            dmain = input("dmain > ")
            if os.path.isfile(dmain):
                f = open(dmain)
                src = f.read()
                f.close()
                print(src)
            elif dmain == "see_end":
                break
            else:
                print("not found")
    elif cmd == "write":
        title = input("title > ")
        gyousuu = input("How many lines? > ")
        if bool(re.match(r'ttt.[a-z]*.com',title)):
            if os.path.isfile(title):
                print("already exists with the same name.")
                sys.exit()
            else:
                pass
        else:
            print("Please write at ttt.().com")
            sys.exit()
        try:
            gyousuu = int(gyousuu)
        except:
            print("please enter well")
            sys.exit()
        for i in range(gyousuu):
            a = input("> ")
            if a:
                f = open(title,'a')
                f.write(f"{a}\n")
                f.close()
            else:
                print('I have not entered the',i,'line, but I will write it in the content')
                f = open(title,"a")
                f.write(a,"\n")
                f.close()
    elif cmd == "end":
        sys.exit()
    else:
        print("command error")
