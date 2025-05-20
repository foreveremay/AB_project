from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from models import ContractCreate
from database import contract_collection
from datetime import datetime
from bson import ObjectId

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/contracts")
async def create_contract(contract: ContractCreate):
    data = contract.dict()
    data["created_at"] = data.get("created_at") or datetime.utcnow().isoformat()
    result = await contract_collection.insert_one(data)
    return {"id": str(result.inserted_id)}

@app.get("/api/contracts/search")
async def search_contracts(
    keyword: str = "",
    startDate: str = "",
    endDate: str = "",
    item: str = ""
):
    query = {"$and": []}
    if keyword:
        query["$and"].append({"$or": [
            {"title": {"$regex": keyword, "$options": "i"}},
            {"intro": {"$regex": keyword, "$options": "i"}}
        ]})
    if item:
        query["$and"].append({"items.description": {"$regex": item, "$options": "i"}})
    if startDate:
        query["$and"].append({"created_at": {"$gte": startDate}})
    if endDate:
        query["$and"].append({"created_at": {"$lte": endDate}})
    if not query["$and"]:
        query = {}

    results = await contract_collection.find(query).to_list(length=50)
    for r in results:
        r["_id"] = str(r["_id"])
    return results

@app.delete("/api/contracts/{contract_id}")
async def delete_contract(contract_id: str):
    result = await contract_collection.delete_one({"_id": ObjectId(contract_id)})
    if result.deleted_count == 1:
        return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Contract not found")