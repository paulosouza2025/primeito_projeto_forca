# Logica do JOGO DA FORCA

# Coletando palavra secreta do usuario
palavra = input('Digite a palavra secreta: ').lower().strip()

# Espaços para que a palavra secreta "desaparecer"
for i in range(50):
    print("")


# Criando variaveis e listas para armazenamento de dados para funcionamento
digitadas = []
acertos = []
erros = 0
linha3 = 'X'
linha4 = 'X'
linha5 = 'X'

# Logica para ocultação da palavra secreta
while True:
    adivinha = ''
    for letra in palavra:
        if letra in acertos:
            adivinha += letra
        else:
            adivinha += '\u23BD'
    
# CONDIÇÃO DE VITORIA
    if adivinha == palavra:
            print('ACERTOU!!!')
            break

    print (f'Adivinhe: {adivinha}, {len(palavra)} letras ')
    
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
            if erros == 1:
                linha3 += '  O'
            if erros == 2:
                linha4 += ' /'
            if erros == 3:
                linha4 += '|'
            if erros == 4:
                linha4 += '\ '
            if erros == 5:
                linha5 += ' /'
            if erros == 6:
                linha5 += ' \ '
            print('Você errou!')
            
            
    
# DESENHO DA FORCA
    print('X==:==')
    print('X  :')
    print(linha3)
    print(linha4)
    print(linha5)
    print('X\n=========')

# CONDIÇÃO DE DERROTA
    if erros == 6:
        print('ENFORCADO!!!')
        print(f'A palavra correta é: {palavra}')
        break

# Erro onde era adicionado partes do corpo a mais corrigido!
