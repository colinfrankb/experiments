from multiprocessing import Process
import os
import time

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)
    time.sleep(5)

if __name__ == '__main__':
    info('main line')
    
    p = Process(target=f, args=('bob',))
    p.start()

    while True:
        if not p.is_alive():
            print('exit code:', p.exitcode)
            p = Process(target=f, args=('bob',))
            p.start()
