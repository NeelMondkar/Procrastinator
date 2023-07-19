
import time
import psutil

def process_exists(process_name):
    return process_name in (i.name() for i in psutil.process_iter())

start = 0
while not process_exists("Spotify"):
    pass

start = time.time()

while process_exists("Spotify"):
    pass

end = time.time()
time_used = end - start
print("Time used:", time_used)
