from queue import Queue
import socket
import threading 
import time 

print_lock = threading.Lock() 
target = 'localhost'

def portscan(port): 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	try: 
		con = s.connect((target, port)) 
		with print_lock: 
			print('Port is open.', port) 
		con.close() 
	except: 
		print('Port is closed.', port) 

def threader(): 
	while True: 
		worker = q.get() 
		portscan(worker) 
		q.task_done() 

q = Queue() 

for x in range(5): # Edit to change number of threads you want to allow
	t = threading.Thread(target=threader) 
	t.daemon = True
	t.start() 

start = time.time() 
for worker in range(1, 10): 
	q.put(worker) 
q.join() 
