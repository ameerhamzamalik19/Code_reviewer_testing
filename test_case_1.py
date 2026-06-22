import os
import subprocess

def unsafe(user_input):
    password = "secret123"

    eval(user_input)

    print(password)

    return 123


x = unsafe("print('hello')")