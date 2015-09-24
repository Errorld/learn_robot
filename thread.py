from multiprocessing import Process
import os

# 子进程要执行的代码
def func(name):
    print('run %d ,name is %s' %os.getpid(), name)

p = Process(target = func, args='test',)
p.start()
p.join()
