from fastapi import APIRouter 
from queries.toktan import query_toktan 

router = APIRouter(
  prefix="/toktan", 
)

@router.get("/")
async def get_toktan(st:str, ed:str, syozok:str):
  return query_toktan(st, ed, syozok).to_dict(orient="records")