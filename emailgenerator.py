import random
from colorama import Fore, Style, init
from time import sleep

# Initialize colorama
init()
#####################

n = int(input("How many email(s) could i generate?\n"))

s = str(n)

if(n > 0):
    if(n > 1):
        print(Fore.YELLOW+"[!] "+s+" emails being generated")
    else:
        print(Fore.YELLOW+"[!] "+s+" email being generated")
    #####################################  GENERATING EMAILS  ##################################
    for x in range(1,n+1):
        print(Fore.GREEN+"["+str(x)+"] "+Fore.MAGENTA+random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")+str(random.randint(1,10000))+random.choice(["@1secmail.com","@1secmail.net","@1secmail.org"]))
    ########################################  FINISHED!  #######################################
    print(Fore.BLUE+"[i] "+s+" email(s) have been generated!")
else:
    print(Fore.RED+"[#] Please enter only numbers!")
    sleep(2)
