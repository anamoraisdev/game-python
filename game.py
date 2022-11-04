import random 
import time 
score = 0

print("Bem-vindo ao Quiz Matemático")
user = input ("Vamos começar? (sim/não):")
if user == "sim":
    print("Começando em ...")
if user == "não":
    quit()

def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
    print('VALENDO!!') 
t = (5) 
countdown(int(t)) 

def gerar_numero:
    return random.randint(50,500)










