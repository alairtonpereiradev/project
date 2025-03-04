from sqlmodel import Field, SQLModel, create_engine
from enum import Enum
from datetime import datetime

class Bancos(Enum):
    NUBANK = 'Nubanks'
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

    # Efetivando a criação da tabela no DB:

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()
