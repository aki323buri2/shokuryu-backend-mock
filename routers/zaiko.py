from fastapi import APIRouter
from utilities.common import fullpath, load_csv
from decimal import Decimal, ROUND_HALF_UP 

router = APIRouter(
  prefix="/zaiko", 
)

@router.get("/")
async def get_zaiko():
  filename = fullpath("csv/zaiko1.csv")
  df = load_csv(filename)

  def round(x, format):
    return Decimal(x).quantize(Decimal(format), rounding=ROUND_HALF_UP)

  for name in [
    "kgtan", 
  ]:
    df[name] = [str(round(x, "0")) for x in df[name]]
  
  for name in [
    "tou_zjuryo", 
  ]:
    df[name] = [str(round(x, "0.001")) for x in df[name]]
  
  return df.to_dict(orient="records")[:100]