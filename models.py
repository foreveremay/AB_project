from pydantic import BaseModel
from typing import List

class ContractItem(BaseModel):
    description: str
    total: float
    partA: float
    partB: float
    costA: float
    costB: float

class ContractCreate(BaseModel):
    title: str
    intro: str
    executionTime: str
    paymentTerms: str
    created_at: str
    items: List[ContractItem]