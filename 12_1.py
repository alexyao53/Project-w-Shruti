import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
print("Enter Website home URL: ") #'www.py4inf.com'
homeurl = raw_input().strip()
mysock.connect(('www.py4inf.com', 80)) 

print("Enter specific page URL: ") #http://www.py4inf.com/code/romeo.txt
pageurl = raw_input().strip()
mysock.send('GET' pageurl 'HTTP/1.0\n\n')
while True: 
    data = mysock.recv(512) 
    if ( len(data) < 1 ) : 
        break 
    print data
mysock.close()