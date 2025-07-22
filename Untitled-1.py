import time

def counting(y):
    if y <= 6:
        print ('я даун')  
        return   
    x = y - 7  
    print(y ,'-7 =' , x)
    time.sleep(0.2)
    counting(x)      

result = counting(1000)  
print(result)  