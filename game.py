import random 
import time 
score = 0
numero1 = random.randint(50,200)
numero2 = random.randint(201,350)
numero3 = random.randint(351,500)
numero4 = random.randint(501,650)
resposta1 = numero1 + numero2
resposta2 = numero3 + numero4

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










