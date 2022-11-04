import random 
import time

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
t = (2) 
countdown(int(t))

def gerar_numero():
    return random.randint(50,500)

def gerar_pergunta():
    numero1 = gerar_numero()
    numero2 = gerar_numero()
    resposta = int(input(f"Quanto é {numero1} + {numero2}: "))
    resultado = numero1 + numero2
    return conferi_resultado(resultado, resposta)

def conferi_resultado (resultado, resposta):
    if resposta == resultado:
        return True
    else:
        return False

def principal():
    perguntas = int(input("Quantas perguntas voce quer: "))
    perguntas_iniciais = perguntas
    acertos = 0
    while perguntas:
        resultado = gerar_pergunta()
        if resultado:
            acertos += 1
            print("Acertou!")
        else:
            print("Errou!")
        perguntas -= 1
    print(f"Você acertou {acertos} de {perguntas_iniciais} perguntas.")
    
principal()
