import time
import random
import threading

semaphore = threading.Semaphore(3)

customers = []

for i in range(30):
    customers.append(i+1)

def attendance():
    for i in customers:
        semaphore.acquire()
        
        print("Caixa " + threading.currentThread().getName() + " está atendendo cliente " + str(i))
        customers.remove(i)
        time.sleep(random.randint(0,1))
        
        semaphore.release()

thread1 = threading.Thread(target = attendance, args = ())
thread2 = threading.Thread(target = attendance, args = ())
thread3 = threading.Thread(target = attendance, args = ())

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()