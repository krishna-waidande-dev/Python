#This program blocks the access to below mentioned sites for time between 9 AM to 5 PM (Working hours). To increase our productivity.

import time
from datetime import datetime as dt

host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirectIP = "127.0.0.1"
websites = ["www.facebook.com", "facebook.com", "www.gmail.com", "gmail.com"]
curr=dt.now()

def addWebsites():
    with open(host_path,'r+') as file:
        content=file.read()

        for website in websites:
            if website in content:
                pass
            else:
                file.write("\n" + redirectIP + "\t" + website)

def removeWebsites():
    with open(host_path, 'r+')  as file:
        content=file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in websites):
                file.write(line)
        file.truncate()

def main():
    while True:
        if dt(curr.year, curr.month, curr.day, 9) < dt.now() < dt(curr.year, curr.month, curr.day, 17):
            addWebsites()
        else:
            removeWebsites()
        time.sleep(5)
main()
