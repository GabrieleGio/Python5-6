import time
import sys
sys.stdout = open("./file_per_le_print.txt","w+")
i = 1
while (i<10):
    print("Ciao")
    sys.stdout.flush()
    time.sleep(3)
    i+=1
sys.stdout.close()