from sqlmodel import Field, SQLModel, Relationship, create_engine
from enum import Enum
from datetime import datetime,date

class Bancos(Enum):
    NUBANK = 'Nubank'
    SANTANDER  = 'Santander'
    INTER = 'Inter'
    MERCADO_PAGO = 'mercado_pago'
    WILLBANK = 'willbank'

class Status(Enum):
    ATIVO = 'ativo'
    INATIVO = 'inativo'

class Conta(SQLModel, table=True):
    id: int = Field(primary_key=True)
    banco: Bancos = Field(default=Bancos.NUBANK)
    status: Status = Field(default=Status.ATIVO)
    valor: float
    data_criacao: datetime = Field(default_factory=datetime.now)

class Tipos(Enum):
    ENTRADA = 'Entrada'
    SAIDA = 'Saída'

class Historicos(SQLModel, table=True):
    id: int = Field(primary_key=True)
    conta_id: int = Field(foreign_key="conta.id")
    conta: Conta = Relationship()
    tipo: Tipos = Field(default=Tipos.ENTRADA)
    valor: float
    data: date

    # Efetivando a criação da tabela no DB:

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

#engine = create_engine(sqlite_url, echo=True)
engine = create_engine(sqlite_url, echo=False)
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()
