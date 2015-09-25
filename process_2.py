from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Tast %s runs %0.2f seconds.' % (os.getpid(), (end-start)))

if __name__=='__main__':
    print('Parent process %s.' % (os.getpid()))
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done')
    print('Parent process %s.' % (os.getpid()))
    for x in range(1,10):
        print('fuck')
        time.sleep(1)
    #p.close()
    p.join()
    print('All subprocesses done')
