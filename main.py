# Logica do JOGO DA FORCA

# Coletando palavra secreta do usuario
import desenhos as d
palavra = input('Digite a palavra secreta: ').lower().strip()

# Espaços para que a palavra secreta "desaparecer"
for i in range(50):
    print("")


# Criando variaveis e listas para armazenamento de dados para funcionamento
digitadas = []
acertos = []
erros = 0

# Logica para ocultação da palavra secreta
while True:
    adivinha = d.imprimir_palavra_secreta(palavra, acertos)
# CONDIÇÃO DE VITORIA
    if adivinha == palavra:
            print('ACERTOU!!!')
            break   

    
    
# Coletando a tentativa do usuario 
    while True:
        tentativa = input('Digite uma letra: ').strip().lower()
# Verificando se foi digitada mais de uma letra
        if len(tentativa) != 1:
            print('Digite apenas 1 letra!')
            continue
        else:
            break
# Verificando se o usario ja tentou esse letra
    if tentativa in digitadas:
        print('Você ja tentou essa')
        continue
    
    else:
        digitadas.append(tentativa)
        if tentativa in palavra:
            acertos.append(tentativa)
            adivinha += tentativa
        else:
            erros += 1
            print('Você errou!')
            
            
    
    d.desenhar_forca(erros)
# CONDIÇÃO DE DERROTA
    if erros == 6:
        print('ENFORCADO!!!')
        print(f'A palavra correta é: {palavra}')
        break

# Erro onde era adicionado partes do corpo a mais corrigido!
