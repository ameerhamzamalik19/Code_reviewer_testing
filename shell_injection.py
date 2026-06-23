import subprocess

def ping(host):
    subprocess.call(f"ping {host}", shell=True)