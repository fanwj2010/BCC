import time
import zmq
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

t_1 = time.time()
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
publickey = key.publickey()
#privatekey = key.privatekey()

msg_plaintext_str = "alert tcp 10.0.2.5 any -> any 80 (msg:\"DROP\"; sid:1000008; priority:0;)"
#msg_plaintext_str = "10.0.2.5"
msg_encrypt = publickey.encrypt(msg_plaintext_str, 32)
msg_encrypt_str = str(msg_encrypt)
#print(msg_encrypt_str)

context = zmq.Context()

print("Connection to the receiver")
socket0 = context.socket(zmq.REQ)
socket0.connect("tcp://10.0.2.4:5555")

#print("Connection to the Controller1")
#socket1 = context.socket(zmq.REQ)
#socket1.connect("tcp://10.0.2.7:5555")
t_2 = time.time()
t_dur = t_2 - t_1
print(t_dur)

for request in range(11):
    #print("Sending request %s..." % request)
    t_start = time.time()
#   sleep.time(1)
    #socket.send(u"alert tcp 10.0.2.5 any -> any 80 (msg:\"DROP\"; sid:1000008; priority:0;)")
    #socket.send(msg_plaintext_str)
    #socket3.send(msg_encrypt_str)
    socket0.send(msg_encrypt_str)
    #message3 = socket3.recv()
    message0 = socket0.recv()
    t_end = time.time()
    t_dur = t_end - t_start
    #time.sleep(0.1)
    #print("Received reply %s [%s]" %(request,message3))
    print("Received reply %s [%s]" %(request,message0))
   # print("latency %s" %(t_dur))
    print( (t_dur))

