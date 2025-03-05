from models import Conta, Bancos, Status, Historicos, Tipos, engine
from sqlmodel import Session, select
from datetime import date, datetime, timedelta


# usuário possa criar contas dentro da aplicação
def criar_conta(conta: Conta):
    with Session(engine) as session:
        # recebe a pesquisa de uma conta de banco
        statement = select(Conta).where(Conta.banco==conta.banco)
        results = session.exec(statement).all()
        if results:
            print(f"Conta {conta.banco} já existe.")           
            return
        session.add(conta)
        session.commit()
        return Conta
        print(f"Conta {conta.banco} criada com sucesso.")

# Debug
#conta = Conta(valor=150, banco=Bancos.MERCADO_PAGO)
#criar_conta(conta)

# função responsável em listar todas as contas
def listar_contas():
    with Session(engine) as session:
        statement = select(Conta).order_by(Conta.banco)
        results = session.exec(statement).all()
    return results
# Debug
#for i in listar_contas():
#    print(i.banco)

# função responsável por desativar uma determinada conta

def desativar_conta(id):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id==id)
        conta = session.exec(statement).first()
        if conta.valor > 0:
            # raise gera uma excessão (exception)
            raise ValueError('Essa conta ainda possui saldo, não é possível desativar.')
            return
        conta.status = Status.INATIVO
        session.commit()
        
# Debug
#desativar_conta(2)

# aula 1: 51:52

def transferir_saldo(id_conta_saida, id_conta_entrada, valor):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id==id_conta_saida)
        conta_saida = session.exec(statement).first()        
        if conta_saida.valor < valor:
            raise ValueError('Saldo Insuficiente')
        statement = select(Conta).where(Conta.id==id_conta_entrada)
        conta_entrada = session.exec(statement).first()
        
        conta_saida.valor -= valor
        conta_entrada.valor += valor
        session.commit()

# Debug (id conta de saida, id conta de entrada e valor)
# transferir_saldo(1, 3, 10)

# 1:28:45 - Movimentação financeira

def movimentar_dinheiro(historicos: Historicos):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id==historicos.conta_id)
        conta =session.exec(statement).first()
        # validar o status da conta.
        if conta.status == Status.INATIVO:
            raise ValueError('Conta Inativa')
        else:
            if historicos.tipo == Tipos.ENTRADA:
                conta.valor += historicos.valor
            else:
                if conta.valor < historicos.valor:
                    raise ValueError('Saldo Insuficiente')
                    conta.valor -= historicos.valor

        session.add(historicos)
        session.commit()
        return historicos

# Debug
#historicos = Historicos(conta_id=3, tipos=Tipos.ENTRADA, valor=10, data=date.today())
#movimentar_dinheiro(historicos)

def total_contas():
    with Session(engine) as session:
        statement = select(Conta)
        contas = session.exec(statement).all()

        total = 0
        for conta in contas:
            total += conta.valor

        return float(total)

# Debug

# Filtro de movimentações financeiras

def buscar_historicos_entre_datas(data_incio: date, data_fim: date):
    with Session(engine) as session:
        statement = select(Historicos).where(
            Historicos.data >= data_incio,
            Historicos.data <= data_fim
        )
        resultados = session.exec(statement).all()
        return resultados

# Debug
#x = buscar_historicos_entre_datas(date.today() - timedelta(days=2), date.today() + timedelta(days=2))
#print(x)

# Gráfico que mostra  total de dinheiro

def criar_grafico_por_conta():
    with Session(engine) as session:
        statement = select(Conta).where(Conta.status==Status.ATIVO)
        contas = session.exec(statement).all()
        bancos = [i.banco.value for i in contas]
        total = [i.valor for i in contas]
        import matplotlib.pyplot as plt
        plt.bar(bancos, total)
        plt.show()

# Debug
# criar_grafico_por_conta()