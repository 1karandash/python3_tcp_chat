import socket
import threading

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55555))

def receive():
	while True:
		try:
			# receive message from server
			# if "NICK" send Nickname
			message = client.recv(1024).decode("ascii")
			if message == "NICK":
				client.send(nickname.encode("ascii"))
			else:
				print(message)
		except:
			# close when error
			print("An error occured!")
			client.close()
			break
			
			
def send():
	while True:
		inp = input("")
		if inp == "quit":
			client.close()
		else:
			message = "{}: {}".format(nickname, inp)
			client.send(message.encode("ascii"))
		
receive_thread = threading.Thread(target = receive)
send_thread = threading.Thread(target = send)

receive_thread.start()
send_thread.start()



