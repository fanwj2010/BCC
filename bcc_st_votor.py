import time
import zmq
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

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
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
      t_start = time.time()
      message = socket.recv()
      time.sleep(1)
     #print("Received request: %s"% message )
      #socket.send(b"This is Controller3")
      socket.send(msg_encrypt_str)
      t_end = time.time()
      t_dur = t_end - t_start
      print("transmitting time %s"% t_dur)
