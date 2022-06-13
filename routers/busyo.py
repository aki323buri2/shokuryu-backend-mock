from fastapi import APIRouter 
from utilities.common import load_csv 
router = APIRouter(
  prefix="/busyo", 
)

@router.get("/")
async def get_busyo():
  df = load_csv("csv/busyo.csv")
  return df.to_dict(orient="records")