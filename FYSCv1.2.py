# PYFYSCV1.3AUG2
# -------IMPORTING-------
import time
import random
import threading
import pickle
import os
import sys

# -------DATABASE-------
base_path = os.getcwd()
file_name = "data/mydata.txt"
file_name2 = "data/mydata2.txt"
file_name3 = "data/mydata3.txt"
Udatafile_name1 = "data/Udata1.txt"
Udatafile_name2 = "data/Udata2.txt"
Udatafile_name3 = "data/Udata3.txt"
fyscdollarfile = "data/fyscdollar.txt"
full_path = os.path.join(base_path, file_name)
full_path2 = os.path.join(base_path, file_name2)
full_path3 = os.path.join(base_path, file_name3)
Upath1 = os.path.join(base_path, Udatafile_name1)
Upath2 = os.path.join(base_path, Udatafile_name2)
Upath3 = os.path.join(base_path, Udatafile_name3)
Upath4 = os.path.join(base_path, fyscdollarfile)


file_path = r"%s"%(full_path)
print(full_path)
file_path2 = r"%s"%(full_path2)
print(full_path2)
file_path3 = r"%s"%(full_path3)
print(full_path3)
Upath1 = r"%s"%(Upath1)
Upath2 = r"%s"%(Upath2)
Upath3 = r"%s"%(Upath3)
Upath4 = r"%s"%(Upath4)

# -------VARIABLE SETUP-------
U1boost = 1
U1cost = 100
tupU1 = 0
U2num = 0 # no save for now
U2str = 'coming soon' # no save for now
U2cost = 0 # no save for now
fyscdollar = 0

subs = 0
growth = 0
repeat = 0
ctime = 0

# for update use (reset all data)
"""with open(file_path, "wb") as f:
    pickle.dump(subs, f, pickle.HIGHEST_PROTOCOL)
with open(file_path2, "wb") as f:
    pickle.dump(growth, f, pickle.HIGHEST_PROTOCOL)
with open(file_path3, "wb") as f:
    pickle.dump(ctime, f, pickle.HIGHEST_PROTOCOL)
with open(Upath1, "wb") as f:
    pickle.dump(U1boost, f, pickle.HIGHEST_PROTOCOL)
with open(Upath2, "wb") as f:
    pickle.dump(U1cost, f, pickle.HIGHEST_PROTOCOL)
with open(Upath3, "wb") as f:
    pickle.dump(tupU1, f, pickle.HIGHEST_PROTOCOL)
with open(Upath4, "wb") as f:
    pickle.dump(fyscdollar, f, pickle.HIGHEST_PROTOCOL)"""

# -------CLEAN SCREEN-------
def clear_screen_ansi():
    print("\033[H\033[2J", end="")

# -------LOAD DATA-------
with open(file_path, "rb") as f:
    subs = pickle.load(f)
    print('loaded', subs,)
    subs = float(subs)
with open(file_path2, "rb") as f:
    growth = pickle.load(f)
    print('loaded', growth,)
    growth = float(growth)
with open(file_path3, "rb") as f:
    ctime = pickle.load(f)
    print('loaded', ctime,)
with open(Upath1, "rb") as f:
    U1boost = pickle.load(f)
    print('loaded', U1boost,)
    U1boost = float(U1boost)
with open(Upath2, "rb") as f:
    U1boost = pickle.load(f)
    print('loaded', U1cost,)
    U1cost = int(U1cost)
with open(Upath3, "rb") as f:
    U1boost = pickle.load(f)
    print('loaded', tupU1,)
    tupU1 = int(tupU1)
with open(Upath4, "rb") as f:
    U1boost = pickle.load(f)
    print('loaded', fyscdollar,)
    fyscdollar = float(fyscdollar)

if ctime == 0:
    ctime = time.time()
    
otime = time.time()

offlinetime = int(otime - ctime)

print('total offline time:', offlinetime, 'seconds')

while repeat < offlinetime / 2:
    print(f"\rProcessing item {repeat} of {offlinetime / 2}...", end="")
    subs += growth / 50000
    fyscdollar += growth / 50000 / 100
    growth -= growth / 50000
    repeat += 1
print("\nDone!")
print('subs now:', subs)
ttime = time.time()
print('total time used to cal:', (ttime - otime) * 1000, 'ms')

clear_screen_ansi()
    

print('Welcome to Python FYSC v1.3. type "help" if you need help. type "cmd" if you dont know the command.')

def growths():
    while True:
        global subs
        global growth
        global fyscdollar
        global ctime 
        time.sleep(2)
        subs += growth / 50000
        fyscdollar += growth / 50000 / 100
        growth -= growth / 50000
        ctime = time.time()
        with open(file_path, "wb") as f:
            pickle.dump(subs, f, pickle.HIGHEST_PROTOCOL)
        with open(file_path2, "wb") as f:
            pickle.dump(growth, f, pickle.HIGHEST_PROTOCOL)
        with open(file_path3, "wb") as f:
            pickle.dump(ctime, f, pickle.HIGHEST_PROTOCOL)

def savedata():
    while True:
        global U1boost
        global U1cost
        global tupU1
        global fyscdollar
        time.sleep(2)
        with open(Upath1, "wb") as f:
            pickle.dump(U1boost, f, pickle.HIGHEST_PROTOCOL)
        with open(Upath2, "wb") as f:
            pickle.dump(U1cost, f, pickle.HIGHEST_PROTOCOL)
        with open(Upath3, "wb") as f:
            pickle.dump(tupU1, f, pickle.HIGHEST_PROTOCOL)
        with open(Upath4, "wb") as f:
            pickle.dump(fyscdollar, f, pickle.HIGHEST_PROTOCOL)


