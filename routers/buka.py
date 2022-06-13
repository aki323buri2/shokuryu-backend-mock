from fastapi import APIRouter 
from queries.buka import query_buka 

router = APIRouter(
  prefix="/buka", 
)

@router.get("/")
async def get_buka():
  return query_buka().to_dict(orient="records")