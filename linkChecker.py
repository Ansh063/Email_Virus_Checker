#!/usr/bin/env python3

import requests
import json
from termcolor import colored
import time 

def GetStatus():
    return temp

def linkchecker(api_key):
    url = "https://www.virustotal.com/vtapi/v2/url/report"
    api = api_key
    fp = open("links.txt","r")
    lines = fp.readlines()
    for line in lines :
        if len(line) < 1:
            continue
        resource = line
        params = {'apikey':api,'resource': resource}
        #response = requests.get(url,params=params)
        response = requests.get(url,params=params)
        json_response = json.loads(response.text)
        #print(colored('[+] Link Not Reachable ','blue'))
        if(json_response['response_code'] == 1):
            if(json_response['positives'] <= 1):
                t = colored('[+] Not Malicious','green')
                line = line.strip('\n')
                print(t+" "+line)
            else:
                temp = False
                t = colored('[-] Malicious','red')
                line = line.strip('\n')
                print(t + " " + line)
        else:
            t = colored('[?] Link not Exist in Database','yellow')
            line = line.strip('\n')
            print(t + " " + line)
        time.sleep(20)

temp = True
#linkchecker()
