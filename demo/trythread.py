
import thread
import time

count = 0


def threadTest():
    global count
    for i in range(10):
        count += 1
    for i in range(10):
        thread.start_new_thread(threadTest, ())
    time.sleep(3)
    print(count)

threadTest()

#eof
