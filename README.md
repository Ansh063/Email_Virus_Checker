# Email Virus Checker

[![GitHub stars](https://img.shields.io/github/stars/Ansh063/Email_Virus_Checker?color=green)](https://github.com/Ansh063/Email_Virus_Checker/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Ansh063/Email_Virus_Checker?color=green)](https://github.com/Ansh063/Email_Virus_Checker/network)

Email Virus Checker is a `Real Time Monitoring` Tool for Mails. It gets triggered to extract all the links and attachments and scans all the links and attachments and give you a status of Mail. It Uses IMAP (Internet Mail Access Protocol) and Python v3. If it Found that mail contain any`Malicious links or Attachments` then ask for permission to delete and then delete automatically.

# [IMAP (Internet Message Access Protocol)](https://docs.python.org/3/library/imaplib.html)

IMAP (`Internet Message Access Protocol`) is a standard email protocol that stores email messages on a mail server, but allows the end user to view and manipulate the messages as though they were stored locally on the end user's computing device(s). This allows users to organize messages into folders, have multiple client applications know which messages have been read, flag messages for urgency or follow-up and save draft messages on the server.

# [VirusTotal](https://en.wikipedia.org/wiki/VirusTotal)

VirusTotal inspects items with over 70 antivirus scanners and URL/domain blacklisting services. <br>
For more information visit : https://support.virustotal.com/hc/en-us/articles/115002126889-How-it-works

# Generation of API_KEY
```

1. Go to Virustotal Website. Site : https://www.virustotal.com/gui/home/upload 
2. Signup on Virustotal
3. You get Your Free Public API_KEY.
```

# Ussage:

```
1. Install Python3 
2. Install pip 
3. Install all the Requirements using : pip install -r requirements.txt
4. Change Permission of IMAP_Connection.py : chmod a+x IMAP_Connection.py 
5. Change Gmail Permission to allow less secure apps : ON  
6. run : IMAP_Connection [ gmail_id ] [ Password ] [ API_KEY ] 
```
<i><b>Now Your Server has been Configured for New Mails !!!</b></i><br><br>
[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

