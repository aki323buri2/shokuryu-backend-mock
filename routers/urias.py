from fastapi import APIRouter 
from queries.urias import query_urias 

router = APIRouter(
  prefix="/urias", 
)

@router.get("/")
async def get_urias(kjob:str, syozok:str):
  return query_urias(kjob, syozok).to_dict(orient="records")