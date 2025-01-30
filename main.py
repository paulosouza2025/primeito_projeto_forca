from desenhos import menu
import jogo as j

while True:
    
    menu()
    
    opcao = int(input('Escolha uma opção: '))
    
    if opcao == 1:
        j.jogo()
        input('Aperte qualquer tecla para voltar ao menu...')
        
    elif opcao == 2:
        print('Score em breve!')
        input('Aperte qualquer tecla para voltar ao menu...')
        continue
        
    elif opcao == 3:
        print('Encerrando...')
        break
    else:
        print('Opção invalida!')
        continue
