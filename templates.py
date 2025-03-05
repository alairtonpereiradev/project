from models import *
from view import *
class UI:
    def start(self):
        while True:
            print('''
            [1] -> Criar conta
            [2] -> Desativar conta
            [3] -> Transferir dinheiro
            [4] -> Movimentar dinheiro
            [5] -> Total contas
            [6] -> Filtrar histórico
            [7] -> Gráfico
                  ''')
            
            choice = int(input('Escolha uma opção: '))

            if choice == 1:
                self._criar_conta()
            elif choice == 2:
                self._desativar_conta()
            elif choice == 3:
                self._transferir_saldo()
            elif choice == 4:
                self._movimentar_dinheiro()
            elif choice == 5:
                self._total_contas()
            elif choice == 6:
                self._filtrar_movimentacoes()
            elif choice == 7:
                self._criar_grafico()
            else:
                break

    def _criar_conta(self):
        print('Digite o nome de algum dos bancos abaixo:')
        for banco in Bancos:
            #print(f'[{banco.value}] -> {banco.name}')
            print(f'---{banco.value}---')
        
        banco = input()#.title()
        valor = float(input('Digite o valor em sua conta: '))
        
        conta = Conta(banco=Bancos(banco), valor=valor)
        criar_conta(conta)
        #print('Conta criada com sucesso!')

    def _desativar_conta(self):
        print('Escolha o número da conta que deseja desativar.')

        for i in listar_contas():
            print(f'{i.id} -> {i.banco} -> R$ {i.valor}')
            if i.valor == 0:
                print(f'{i.id} -> {i.banco.value} -> R$ {i.valor}')

        id_conta = int(input())

        try:
            desativar_conta(id_conta)
            print('Conta desativada com sucesso.')
        except ValueError:
            print('Essa conta ainda possui saldo, faça uma transferência')

    def _transferir_saldo(self):
        print('Escolha a conta retirar o dinheiro.')
        for i in listar_contas():
            print(f'{i.id} -> {i.banco.value} -> R$ {i.valor}')

        conta_retirar_id = int(input())

        print('Escolha a conta para enviar dinheiro.')
        for i in listar_contas():
            if i.id != conta_retirar_id:
                print(f'{i.id} -> {i.banco.value} -> R$ {i.valor}')

        conta_enviar_id = int(input())

        valor = float(input('Digite o valor para transferir: '))
        transferir_saldo(conta_retirar_id, conta_enviar_id, valor)


UI().start()
        

            