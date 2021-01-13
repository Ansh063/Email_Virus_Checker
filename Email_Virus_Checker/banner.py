#!/usr/bin/python3

import pyfiglet
from termcolor import colored
def ussage():
    print(colored('                                          :- Ansh Goyal','cyan'))
    print()
    print(colored('Ussage : IMAP_Connection.py [GmailID] [Password] [Virustotal API Key ]','red'))
    print()
    print(colored(('-'*70),'cyan'))
    print()

def banner():
    ascii_banner = pyfiglet.figlet_format("Email Virus Checker")
    print(colored(ascii_banner,'cyan'))
    ussage()
    return 
#banner()


