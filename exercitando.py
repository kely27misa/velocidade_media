#MAIORES DE 18 ANOS

idade = (input("Informe sua idade: "))
rm = input("Informe seu RM: ")

if int(idade) >= 18:
    print("Sua participação foi autorizada, aluno de RM {}!".format(rm))
    print("Mais  informações  serão  enviadas  para  seu  e-mail cadastrado!")
else:
    autorizado = input("Você  possui  autorização  dos responsáveis? S-SIM ou N-NÃO: ")
if autorizado == 'S':
    print("Sua participação foi autorizada, aluno de RM {}!".format(rm))
    print("Mais  informações  serão  enviadas  para  seu  e-mail cadastrado!")
else: print("Sua  participação  não  foi  autorizada  por causada sua idade")
