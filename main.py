from fastapi import FastAPI 
from routers.busyo import router as busyo_router 
from routers.zaiko import router as zaiko_router 
from routers.buka import router as buka_router 
from routers.toktan import router as toktan_router 
from routers.soneki import router as soneki_router
from routers.urias import router as urias_router


app = FastAPI(
  title="Ebixショクリュー", 

)

@app.get("/")
async def hello():
  return dict(hello="World!")

app.include_router(busyo_router)
app.include_router(zaiko_router)
app.include_router(buka_router)
app.include_router(toktan_router)
app.include_router(soneki_router)
app.include_router(urias_router)