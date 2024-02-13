from random import randint
cpfValidado = ''
cpf_escolhido = ''

#Escolher 9 números aleatórios para a base do CPF
for i in range(0,9):
    cpf_escolhido = cpf_escolhido + str(randint(0,9))

#Aplicar a fórmula para o 1° e 2° dígito validador
while True:
    soma = 0
    contador = 10 if len(cpf_escolhido) == 9 else 11
    cpf = []
    for N in cpf_escolhido:
        n_a = int(N)
        cpf.append(n_a)
    for num in cpf:
        soma += num * contador
        contador -= 1
    dgt = (soma * 10)% 11 
    if dgt > 9:
        dgt = 0
    cpf_escolhido += str(dgt)
    if len(cpf) == 11:
        break

#Colocar a pontuação correta para CPF
for C in cpf:
    cpfValidado = cpfValidado + ''.join(str(C))
    if len(cpfValidado) == 3 or len(cpfValidado) == 7:
        cpfValidado = cpfValidado + '.'
    if len(cpfValidado) == 11:
        cpfValidado = cpfValidado + '-'

print(f'O CPF validado é: {cpfValidado}')