from util import *

def t_log():
    init_log()

def t_progressbar():
    from random import randint
    N=50
    while True:
        pos=randint(0,N)
        progressbar(N,pos)
        
def t_waitnot():
    for i in range(100):        
        waitnot()        
        
t_waitnot()
