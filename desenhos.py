def imprimir_palavra_secreta(palavra, acertos):
    adivinha = ''
    for letra in palavra:
        if letra in acertos:
            adivinha += letra
        else:
            adivinha += '\u23BD'
    print (f'Adivinhe: {adivinha}, {len(palavra)} letras ')
    return adivinha

def desenhar_forca(erros):
    print("X==:==")
    print("X  :  ")
    if erros >= 1:
        print('X  O  ')
        
    else:
        print('X')
        
    linha2 = ""
    if erros == 2:
        linha2 = "  | "
        
    elif erros == 3:
        linha2 = " /| "
        
    elif erros >= 4:
        linha2 = " /|\ "
        
    print(f"X{linha2}")
    
    linha3 = ""
    if erros == 5:
        linha3 += " / "
        
    elif erros >= 6:
        linha3 += " / \ "
        
    print(f"X{linha3}")
    
    print(f"X\n=======")
    
def menu():
    print(30*'=')
    print(''*7+'JOGO DA FORCA')
    print(30*'=')
    print('\n1 - JOGAR')
    print('2 - SCORE')
    print('3 - SAIR\n')
    print(30*'=')