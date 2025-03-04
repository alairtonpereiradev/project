from models import Conta, Bancos, engine
from sqlmodel import Session, select


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
#conta = Conta(valor=1000, banco=Bancos.INTER)
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
            raise ValueError('Essa conta ainda possui saldo, não é possível desativar.')
            return
        conta.status = Status.INATIVO
        session.commit()
        return result

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