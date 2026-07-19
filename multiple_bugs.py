import subprocess
import os

password = "admin123"

def run(cmd):
    subprocess.call(cmd, shell=True)

def add(a: int, b: int) -> int:
    return str(a + b)

print(undefined_variable)