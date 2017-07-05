#!/usr/bin/python3

import time
import subprocess
import re


def getTemp():
    """Gets GPU temperature."""
    p1 = subprocess.Popen(['atitweak', '-s'], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['grep', 'temp'], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    out, err = p2.communicate()
    temp = float(re.search(r'(?<= )[0-9].*[0-9](?= )', str(out)).group(0))
    return temp


def killMinerScreen():
    """Gets detached screen ID containing mining session. Mining session is highest number."""
    p1 = subprocess.Popen(['screen', '-ls'], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['grep', 'Detached'], stdin=p1.stdout, stdout=subprocess.PIPE)
    p3 = subprocess.Popen(['cut', '-d.', '-f1'], stdin=p2.stdout, stdout=subprocess.PIPE)
    p4 = subprocess.Popen(['awk', '{print $1}'], stdin=p3.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    out, err = p4.communicate()
    ids = [int(i) for i in str(out)[2:-1].split("\\n")[:-1]]
    mnr_id = max(ids)
    subprocess.call(['kill', str(mnr_id)])
    print("Killed ", mnr_id)


while True:
    temperature = getTemp()
    print(temperature)
    if temperature > 89.9:
        killMinerScreen()
        break
    time.sleep(900)
