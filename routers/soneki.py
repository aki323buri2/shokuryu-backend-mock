from fastapi import APIRouter 
from queries.soneki import query_soneki 

router = APIRouter(
  prefix="/soneki", 
)

@router.get("/")
async def get_soneki(kjob:str, syozok:str):
  return query_soneki(kjob, syozok).to_dict(orient="records")