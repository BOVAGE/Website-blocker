import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websiteList = ["www.facebook.com", "facebook.com", "nairaland.com", "www.nairaland.com"]

while True:
    if 8 < dt.now().hour < 23:
        with open(hosts_path, "r+") as file:
            content = file.read()
            for site in websiteList:
                if site in content:
                    pass
                else:
                    file.write(f"{redirect}\t{site}\n")
        print("Working hours......")
        time.sleep(5)
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websiteList):
                    file.write(line)
            file.truncate()
        print("Enjoy!Enjoy!Enjoy!")
        time.sleep(5)