threadgrowth = threading.Thread(target=growths)
threadgrowth.daemon = True
threadgrowth.start()
savedata = threading.Thread(target=savedata)
savedata.daemon = True
savedata.start()

while True:
    command = input('Enter Command: ')
    if command == 'video':
        randomnum = random.randrange(1,5)
        if randomnum == random.randrange(1,5):
            randomgrowth = random.randrange(200, 1200) * U1boost
            growth += randomgrowth
            print('wow! you put good effort on your video and end up getting %d growth!'%(randomgrowth))
        else:
            randomgrowth = random.randrange(60, 300) * U1boost
            growth += randomgrowth
            print('you put some effort on your video. end up getting %d growth.'%(randomgrowth))
    elif command == 'short' and subs >= 1000:
        randomnum = random.randrange(1,5)
        if randomnum == random.randrange(1,5):
            randomgrowth = random.randrange(300, 2000) * U1boost
            growth += randomgrowth
            print('wow! you put good effort on your short and end up getting %d growth!'%(randomgrowth))
        else:
            randomgrowth = random.randrange(75, 600) * U1boost
            growth += randomgrowth
            print('you put some effort on your short. end up getting %d growth.'%(randomgrowth))
    elif command == 'short' and subs <= 1000:
        print("you haven't reached the requirement for you to upload shorts. type the command milestone to learn more.")
    elif command == 'help':
        print('This is Python FYSC. A new stage of FYSC. In there, you can gain subscribers by typing "video" or "short" in the command panel. In the future, we will expect upgrades added to this FYSC!')
    elif command == 'cmd':
        print("""Commands:
video / short: upload a video onto the FYSC to gain subs. 
help: get help. cmd: get the list of commands. 
end: help you save the data and tell you to press the x button. 
stats: get your stats.
milestone: see milestone.
upgrade: see upgrades (10000 subs required)""")
    elif command == 'stats':
        print("""
your subs is %d.
your growth is %d.
"""%(subs, growth))
    elif command == 'end':
        print('saving...')
        ctime = time.time()
        with open(file_path, "wb") as f:
            pickle.dump(subs, f, pickle.HIGHEST_PROTOCOL)
            print('saved', subs)
        with open(file_path2, "wb") as f:
            pickle.dump(growth, f, pickle.HIGHEST_PROTOCOL)
            print('saved', growth)
        with open(file_path3, "wb") as f:
            pickle.dump(ctime, f, pickle.HIGHEST_PROTOCOL)
            print('saved', ctime)
        print('Ending...')
        sys.exit(0)
        print('END FAILED')
    elif command == 'milestone':
        if subs >= 1000:
            milestone1 = int(0)
            eta1 = str(0)
        else:
            milestone1 = 1000 - subs
            eta1 = milestone1 /(growth / 50000 / 2)
        if subs > 10000:
            milestone2 = int(0)
            eta2 = str(0)
        else:
            milestone2 = 10000 - subs
            eta2 = milestone2 /(growth / 50000 / 2)
        if subs > 1000000:
            milestone3 = int(0)
            eta3 = str(0)
        else:
            milestone3 = 1000000 - subs
            eta3 = milestone3 /(growth / 50000 / 2)
        print("""
Milestone (subs left for milestone)
1,000 subs(requirement for shorts): %d ETA: %s seconds
10,000 subs(requirement for upgrades): %d ETA: %s seconds
1,000,000 subs: %d ETA: %s seconds"""%(milestone1,eta1, milestone2,eta2, milestone3, eta3))
    elif command == 'upgrade' and subs >= 10000:
        ucommand = input("""
Upgrade Shop

FYSC Dollars: %d
U1: Better Video and Short: gain more growth on them. Current boost: %d
Cost: %d
Command to buy: buyU1
U2: Worker: worker help you upload video while you are offline. upload every %d %s
Cost: %d
Command to buy: COMING SOON
Type Upgrade Command Here: """%(fyscdollar, U1boost, U1cost, U2num, U2str, U2cost))
        if ucommand == 'buyU1':
            buyU1cal = U1cost
            print(buyU1cal)
            cal = fyscdollar
            print(cal)
            maxbuyU1 = 0
            if U1cost < cal:
                while cal > 0:
                    cal -= buyU1cal
                    buyU1cal *= 1.05
                    maxbuyU1 += 1
                maxbuyU1 -= 1
            utobuy1 = input("how many upgrades to buy? max is %d. Type number here: "%(maxbuyU1))
            utobuy1 = int(utobuy1)
            if isinstance(utobuy1, int) == True:   
                print(isinstance(utobuy1, int))
                if utobuy1 <= maxbuyU1:
                    print('doing it')
                    repeat2 = 0
                    while utobuy1 > repeat2:
                        repeat2 += 1
                        fyscdollar -= U1cost
                        U1cost *= 1.05
                        U1boost += 0.1
                        tupU1 += 1
                        
                    print("you have now %d upgrades. You have %d fysc dollar now."%(tupU1, fyscdollar))
                
                
                
    elif command == 'upgrade' and subs <= 10000:
        print("you didn't meet the requirement to go to the upgrade shop.")
        






