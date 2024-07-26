import random

jogar_novamente = True

def sorteador():
    numero = random.randint(1, 200)
    return numero

def imprimir_boas_vindas():
    print("Bem Vindo ao jogo da adivinhção!!!")
    print("O número secreto está entre 1 a 200")
    
def Receber_chute():
    chute = int(input("Digite um número entre 1 a 200:"))
    return chute
def verificar_chute(chute, numero_secreto):
    if chute == numero_secreto:
        return True
    elif chute > numero_secreto:
        print("O número secreto é menor que o digitado")
    else:
        print("O número secreto é maior que o digitado")
    
def reiniciar():
    resposta = input("Você deseja jogar novamente?(s/n) ")
    if resposta == "s":
        print("Excelente, vamos jogar de novo")
        return  True
    elif resposta == "n":
        return False

def main():
    tentativas = 0
    acertou = False
    numero_secreto = sorteador()
    imprimir_boas_vindas()
    while not acertou:
        chute = Receber_chute()
        tentativas += 1
        acertou = verificar_chute(chute, numero_secreto)
    if tentativas == 1:
        print(f"parabéns Você acertou o número secreto, que era {numero_secreto} de PRIMEIRA!!!")
    else:
        print(f"parabéns Você acertou o número secreto, que era {numero_secreto} com {tentativas} tentativas!!!")
    

while jogar_novamente:
    main()
    jogar_novamente = reiniciar()
print("Obrigado por jogar!!!")
