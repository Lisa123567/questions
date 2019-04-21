# ########## Starting a New ##############
# #!/usr/bin/python3
#
# import _thread
# import time
#
# # Define a function for the thread
# def print_time( threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#
# # Create two threads as follows
# try:
#     _thread.start_new_thread(print_time, ("Thread-1", 1))
#     _thread.start_new_thread(print_time, ("Thread-2", 2))
#     _thread.start_new_thread(print_time, ("Thread-3", 3))
#     _thread.start_new_thread(print_time, ("Thread-4", 4))
#     _thread.start_new_thread(print_time, ("Thread-5", 5))
# except:
#     print ("Error: unable to start thread")
#
# while 2:
#     pass
# ###########################
# ###############The Threading Module ##############
# #!/usr/bin/python3
#
# import threading
# import time
#
# exitFlag = 0
#
# class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print ("Starting " + self.name)
#       print_time(self.name, self.counter, 5)
#       print ("Exiting " + self.name, self.threadID,self.counter )
#
# def print_time(threadName, delay, counter):
#    while counter:
#       if exitFlag:
#          threadName.exit()
#       time.sleep(delay)
#       print ("%s: %s" % (threadName, time.ctime(time.time())))
#       counter -= 1
#
# # Create new threads
# thread1 = myThread(101, "Thread-1", 5)
# thread2 = myThread(202, "Thread-2", 10)
#
# # Start new Threads
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print ("Exiting Main Thread",)
#########################Synchronizing Threads##############
# #!/usr/bin/python3
#
# import threading
# import time
#
# class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print ("Starting " + self.name)
#       # Get lock to synchronize threads
#       threadLock.acquire()
#       print_time(self.name, self.counter,self.threadID, 5)
#       # Free lock to release next thread
#       threadLock.release()
#
# def print_time(threadName, delay, threadID, counter):
#    while counter:
#       time.sleep(delay)
#       print ("%s: %s : %s" % (threadName, threadID,  time.ctime(time.time())))
#       counter -= 1
#
# threadLock = threading.Lock()
# threads = []
#
# # Create new threads
# thread1 = myThread(11, "Thread-1", 1)
# thread2 = myThread(12, "Thread-2", 2)
# thread3 = myThread(13, "Thread-3", 3)
#
# # Start new Threads
# thread1.start()
# thread2.start()
# thread3.start()
#
# # Add threads to thread list
# threads.append(thread1)
# threads.append(thread2)
# threads.append(thread3)
#
# # Wait for all threads to complete
# for t in threads:
#    t.join()
# print ("Exiting Main Thread")
###########################################################
#!/usr/bin/python3

import queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      print ("Starting " + self.name)
      process_data(self.name, self.q)
      print ("Exiting " + self.name)

def process_data(threadName, q):
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
         data = q.get()
         queueLock.release()
         print ("%s processing %s" % (threadName, data))
      else:
         queueLock.release()
         time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
   pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")