import random as rn
import time as tm
import math
import os
import sys

file_extensions = [".hell", ".dpp"]
tape = [0] * 250
pointer = 0
code = ""
variables = {}


if file_extensions[0] in sys.argv[1] or file_extensions[1] in sys.argv[1]:
    with open(sys.argv[1], "r") as fl:
        print(sys.argv[1])
        content = fl.read()
        content = content.strip()
        code = content
        for line in code:
            line.strip()
            if ">" in line:
                if comment_mode == True:
                    continue
                else:
                    pointer += 1
            if "<" in line:
                if comment_mode == True:
                    continue
                else:
                    pointer -= 1
            if "." in line:
                if comment_mode == True:
                    continue
                else:
                    print(tape[pointer])
            if "+" in line:
                if comment_mode == True:
                    continue
                else:
                    tape[pointer] = int(tape[pointer])
                    tape[pointer] += 1
                    tape[pointer] = str(tape[pointer])
            if "-" in line:
                if comment_mode == True:
                    continue
                else:
                    tape[pointer] = int(tape[pointer])
                    tape[pointer] -= 1
                    tape[pointer] = str(tape[pointer])
            if "@" in line:
                if comment_mode == True:
                    continue
                else:
                    print(tape)
                    tape.clear()
                    tape = [""] * 250
            if "," in line:
                if comment_mode == True:
                    continue
                else:
                    quit()
            if "$" in line:
                comment_mode = True
                continue
            if "/" in line:
                comment_mode = False
            if "," not in code:
                raise Exception("SyntaxError: You forgot the ',' dimwit, learn how to code....")
            if ">" not in code and "<" not in code:
                i = 0
                while i != 20:
                    i += 1
                    print("Imagine staying in one cell for the entire code pussy 🐱")
                    tm.sleep(0.5)
                os.system("reboot")
            


#
else:
    Exception("RuntimeError: NoFileLoadable, maybe next time put a filename you dumbass, just for that im restarting your computer")
    os.system("restart")
            
                            