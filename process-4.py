from multiprocessing import Process
import time
import os

def subp(enable):
	while enable[0]:
		print('working subprocess',os.getpid())
		time.sleep(2)
if __name__ == '__main__':
	enable=[True]
	p = Process(target=subp,args=(enable,))
	p.start()
	for i in range(10):
		inpu = input('Ready to input')
		print('input')
		if inpu=='stop':
			enable[0]=False
		time.sleep(1)
	p.join()
	print('fin')