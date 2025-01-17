
from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class CustomerBase(SQLModel):
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    email: str = Field(default=None)
    age: int = Field(default=None)

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class Customer(CustomerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
    
class TransactionBase(SQLModel):
    ammount: int
    description: str


class Transaction(TransactionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    
class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction] 
    total: int  
    
    @property
    def total(self):
        return sum(transaction.ammount for transaction in self.transactions)