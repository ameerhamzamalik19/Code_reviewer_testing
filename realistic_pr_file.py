import hashlib
import subprocess

API_KEY = "secret123"

def execute(cmd):
    subprocess.call(cmd, shell=True)

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def add(a: int, b: int) -> int:
    return str(a + b)