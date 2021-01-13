#!/usr/bin/env python3 

# For Checking all the attachments 

from termcolor import colored
import requests
import time
import json
import os
temp2 = True
def GetStatus2():
    return temp2


def attachments_checker(api_key):
    path = os.getcwd()
    path = path + "/Attachments/"
    # print(os.listdir(path))
    for ftc in os.listdir(path):
        flag1 = 3
        flag2 = 3
        flag3 = 3
        url = "https://www.virustotal.com/vtapi/v2/file/scan"
        api = api_key
        params = {'apikey': api}
        #print(ftc)
        file_path = path + ftc
        #print(file_path)
        files = {'file': (ftc, open(file_path, "rb"))}
        response = requests.post(url, files=files, params=params)
        #print(response.status_code)
        #print(response.text)
        response_json = json.loads(response.text)
        #time.sleep(30)
        #print(response_json)
        
        #print(response_json['response_code'])
        if (response_json['response_code'] == 1):
            url = "https://www.virustotal.com/vtapi/v2/file/report"
            scan_id = response_json["scan_id"]
            params2 = {'apikey': api, 'resource': scan_id}
            response2 = requests.get(url, params=params2)
            response_json2 = json.loads(response2.text)
            if(response_json2['response_code'] == 1):
                if(response_json2['positives'] <= 0):
                    t = colored(' [+] Not Malicious', 'green')
                    print(ftc + " " + t)
                else:
                    temp2 = False
                    t = colored('[-] Malicious','red')
                    print(ftc + " " + t)

            elif(response_json2['response_code'] == 0):
                t = colored(' [?] Not found in Database','yellow')
                print(ftc+' '+t)
            else:
                while(response_json2['response_code'] == -2 and flag1 > 1):
                    #time.sleep(30)
                    response2 = requests.get(url, params=params2)
                    response_json2 = json.loads(response2.text)
                    print(colored("Response Not Ready Wait for 60 Second...",'blue'))
                    flag1 = flag1-1
                    time.sleep(60)
                if(response_json2['response_code'] == 1):
                    if(response_json2['positives'] <= 0):
                        t = colored(' [+] Not Malicious', 'green')
                        print(ftc + " " + t)
                    else:
                        temp2 = False
                        t = colored('[-] Malicious','red')
                        print(ftc + " " + t)
                else:
                    t = colored(' [?] Not found in Database','yellow')
                    print(ftc+' '+t)
        elif(response_json['response_code']==0):
            t = colored(' [?] Not Found in Database','yellow')
            print(ftc + " "+t)
        else:
            while(response_json['response_code'] == -2 and flag2 > 1):
                #time.sleep(30)
                response = requests.post(url, files=files, params=params)
                response_json = json.loads(response.text)
                flag2 = flag2-1
                print(colored("Response Not Ready Wait for 60 Second...",'blue'))
                time.sleep(60)
            url = "https://www.virustotal.com/vtapi/v2/file/report"
            scan_id = response_json["scan_id"]
            params2 = {'apikey': api, 'resource': scan_id}
            response2 = requests.get(url, params=params2)
            response_json2 = json.loads(response2.text)
            if(response_json2['response_code'] == 1):
                if(response_json2["positives"] <= 0):
                    t = colored(' [+] Not Malicious', 'green')
                    print(ftc + " " + t)
                else:
                    temp2 = False
                    t = colored('[-] Malicious','red')
                    print(ftc + " " + t)
            elif(response_json2['response_code'] == 0):
                t = colored(' [?] Not found in Database','yellow')
                print(ftc + " " + t)
            else:
                while(response_json2["response_code"] == -2 and flag3 > 1):
                    #time.sleep(30)
                    response2 = requests.get(url, params=params2)
                    response_json2 = json.loads(response2.text)
                    print(colored("Response Not Ready Wait for 60 Second...",'blue'))
                    flag3 = flag3 -1 
                    time.sleep(60)
                if(response_json2["response_code"] == 1):
                    if(response_json2["positives"] <= 0):
                        t = colored(' [+] Not Malicious', 'green')
                        print(ftc + " " + t)
                    else:
                        temp2 = False
                        t = colored('[-] Malicious','red')
                        print(ftc + " " + t)
                else:
                    t = colored(' [?] Not found in Database','yellow')
                    print(ftc + " " + t )
        time.sleep(60)
#attachments_checker()

