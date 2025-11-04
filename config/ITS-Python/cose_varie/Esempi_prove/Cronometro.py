# Creare un decorator che permette di fare un cronometro per un'altra funzione

def cronometro(fun):
    def wrapper(*args):
        import time
        start = time.time()
        temp= fun(*args)
        print(time.time() - start)
        return temp
    return wrapper
'''
@cronometro
def prova():
    for i in range (10000000):
        pass
'''

dict = {
    1: "2"

}

a = dict.pop(1)
print(a)
print(dict)