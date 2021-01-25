import socket
import time
import threading
from multiprocessing import Process

def request():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(address)  ## <--Add this line.
    client.send(b"GET / HTTP/1.0\r\n\r\n")
    client.recv(12)
    client.close()

def process():
    processes = list()

    for i in range(0, 1000):
        process = Process(target=request)
        process.start()
        processes.append(process)
    for process in processes:
        process.join()

def thread():
    threads = list()

    for i in range(0, 1000):
        thread = threading.Thread(target=request)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


ip=socket.gethostbyname("127.0.0.1")
port=80
address=(ip,port)

start = time.time()
process()
end = time.time()
print(end - start)

start = time.time()
thread()
end = time.time()
print(end - start)